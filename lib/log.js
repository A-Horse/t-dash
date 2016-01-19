'use strict';

let config = global.config;

export default () => {
    let args = Array.prototype.slice.call(arguments);
    switch (config.log) {
    case 'file':
        break;
    default:
        console.log(args);
    }
};
