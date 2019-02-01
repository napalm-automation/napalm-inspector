from flask import Flask


def create_app():
    app = Flask(__name__)

    from napalm_inspector.errors import bp as errors_bp

    app.register_blueprint(errors_bp)

    from napalm_inspector.main import bp as main_bp

    app.register_blueprint(main_bp)

    return app
