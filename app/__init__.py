#!/usr/bin/env python3

from flask import Flask
webapp = Flask(__name__)


import app.views
import app.models