'use strict';

import * as fs from 'fs';
import * as path from 'path';

import * as util from '../lib/util';


let parse = (version) => {
    let docsetPath = path.resolve('docset/nodejs/', version + '.json');
    util.loadFile(docsetPath, (err, docsetData) => {
        if (err) {
            
        }

        let docsetJson = JSON.parse(docsetData);
        Object.keys(docsetJson).map((k) => {
            Object.keys(docsetJson[k]).map(function(l){
                console.log(l);
            });
        });
    });
};

parse('v5.3.10');

export default parse;
