package main

import (
	"fmt"
)

func merge(left, right []int) []int{
	
	result := []int{}
	i, j := 0, 0

	for i<len(left) && j<len(right){
		if left[i] < right[j]{
			result = append(result, left[i])
			i++
		} else{
		if right[j] < left[i]{
			result = append(result, right[j])
			j++
		}
		}
	}
	
	result = append(result, left[i:]...)
	result = append(result, right[j:]...)
	
	return result
}

func mergeSort(arr []int) []int{
	if len(arr) <= 1{
		return arr
	}

	mid := len(arr)/2

	left := mergeSort(arr[:mid])
	right := mergeSort(arr[mid:])

	return merge(left, right)
}

func main(){
	// var n int
	// fmt.Println("Enter the number of elements you want in the array : ")
	// fmt.Scan(&n)

	// arr := make([]int,n)

	// fmt.Println("Enter elements:")

	// for i:=0;i<n;i++{
	// 	fmt.Scan(&arr[i])
	// }

	// fmt.Println(arr)

	arr := []int{38, 27, 43, 3, 9, 82, 10}
	sorted := mergeSort(arr)

	fmt.Println("Sorted array:", sorted)
}