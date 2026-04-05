package main

import (
	"fmt"
)

func main(){
	var num int
	fact := 1

	fmt.Print("Enter which number's factorial you want to print : ")
	fmt.Scan(&num)

	for i:=1; i<=num; i++{
		fact*=i
	}

	fmt.Print("Factorial of ",num," is ",fact)
}