"""Runs the Masterblog app and provides the flask routes and functionality for
the Masterblog web application"""
import json
import os

from flask import Flask, flash, render_template, redirect, request, url_for
from flask.cli import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.secret_key = SECRET_KEY

def write_json(blog_posts: list[dict] = "") -> None:
    """Writes the json file as the database for blog articles"""
    if not blog_posts:
        blog_posts = [
            {"id": 1, "author": "John Doe", "title": "First Post",
             "content": "This is my first post."},
            {"id": 2, "author": "Jane Doe", "title": "Second Post",
             "content": "This is another post."}
        ]
    blog_data = blog_posts
    content = json.dumps(blog_data, indent=4)
    with open("data/blog.json", "w", encoding="utf-8") as jsonobj:
        jsonobj.write(content)
    return None


def load_json() -> list[dict] | str:
    """Try to load a json-file and returns content as json or None if fails
    to open the file"""
    try:
        with open("data/blog.json", "r", encoding="utf-8") as jsonobj:
            blog_posts = json.load(jsonobj)
            return blog_posts
    except OSError:
        return [
            {
                "author": "N/A",
                "title": "No Blog-Data available",
                "content": "Please start your blog first"
            }
        ]


@app.route("/", methods=["GET"])
def home():
    """With a get request for this route, the function will return a rendered
    index.html containing the blog content from the blog database"""
    blog_posts = load_json()
    return render_template("index.html", blog_posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """with a get request a form html will be returned for creating a new blog
    post, with the post request the content of the new post form will be send
    and be written into the database. Redirects to index.html afterwards."""
    if request.method == 'POST':
        blog_posts = load_json()
        author_name = request.form.get("author", "anonymus")
        post_title = request.form.get("title", "N/A")
        post_content = request.form.get("content", None)

        if post_content is None:
            flash("Please enter valid content!", "error")
            return redirect(url_for("home"))

        id_check = blog_posts[-1].get(id, "")

        if id_check == "":
            new_id = len(blog_posts) + 1

        else:
            new_id = 1
            blog_posts = []

        new_post = {
            "id": new_id,
            "author": author_name,
            "title": post_title,
            "content": post_content
        }
        blog_posts.append(new_post)
        write_json(blog_posts)

        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
