from flask import Flask
from flask_restful import reqparse, Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {
    "0": {"description": "Remember the milk"},
    "1": {"description": "Remember the milk"},
}

parser = reqparse.RequestParser()
parser.add_argument("description")


class ToDosAll(Resource):
    def get(self):
        return {"todos": todos}

    def put(self):
        args = parser.parse_args()
        print(args)
        description = args["description"]
        # Generate ID by incrementing counter
        todo_id = str(len(todos))
        todos[todo_id] = {"description": description}
        return {"id": todo_id, "description": todos[todo_id]}


class ToDos(Resource):
    def get(self, todo_id):
        return todos[todo_id]

    def put(self, todo_id):
        args = parser.parse_args()
        print(args)
        todos[todo_id]["description"] = args["description"]
        return todos[todo_id]


api.add_resource(ToDosAll, "/todos")
api.add_resource(ToDos, "/todos/<todo_id>")

if __name__ == "__main__":
    app.run(debug=True)


# Eintrag anlegen:
# curl http://localhost:5000/todos -d "data=Remember the milk" -X PUT
# -> Man bekommt die u.a. die generierte ID zurück

# Alle Einträge auslesen:
# curl http://localhost:5000/todos
# -> Man bekommt alles zurück

# Einzelner Eintrag auslesen:
# curl http://localhost:5000/todo/1
# -> Man bekommt einen Eintrag zurück

# Einzelner Eintrag setzen:
# curl http://localhost:5000/todo/1 -d "data=Buy some apples" -X PUT
# -> Man manipuliert einen Eintrag
