'use strict';

import * as fs from 'fs';
import * as path from 'path';

import * as util from '../lib/util';


let parse = (version) => {
    let docsetPath = path.resolve('../docset/nodejs/', version + '.json');
    util.loadFile(docsetPath, (err, docsetData) => {
        if (err) {
            console.log('..');
        }
        let docsetJson = JSON.parse(docsetData);
        console.log(docsetData);
    });
};

export default parse;
