package main

import (
	"fmt"
)

func selectionSort(arr []int) []int {
	n := len(arr)

	for i := 0; i < n-1; i++ {
		minIndex := i

		for j := i + 1; j < n; j++ {
			if arr[j] < arr[minIndex] {
				minIndex = j
			}
		}

		//Swap the minimum element from the remaining array
		arr[i], arr[minIndex] = arr[minIndex], arr[i]
		fmt.Println(arr)

	}

	return arr

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

	sortedArr := selectionSort(arr)

	fmt.Println("Sorted array:", sortedArr)

}
