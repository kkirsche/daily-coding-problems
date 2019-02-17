var expect = require('chai').expect;
var calculate = require('../main');

describe('calculate(l, k)', function() {
  it('should calculate if any two numbers sums equal k', function () {
    const k = 17;
    const l = [10, 15, 3, 7];

    const r = calculate(l, k);

    expect(r).to.be.equal(true);
  });
});
