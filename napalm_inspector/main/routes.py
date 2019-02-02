from napalm_inspector.exceptions import MissingData
from napalm_inspector.main import bp
from napalm_inspector.drivers import test_drivers
from flask import render_template, request
import json
import traceback


@bp.route("/")
def index():
    """Main page."""
    return render_template("index.html")


@bp.route("/test-getters/")
def getters():
    drivers = list(test_drivers.keys())
    return render_template("test_getter_platforms.html", drivers=drivers)


@bp.route("/test-getters/<platform>/")
def platform(platform):
    """Main page."""

    driver = test_drivers[platform]

    napalm_getters = [g for g in dir(driver) if g.startswith("get_")]
    return render_template("platform.html", platform=platform, getters=napalm_getters)


@bp.route("/test-getters/<platform>/<getter>", methods=["GET", "POST"])
def getter(platform, getter):
    """Getter test."""
    tb = None
    exception = None
    data = None
    missing_command = None
    missing_command_id = None
    input_data = {}
    form_data = []
    if request.method == "POST":
        for entry in request.form:
            input_data[entry] = request.form[entry].replace("\r\n", "\n")
            command = {}
            command["id"] = entry
            command["data"] = request.form[entry]
            form_data.append(command)

    driver = test_drivers[platform]
    dev = driver(input_data)

    func = getattr(dev, getter)
    try:
        data = func()
        data = json.dumps(data, indent=4, sort_keys=True)

    except MissingData as e:
        missing_command = e.request
        missing_command_id = e.request_id
    except Exception as e:
        tb = traceback.format_exc()
        exception = e

    return render_template(
        "getter.html",
        getter=getter,
        data=data,
        traceback=tb,
        exception=exception,
        form_data=form_data,
        missing_command=missing_command,
        missing_command_id=missing_command_id,
        platform=platform,
    )
