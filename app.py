from flask import Flask
from Routes.AllRoutes import routes

app = Flask(__name__)
app.register_blueprint(routes)


# Home route
# @app.route("/")
# def home():
#     return "Home Screen"

# # About route
# @app.route("/about")
# def about():
    # return "About Screen"

if __name__ == "__main__":
    app.run(debug=True)
