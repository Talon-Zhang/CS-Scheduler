#!/usr/bin/env python
# coding:utf-8

from scheduler.create_app import application
# from scheduler.db_updater.update_db import start_program, refresh_db

application.run(host='0.0.0.0', port=7777)




