from app import app
from flask import render_template, request
from flask_restful import Resource, Api
from app.database import Database

api = Api(app)


@app.route("/")
def index():
    db = Database()
    # db.init_db()
    testbeds = db.get_list()
    return render_template("index.html", testbeds=testbeds)


@app.route("/about")
def about():
    return render_template("about.html")


class TodoSimple(Resource):

    def get(self):
        return None

    def put(self):
        agent_data = request.json
        print(agent_data)
        return agent_data


api.add_resource(TodoSimple, "/client/")
