import os

from flask import Flask, render_template, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("homepage.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.route("/log_in")
def log_in():
    return render_template("log_in.html")


@app.route("/search_result")
def search_result():
    return render_template("search_result.html")
