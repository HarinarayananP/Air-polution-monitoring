# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from os import path
from datetime import datetime, timedelta
import json, ssl

db = SQLAlchemy()
login_manager = LoginManager()



def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ('base', 'home'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app):
    @app.before_first_request
    def initialize_database():
        db.create_all()
        from app.base.models import Settings
        row = Settings.query.filter_by(name='SensorCount').first()
        if not row:
            row = Settings()
        row.name = 'SensorCount'
        row.value = 3
        db.session.add(row)
        row = Settings.query.filter_by(name='ChartMax').first()
        if not row:
            row = Settings()
        row.name = 'ChartMax'
        row.value = 10
        db.session.add(row)
        row = Settings.query.filter_by(name='TableMax').first()
        if not row:
            row = Settings()
        row.name = 'TableMax'
        row.value = 10
        populate_sensor_data(app)
        db.session.add(row)
        db.session.commit()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def touch_up(appz):
    from app.base.models import Settings
    appz.config.update(dict(
        TABLE_MAX_VALUE=10,
        CHART_MAX_VALUE=10,
        SENSOR_MAX_VALUE=200,
        SENSOR_WARNING_VALUE=150,
        SENSOR_SAFE_VALUE=100
    ))


def create_app(config):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    touch_up(app)
    return app


def populate_sensor_data(appz):
    # from app.base.models import SensorData, SensorDetails
    # i = 0
    # sensors = SensorDetails.query.all()
    # for sensor in sensors:
    #     while i < 100:
    #         i += 1
    #         row = SensorData()
    #         row.sensorname = 'Sensor-Node-3'
    #         row.time = datetime.now() - timedelta(minutes=i)
    #         row.value = randint(1, appz.config['SENSOR_MAX_VALUE'])
    #         db.session.add(row)
    # db.session.commit()
    pass
