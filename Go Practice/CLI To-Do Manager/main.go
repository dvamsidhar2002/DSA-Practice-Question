package main

import "fmt"

func main() {
	tasks := loadTasks()

	for {
		fmt.Println("\n1. Add Task")
		fmt.Println("2. View Tasks")
		fmt.Println("3. Complete Task")
		fmt.Println("4. Exit")

		var choice int
		fmt.Print("Enter choice: ")
		fmt.Scan(&choice)

		switch choice {

		case 1:
			var title string
			fmt.Print("Enter task: ")
			fmt.Scanln(&title)
			tasks = addTask(tasks, title)
			saveTasks(tasks)

		case 2:
			fmt.Println("\nTasks:")
			for _, t := range tasks {
				fmt.Println(t.ID, "-", t.Title, "| Completed:", t.Completed)
			}

		case 3:
			var id int
			fmt.Print("Enter Task ID: ")
			fmt.Scan(&id)
			tasks = completeTask(tasks, id)
			saveTasks(tasks)

		case 4:
			fmt.Println("Goodbye 👋")
			return
		}
	}
}