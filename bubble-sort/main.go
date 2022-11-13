package main

import "fmt"

func main() {
	numbers := [10]int32{1, 5, 3, 32, 43, 23, 3, 2, 4, 8}
	noMoreSwaps := false
	end := len(numbers) - 1
	for j := 0; j < len(numbers)-1; j++ {
		noMoreSwaps = true
		for k := 0; k < end; k++ {
			if numbers[k] > numbers[k+1] {
				numbers[k], numbers[k+1] = numbers[k+1], numbers[k]
				noMoreSwaps = false
			}
		}
		end -= 1
		if noMoreSwaps {
			break
		}
	}
	fmt.Println(numbers)
}