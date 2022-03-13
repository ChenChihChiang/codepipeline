from flask import Flask, render_template, request
import smtplib
import requests

# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
posts = requests.get("https://api.npoint.io/04c8311f849463a4a3ae").json()
OWN_EMAIL = "postmaster@sandbox7f728738343048469ee0beaa9ec10d07.mailgun.org"
OWN_PASSWORD = "2f9x6wkvrno7"

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.mailgun.org") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail("chihchinag@gmail.com", "chihchinag@gmail.com", email_message)


if __name__ == "__main__":
    #if you want your web server to run in repl.it, use the next line:
    # app.run(host='0.0.0.0', port=8080)

    #If you want your web server to run locally on your computer, use this:
    app.run(host='0.0.0.0', debug=True, port=8080)
