from flask import(
    Flask,
    request
)
from app.database import task

app = Flask(__name__)

#http get method

@app.get("/tasks")
def get_all_tasks():
    task_list = task.scan()
    out = {
        "tasks" : task_list,
        "ok" : True
    }
    return out

@app.get("/tasks/<int:pk>/")
def get_single_task(pk):
    single_task = task.select_by_id(pk)
    if single_task:
        out = {
            "task": single_task,
            "ok": True
        }
        return out
    out = {
        "ok": False,
        "message":"Not Found"
    }
    return out, 404

@app.post("/tasks")
def create_task():
    task_data = request.json
    task.insert(task_data)
    return "", 204

@app.put("/tasks/<int:pk>/")
def update_task(pk):
    task_data = request.json
    task.update_by_id(task_data,pk)
    return "", 204

@app.delete("/tasks/<int:pk>/")
def delete_task(pk):
    task.delet_by_id(pk)
    return "", 204

