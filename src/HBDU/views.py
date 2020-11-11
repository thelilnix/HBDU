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
    return render_template("Home/index.html", themes=THEMES)


@app.route("/v1/say_happy", methods=['POST'])
def say_happy():
    if (request.form.get("name", '') == ''
        or request.form.get("author", '') == ''
        or request.form.get("theme", '') == ''
            or request.form["theme"] not in THEMES):
        # Required parameters passed and `theme` passed correct
        return redirect(url_for("home"))

    theme = request.form['theme']
    name = request.form['name']
    author = request.form['author']

    return redirect(
        f"/v1/themes/{theme}/{name}/{author}"
    )


# Handling themes

@app.route("/v1/themes/<theme>/<name>/<author>")
def handle_theme(theme, name, author):
    if theme not in THEMES:
        return redirect(url_for("home"))

    return render_template(
        f"{theme}/index.html",
        name=name,
        author=author
    )


@app.errorhandler(404)
def error_404(err):
    return render_template("Error/404.html"), 404
