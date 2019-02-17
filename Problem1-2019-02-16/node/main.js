function calculate(num_list, target_sum) {
  var seen = new Set();
  for (let n of num_list) {
    const diff = target_sum - n;
    if (seen.has(diff)) {
      return true;
    }
    seen.add(n);
  }
  return false;
}

module.exports = calculate;
