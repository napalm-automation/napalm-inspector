from flask import Blueprint

bp = Blueprint("errors", __name__)

from napalm_inspector.errors import handlers  # noqa
