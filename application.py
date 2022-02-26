from crypt import methods
from email.mime import application
from flask import(
    Flask, render_template
)

# Initialize the app
application = Flask(__name__)

# Homepage
@application.route("/", methods= ['GET', 'POST'])
def viz_page():
    """
    Homepage: serve up vizualization page, index.html
    """
    
    return render_template('index.html')


# Run the app
if __name__ == "__main__":
    application.run()