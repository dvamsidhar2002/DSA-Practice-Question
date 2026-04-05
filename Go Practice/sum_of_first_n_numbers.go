package main

import (
	"fmt"
)

func main() {
	var n int
	sum := 0

	fmt.Print("Enter how many first n numbers you want to sum : ")
	fmt.Scan(&n)

	for i := 1; i <= n; i++ {
		sum += i
	}

	fmt.Print("Sum of first ", n, " numbers is ", sum)
}
