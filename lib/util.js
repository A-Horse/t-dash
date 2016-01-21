'use strict';

import * as fs from 'fs';
import * as path from 'path';

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
