package main

import "testing"

func TestCalculate(t *testing.T) {
	k := 17
	numList := []int{10, 15, 3, 7}

	r := calculate(numList, k)
	if r != true {
		t.FailNow()
	}
}
