'use strict';

var fs = require('fs'),
    path = require('path');

let util = require('../lib/util');


module.exports = {

    parse: (version) => {
        let docsetPath = path.resolve('../docset/nodejs/', version + '.json');
        util.loadFile(docsetPath, (err, docsetData) => {
            if (err) {
                
            }
            let docsetJson = JSON.parse(docsetData);
        })
    }
}
