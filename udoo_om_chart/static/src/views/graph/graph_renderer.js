/** @odoo-module **/

import { _t } from '@web/core/l10n/translation';
import { patch } from '@web/core/utils/patch';
import { cookie } from '@web/core/browser/cookie';
import { GraphRenderer } from '@web/views/graph/graph_renderer';
import { SEP } from '@web/views/graph/graph_model';
import { DEFAULT_BG, getColor, hexToRGBA } from '@web/core/colors/colors';

const NO_DATA = _t('No data');

/**
 * Used to avoid too long legend items.
 * @param {string} label
 * @returns {string} shortened version of the input label
 */
function shortenLabel(label) {
    // string returned could be wrong if a groupby value contain a ' / '!
    const groups = label.toString().split(SEP);
    let shortLabel = groups.slice(0, 3).join(SEP);
    if (shortLabel.length > 30) {
        shortLabel = `${shortLabel.slice(0, 30)}...`;
    } else if (groups.length > 3) {
        shortLabel = `${shortLabel}${SEP}...`;
    }
    return shortLabel;
}

patch(GraphRenderer.prototype, {
    getBarChartData() {
        const data = super.getBarChartData();

        data['datasets'].forEach((dataset) => {
            if (dataset.order != -1) {
                dataset.barPercentage = 0.5;
            }
        });

        return data;
    },

    getLineChartData() {
        const data = super.getLineChartData();

        const { stacked, cumulated } = this.model.metaData;

        for (let index = 0; index < data.datasets.length; ++index) {
            const dataset = data.datasets[index];
            dataset.pointBorderWidth = 2.5;
            dataset.pointHoverBorderWidth = 2.5;
            dataset.pointBackgroundColor = '#fff';
            dataset.pointBorderColor = dataset.borderColor;
            if (stacked) {
                dataset.backgroundColor = dataset.borderColor;
            }

            if (stacked && !cumulated) {
                const { height } = this.containerRef.el.getBoundingClientRect();
                const x2d = this.canvasRef.el.getContext('2d');
                const o = x2d.createLinearGradient(0, 0, 0, height * 0.9);
                o.addColorStop(0, dataset.backgroundColor);
                o.addColorStop(1, hexToRGBA(dataset.backgroundColor, 0.0072));
                dataset.backgroundColor = o;
                dataset.fill = true;
            }
        }

        return data;
    },

    getElementOptions() {
        const elementOptions = super.getElementOptions();
        if (elementOptions.line) {
            elementOptions.line.borderWidth = 2.5;
        }

        elementOptions.point = {
            pointStyle: 'circle',
            radius: 5,
            hoverRadius: 7,
            borderWidth: 3,
            hoverBorderWidth: 3,
            backgroundColor: '#ffffff',
            hoverBackgroundColor: '#ffffff',
        }

        return elementOptions;
    },

    getLegendOptions() {
        const legendOptions = super.getLegendOptions();
        const scheme = cookie.get('color_scheme');
        const fontColor = scheme === 'dark' ? '#fff' : '#000';
        const { mode } = this.model.metaData;

        if (mode === 'pie') {
            legendOptions.labels = {
                generateLabels: (chart) => {
                    const data = chart.data;
                    if (data.labels.length && data.datasets.length) {
                        return data.labels.map((label, i) => {
                            return {
                                index: i,
                                text: shortenLabel(label),
                                fullText: label,
                                hidden: !chart.getDataVisibility(i),
                                fillStyle: label === NO_DATA ? DEFAULT_BG : getColor(i, scheme),
                                strokeStyle: data.datasets[0]['backgroundColor'][i],
                                fontColor: fontColor,
                            };
                        });
                    }
                    return [];
                }
            }
        }
        else {
            const superGenerator = legendOptions.labels.generateLabels;
            legendOptions.labels = {
                generateLabels: (chart) => {
                    const labels = superGenerator(chart).map((vals, i) => {
                        const label = { ...vals, fontColor };
                        return label;
                    });
                    return labels;
                },
            };
        }

        return legendOptions;
    },

    getScaleOptions() {
        const scaleOptions = super.getScaleOptions();

        if (scaleOptions.x && scaleOptions.y) {
            scaleOptions.x.grid = {
                display: false,
            }
            scaleOptions.y.grid = {
                drawTicks: false,
            }
        }

        return scaleOptions;
    },
});
