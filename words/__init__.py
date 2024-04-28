from flask import Flask

app = Flask(__name__)

# Import routes at the bottom to avoid circular imports
from words import routes
