
import os


def get_html_theme_path():
    """Return a list of HTML theme paths"""
    theme_path = os.path.abspath(os.path.dirname(__file__))
    return [theme_path]


def setup(app):
    """Setup the theme"""
    theme_path = get_html_theme_path()[0]
    app.add_html_theme("miaowware", os.path.join(theme_path, "miaowware"))
