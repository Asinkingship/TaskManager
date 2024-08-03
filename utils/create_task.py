import requests

URL = "http://127.0.0.1:5000/tasks"

def create_task(name, summary, description):
    task_data = {
        "name": name,
        "summary": summary,
        "description": description
    }
    response = requests.post(URL, json=task_data)
    if response.status_code == 204:
        print("Task successfully created")
    else:
        print("Task creation failed")

if __name__ == "__main__":
    print("Create a new task by filling out the prompts below:")
    name = input("Task name: ")
    summary = input("Task summary: ")
    description = input("Task description: ")
    create_task(name, summary, description)
