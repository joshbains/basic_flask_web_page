from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import random
from random import choice, sample
import logging

app = Flask(__name__)
app.config["SECRET_KEY"] = "chickens"
debug = DebugToolbarExtension(app)

# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "You made a post request"

# @app.route('/')
# def home_page():
#     """Shows home page"""
#     return render_template("hello.html")


@app.route('/form')
def show_form():
    return render_template("form.html")


@app.route('/form_2')
def show_form_2():
    return render_template("form_2.html")


@app.route('/greet_2')
def get_greeting_2():
    username = request.args["username"]
    wants_compliments = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3)
    return render_template("greet_2.html", username=username, nice_things=nice_things, wants_compliments=wants_compliments)


COMPLIMENTS = ['Cool', 'Awesome', 'Gnarly', 'Rad']


@app.route('/spell/<word>')
def spell_word(word):
    return render_template("spell.html", word=word)


@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=nice_thing)


@app.route('/hello')
def say_hello():
    """Shows Hello page"""
    return render_template("hello.html")


@app.route("/lucky")
def show_lucky_num():
    """Example of a simple dynamic template"""
    num = random.randint(1, 10)

    return render_template("lucky.html", lucky_num=num, msg="Hello this is a message!")


@app.route('/add-comment')
def add_comment_form():
    return """
        <h1>Add comment</h1>
        <form method="POST">
            <input type='text' placeholder='comment', name='comment'/>
            <input type='text' placeholder='username', name='username'/>

            <button>Submit</button>
        </form>
    """


@app.route('/add-comment', methods=['POST'])
def save_comment():
    comment = request.form["comment"]
    username = request.form["username"]
    app.logger.info(request.form)
    return f"""
        <h1>Saved your comment</h1>
        <ul>
            <li>Username: {username}</li>
            <li>Comment: {comment}</li>
        </ul>
    """


@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>You are currently browsing the {subreddit} subreddit</h1>"


@app.route("/r/<subreddit>/comments/<post_id>")
def show_comments(subreddit, post_id):
    return f"<h1>Viewing comments for post: {post_id} on the subreddit: {subreddit}</h1>"


POSTS = {
    1: "I like chicken tenders",
    2: "I hate mayo!",
    3: "Double rainbow all the way",
    4: "YOLO OMG (kill me!)"
}


@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, "Post not Found")
    return f"<p>{post}</p>"
