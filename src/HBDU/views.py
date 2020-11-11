"""
The routes of the project. (mt`V` pattern)
"""
from flask import (
    render_template,
    request,
    redirect,
    url_for,
)
from HBDU import app


THEMES = ["Birthday_1", "Birthday_2", "Birthday_3", "Birthday_4"]


@app.route("/")
def home():
    """The main route of the project.

    :return: render_template: `templates/Home/index.html`
    """
    return render_template("Home/index.html", themes=THEMES)


@app.route("/v1/say_happy", methods=['POST'])
def say_happy():
    """The home form sends a POST request to this route.

    :methods: POST
    :return: redirect: `home()` for correct detail
                and `/v1/themes/THEME/NAME/AUTHOR` for wrong detail.
    """
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
    """Renders themes with the given name and author.

    :param theme: The selected theme(An element of `THEMES`).
    :param name: The friend's name.
    :param author: The person who want to send the link.

    :return: redirects to `home()` (if (`theme` not in `THEMES`) == True)
                and renders `{theme}/index.html` for correct theme name.
    """
    if theme not in THEMES:
        return redirect(url_for("home"))

    return render_template(
        f"{theme}/index.html",
        name=name,
        author=author
    )


@app.errorhandler(404)
def error_404(err):
    """Not found error.

    :return: render_template, 404: `Error/404.html`.
    """
    return render_template("Error/404.html"), 404
