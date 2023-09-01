from flask import Flask, render_template
import requests
from post import Post

blog_url = f"https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()
print(all_posts)
post_list = []
for blog_post in all_posts:
    post_id = blog_post["id"]
    title = blog_post["title"]
    subtitle = blog_post["subtitle"]
    body = blog_post["body"]
    post = Post(post_id,title,subtitle,body)
    post_list.append(post)
print(post_list[1].title)

app = Flask(__name__)


@app.route("/")
def get_blog():
    return render_template("index.html", posts=post_list)


@app.route("/post/<int:id>")
def post(id):
    return render_template("post.html", post=post_list[id])


if __name__ == "__main__":
    app.run(debug=True)
