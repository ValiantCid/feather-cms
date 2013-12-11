from flask import Flask

app = Flask(__name__)

import routes_admin, routes_public, interfaces #required to make Flask work