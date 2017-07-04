from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "这是首页"

@app.route("/index")
def hello():
    return "Hello World!"

@app.route("/hello")
def helloworld():
    return "欢迎界面"

@app.route("/user/<username>")
def show_user_profile(username):
    return "User %s" % username

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "post %d" % post_id

@app.route("/projects/")
def projects():
    return "The project page"

@app.route("/about")
def about():
    return "The about page"

if __name__ == "__main__":
    app.run()
