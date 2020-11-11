"""
HBDU (Happy-BirthDay-U) is a website for your friends' birthday.
Enter your friend's name then send the link!
"""

from flask import Flask

app = Flask(__name__)


def import_views():
    """This function imports the routes from `views.py`
    """
    import HBDU.views
    print(f"[\033[1;32m+\033[0m]{HBDU.views.__name__} detected")


import_views()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=False)
