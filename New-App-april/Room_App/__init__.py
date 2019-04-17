"""
The flask.
"""

from flask import Flask, render_template, url_for, views

app = Flask(__name__)


from .views import *
from .models import *