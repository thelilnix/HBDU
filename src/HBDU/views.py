from HBDU import app
from flask import (
    render_template,
    request,
    redirect,
    url_for,
)


THEMES = ["Birthday_1", "Birthday_2", "Birthday_3", "Birthday_4"]


@app.route("/")
def home():
    return render_template("Home/index.html")


@app.route("/v1/say_happy", methods=['POST'])
def say_happy():
    if (request.form.get("name", '') == ''
        or request.form.get("author", '') == ''
        or request.form.get("template", '') == ''
            or request.form["theme"] not in THEMES):
        # Required parameters passed and `theme` passed correct
        return redirect(url_for("home"))

    return redirect(f"/v1/themes/{request.form['theme']}")
