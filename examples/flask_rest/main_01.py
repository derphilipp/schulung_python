from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

todos = {"0": "Zucchini kaufen"}

parser = reqparse.RequestParser()
parser.add_argument("description")


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        args = parser.parse_args()
        print(f"{args}")
        description = request.form["data"]
        todos[todo_id] = description
        return {todo_id: todos[todo_id]}


api.add_resource(TodoSimple, "/<string:todo_id>")

if __name__ == "__main__":
    app.run(debug=True)


# Eintrag anlegen:
# curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT

# Eintrag auslesen:
# curl http://localhost:5000/todo1
