# To run the application we need to perform two tasks in the CLI
#   1. Declare the FLASK_APP, which is the file in which the the Flask application is created using: export FLASK_APP=main.py
#   2. To run the application using: flask run


# From CLI we can go to the Flask shell to check multiple properties of the application using: flask shell
#   To check the mapped routes we can use: app.url_map
#   To check static directory of the application we can use: app.static_folder
#   To check the template directory we can use: app.template_folder



from flask import Flask
from config import DevConfig

app = Flask(__name__)

# The DevConfig class is imported from 
app.config.from_object(DevConfig)

# Creating a basic GET route
@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()