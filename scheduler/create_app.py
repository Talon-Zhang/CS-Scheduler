#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_apscheduler import APScheduler
from flask_cors import *
from scheduler.views import cs_scheduler
# from scheduler.email.send_email import *

scheduler = APScheduler()


class Config(object):
    JOBS = [
        {
            'id': 'updater',
            'func': 'update_db: refresh_db',
            'trigger': 'interval',
            'minutes': 5
        }
    ]
    SCHEDULER_API_ENABLED = True


def create_app():
    app = Flask(__name__)
    app.config['debug'] = True
    app.config.from_object(Config())
    CORS(app, supports_credentials=True)

    scheduler.init_app(app)
    scheduler.start()
    app.app_context().push()

    app.register_blueprint(cs_scheduler)

    return app


application = create_app()



















