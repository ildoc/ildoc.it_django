/* tslint:disable:no-unused-variable */

import { addProviders, async, inject } from '@angular/core/testing';
import { SummaryPipe } from './summary.pipe';

describe('Pipe: Summary', () => {
  it('create an instance', () => {
    let pipe = new SummaryPipe();
    expect(pipe).toBeTruthy();
  });
});
