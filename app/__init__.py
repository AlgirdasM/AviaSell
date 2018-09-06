#!/usr/bin/env python3

from flask import Flask
webapp = Flask(__name__)

webapp.config.from_pyfile('config/webapp.cfg', silent=False)

import app.views
import app.models
import app.api