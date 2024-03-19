odoo.define('@web/core/colors/colors', [], function (require) {
    'use strict';

    const COLORS_BRIGHT = [
        '#22c3aa',
        '#26a0fc',
        '#8b75d7',
        '#ff6178',
        '#febc3b',
        '#36cbcb',
        '#4ecb74',
        '#FBD437',
        '#F2637B',
        '#975FE5',
        '#5254CF',
        '#435188',
        '#26e7a6',
        '#b9ace7',
        '#f5869e',
        '#f2b3ef',
        '#ffb980',
        '#6be6c1',
        '#59c4e6',
        '#2ec7c9',
        '#ffb980',
        '#ffcd56',
        '#a0bee6',
    ];

    const COLORS_DARK = [
        '#68aca6',
        '#b6a2de',
        '#5ab1ef',
        '#ffb980',
        '#d87a80',
        '#8d98b3',
        '#e5cf0d',
        '#97b552',
        '#95706d',
        '#dc69aa',
        '#07a2a4',
        '#9a7fd1',
        '#2ec7c9',
        '#f5994e',
        '#c05050',
        '#59678c',
        '#c9ab00',
        '#7eb00a',
        '#6f5553',
        '#c14089',
    ];

    function getColors(colorScheme) {
        return colorScheme === 'dark' ? COLORS_DARK : COLORS_BRIGHT;
    }

    /**
     * @param {number} index
     * @param {string} colorScheme
     * @returns {string}
     */
    function getColor(index, colorScheme) {
        const colors = getColors(colorScheme);
        return colors[index % colors.length];
    }

    const DEFAULT_BG = '#d3d3d3';

    function getBorderWhite(colorScheme) {
        return colorScheme === 'dark' ? 'rgba(0, 0, 0, 0.6)' : 'rgba(255,255,255,0.6)';
    }

    const RGB_REGEX = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i;

    /**
     * @param {string} hex
     * @param {number} opacity
     * @returns {string}
     */
    function hexToRGBA(hex, opacity) {
        const rgb = RGB_REGEX.exec(hex)
            .slice(1, 4)
            .map((n) => parseInt(n, 16))
            .join(',');
        return `rgba(${rgb},${opacity})`;
    }

    return { getColors, getColor, DEFAULT_BG, getBorderWhite, hexToRGBA };
});
