#===========================================================
# APP NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Welcome page
#-----------------------------------------------------------
@app.get("/")
def show_welcome():
    return render_template("pages/welcome.jinja")


#-----------------------------------------------------------
# New task form
#-----------------------------------------------------------
@app.get("/task/new")
def show_task_form():
    return render_template("pages/task_form.jinja")


#-----------------------------------------------------------
# Handle the task form
#-----------------------------------------------------------
@app.post("/task/new")
def process_task_form():
    # Get the form data
    species = request.form.get("priority", "unknown").strip()
    name = request.form.get("name", "unknown").strip()
    # Connect to the DB
    with connect_db() as db:

        sql = """
            INSERT INTO tasks (priority, name)
            VALUES (?, ?)
        """

        params = (species, name)

        # Run the query
        db.execute(sql, params)

        flash(f"task {name} added successfully")
        # We're done so back to the list
        return redirect("/tasks")


#-----------------------------------------------------------
# Task deletion - Delete a creature via ID
#-----------------------------------------------------------
@app.get("/creature/<int:id>/delete")
def delete_a_creature(id):
    with connect_db() as db:
        sql = """
            DELETE FROM tasks
            WHERE id=?
        """
        params = (id,)
        db.execute(sql, params)

        # Back to the list
        flash("task deleted", "success")
        return redirect("/tasks")


#-----------------------------------------------------------
# Task list page - Show all the tasks
#-----------------------------------------------------------
@app.get("/tasks")
def show_all_tasks():
    with connect_db() as db:
        sql = """
            SELECT id, name, priority, complete
            FROM tasks
        """
        params = ()
        creatures = db.execute(sql, params).fetchall()

        return render_template("pages/task_list.jinja", tasks=tasks)


#-----------------------------------------------------------
# Help page - Show some help
#-----------------------------------------------------------
@app.get("/help")
def show_help():

    flash("Flash test message")
    flash("Flash test message with a longer bit of text")
    flash("Success test message", "success")
    flash("Error test message", "error")

    return render_template("pages/help.jinja")


#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

