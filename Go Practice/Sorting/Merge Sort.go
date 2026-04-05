package main

import (
	"fmt"
)

func mergeSort(arr []int){
	n:=len(arr)

	
}

func main(){
	var n int
	fmt.Println("Enter the number of elements you want in the array : ")
	fmt.Scan(&n)

	arr := make([]int,n)

	fmt.Println("Enter elements:")

	for i:=0;i<n;i++{
		fmt.Scan(&arr[i])
	}

	fmt.Println(arr)
}