'use strict';

let config = global.config || {};

export default (...args) => {
    switch (config.log) {
    case 'file':
        break;
    default:
        console.log(...args);
    }
};
