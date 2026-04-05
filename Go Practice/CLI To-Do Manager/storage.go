package main

import (
	"encoding/json"
	"os"
)

// Save tasks to JSON file
func saveTasks(tasks []Task) {
	file, _ := os.Create("tasks.json")
	defer file.Close()
	json.NewEncoder(file).Encode(tasks)
}

// Load tasks from JSON file
func loadTasks() []Task {
	var tasks []Task
	file, err := os.Open("tasks.json")
	if err != nil {
		return tasks
	}
	defer file.Close()
	json.NewDecoder(file).Decode(&tasks)
	return tasks
}