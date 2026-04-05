package main

import (
	"fmt"
)

func insertionSort(arr []int){

	for i:=1;i<len(arr);i++{
		key:=arr[i]
		j:=i-1

		for j>=0 && arr[j]>key{
			arr[j+1] = arr[j]
			j--
		}

		arr[j+1] = key
	}

} 

func main() {
	var n int
	fmt.Println("Enter size of array : ")
	fmt.Scan(&n)

	arr := make([]int, n)

	fmt.Println("Enter the elements:")
	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	insertionSort(arr)

	fmt.Println("Sorted array:", arr)

}