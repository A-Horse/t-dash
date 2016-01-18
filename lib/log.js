'use strict';

let config = global.config;

module.exports = () => {
    let args = Array.prototype.slice.call(arguments);
    switch (config.log) {
    case 'file':
        break;
    default:
        concole.log(args);
    }
};
