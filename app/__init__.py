#!/usr/bin/env python3

from flask import Flask
webapp = Flask(__name__)

webapp.secret_key = 'cd48e1c22de0961d3d1afb14f8a66e006cfb1cfbf3f0c0f3'

import app.views
import app.models