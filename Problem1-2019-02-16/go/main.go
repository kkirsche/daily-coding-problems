package main

import "fmt"

func calculate(l []int, k int) bool {
	seen := map[int]int{}
	for _, n := range l {
		diff := k - n
		if _, ok := seen[diff]; ok {
			return true
		}
		seen[n] = n
	}

	return false
}

func main() {
	k := 17
	l := []int{10, 15, 3, 7}
	fmt.Println(calculate(l, k))
}
