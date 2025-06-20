from instaloader import Instaloader, Post
import random

L = Instaloader()

L.login("username", "password")

shortcode = "short_code_of_post"
post = Post.from_shortcode(L.context, shortcode)

comments = []
for comment in post.get_comments():
    comments.append({
        "user": comment.owner.username,
        "text": comment.text
    })

if comments:
    winner = random.choice(comments)
    print(f"\n🎉 Randomly selected comment:\n@{winner['user']}: {winner['text']}")
else:
    print("No comments found.")
