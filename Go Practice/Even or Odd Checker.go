package main

import (
	"fmt"
)

func main() {
	var i int
	fmt.Print("Enter a number : ")

	fmt.Scan(&i)

	if i%2 == 0 {
		fmt.Println("This is an Even number")
	} else if i%2 != 0 {
		fmt.Println("This is an Odd number")
	}
}
