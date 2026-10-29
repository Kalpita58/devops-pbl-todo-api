from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage: data resets whenever the application restarts.
todos = [
    {"id": 1, "task": "Complete DevOps PBL", "completed": False}
]
next_id = 2


@app.get("/")
def home():
    return jsonify({
        "message": "Todo API is running",
        "endpoints": ["/todos", "/health"]
    })


@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.get("/todos")
def get_todos():
    return jsonify(todos), 200


@app.post("/todos")
def add_todo():
    global next_id
    data = request.get_json(silent=True) or {}
    task = data.get("task")

    if not isinstance(task, str) or not task.strip():
        return jsonify({"error": "Provide a non-empty 'task' string."}), 400

    todo = {"id": next_id, "task": task.strip(), "completed": False}
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
