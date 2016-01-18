'use strict';

let fs = require('fs'),
    path = require('path');



module.exports = {
    loadFile: (filePath, cb) => {
        fs.readFile(filePath, 'utf-8', (err, data) => {
            if (err) {
                cb(err);
            }
            return cb(null, data);
        });
    }
}
