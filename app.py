"""Runs the Masterblog app and provides the flask routes and functionality for
the Masterblog web application"""
import json
import os

from flask import (abort,
                   Flask,
                   flash,
                   render_template,
                   redirect,
                   request,
                   url_for
                   )
from flask.cli import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.secret_key = SECRET_KEY

def write_json(blog_posts: list[dict]) -> None:
    """Writes the json file as the database for blog articles"""
    if not blog_posts:
        blog_posts = [
            {
                "id": "",
                "author": "N/A",
                "title": "No Blog-Data available",
                "content": "Please start your blog first"
            }
        ]
    blog_data = blog_posts
    content = json.dumps(blog_data, indent=4)
    with open(
            os.path.join(
                "data",
                "blog.json"
            ), "w", encoding="utf-8") as jsonobj:
        jsonobj.write(content)
    return None


def load_json() -> list[dict]:
    """Loads the json file and returns blog posts.
    Returns default placeholder content if the file cannot be opened."""
    try:
        with open(
                os.path.join(
                    "data",
                    "blog.json"
                ), "r", encoding="utf-8") as jsonobj:
            blog_posts = json.load(jsonobj)
            return blog_posts
    except OSError:
        return [
            {
                "id": "",
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


@app.route("/add", methods=["GET", "POST"])
def add():
    """with a get request a form html will be returned for creating a new blog
    post, with the post request the content of the new post form will be send
    and be written into the database. Redirects to index.html afterwards."""
    if request.method == "POST":
        blog_posts = load_json()
        author_name = request.form.get("author", "anonymous").strip()
        post_title = request.form.get("title", "N/A").strip()
        post_content = request.form.get("content", "").strip()

        if not post_content:
            flash("Please enter valid content!", "error")
            return redirect(url_for("add"))

        id_check = str(blog_posts[0].get("id", "")).strip()

        if id_check != "":
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

        flash("New post successfully created!", "success")
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/delete/<post_id>", methods=["POST"])
def delete_post(post_id):
    """Deletes a post via POST request and redirects to home after deletion."""
    if post_id.isdigit():
        post_id = int(post_id)
    else:
        abort(404)

    blog_posts = load_json()
    new_blog_posts = []
    deleted = False

    for post in blog_posts:
        blog_post_id = post.get("id", "")
        if blog_post_id == "":
            abort(404)
        elif blog_post_id == post_id:
            deleted = True
            flash("Post successfully deleted", "success")
        else:
            new_blog_posts.append(post)
    if not deleted:
        abort(404)
    write_json(new_blog_posts)
    return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(error):
    """Render custom 404 page."""
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
