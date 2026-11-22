import test from 'node:test';import assert from 'node:assert/strict';
import {analyse} from '../web/model.mjs';
test('listing date never fills an unknown decision date',()=>{const a=analyse([{institution:'X',year:'2026',listing_date:'2026-01-01',decision_date:null,outcome:'Not classified from summary'}],{},{});assert.equal(a.metrics[2].value,0);assert.equal(a.metrics[3].value,0);});
