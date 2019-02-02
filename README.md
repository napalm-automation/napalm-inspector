[![Build Status](https://travis-ci.org/napalm-automation/napalm-inspector.svg?branch=develop)](https://travis-ci.org/napalm-automation/napalm-inspector)
[![Coverage Status](https://coveralls.io/repos/github/napalm-automation/napalm-inspector/badge.svg?branch=develop)](https://coveralls.io/github/napalm-automation/napalm-inspector?branch=develop)

NAPALM-Inspector
================

The NAPALM Inspector is a web application aimed to help with troubleshooting the getters in NAPALM. If you have found a bug in one of the getters you can use this tool as an easy way to help the developers figure out what's going on.

Once the application is up and running visit [http://127.0.0.1:5000](http://127.0.0.1:5000) and choose the platform and getter you want to test. You will be asked to provide the information your network devices, i.e. when the application will ask you for the output from a command like `show version` then you just paste the output into the form and move on from there.

Installation
============

```bash
pip install napalm-inspector
export FLASK_APP=napalm_inspector
flask run
```

Running from Docker
===================

```bash
git clone https://github.com/napalm-automation/napalm-inspector
cd napalm-inspector
make docker
make start
```

Press Control+C to end the application when done.

Once you are done you can remove the container

```bash
make stop
```