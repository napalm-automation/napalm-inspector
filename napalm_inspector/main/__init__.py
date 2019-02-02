from flask import Blueprint

bp = Blueprint("main", __name__)

from napalm_inspector.main import routes  # noqa
