package main

type Task struct {
	ID        int
	Title     string
	Completed bool
}

func addTask(tasks []Task, title string) []Task {
	id := len(tasks) + 1
	newTask := Task{ID: id, Title: title, Completed: false}
	return append(tasks, newTask)
}

func completeTask(tasks []Task, id int) []Task {
	for i := range tasks {
		if tasks[i].ID == id {
			tasks[i].Completed = true
		}
	}
	return tasks
}