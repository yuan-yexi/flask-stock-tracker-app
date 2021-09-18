from flask import Flask, render_template

from stock_app.blueprints.home import home
from stock_app.blueprints.stock import stock
from stock_app.config import configurations

def create_app(enviroment_name='dev'):
    app = Flask(__name__)

    app.config.from_object(configurations[enviroment_name])

    @app.errorhandler(500)
    def handle_error_500(exception):
        return render_template("500.html"), 500

    app.register_blueprint(home)
    app.register_blueprint(stock, url_prefix='/stock')

    return app
