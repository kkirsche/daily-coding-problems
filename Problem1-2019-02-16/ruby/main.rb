#!/usr/bin/env ruby

require "set"
require "minitest/autorun"

def calculate(num_list, num_sum)
  seen = Set[]
  num_list.each do |n|
    diff = num_sum - n
    if seen.include?(diff)
      return true
    end
    seen.add(n)
  end
  return false
end

class TestCalculate < Minitest::Test
  def test_calculate
    l = [10, 15, 3, 7]
    k = 17
    r = calculate(l, k)
    assert_equal(r, true)
  end
end
