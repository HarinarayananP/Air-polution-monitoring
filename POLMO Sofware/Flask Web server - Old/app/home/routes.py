# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, request, jsonify, Response, current_app
from flask_login import login_required
from jinja2 import TemplateNotFound
from app.base.models import SensorData, SensorDetails, Settings
from app import db, mqtt
from datetime import datetime, timedelta
import random, json


@blueprint.route('/index')
@login_required
def index():
    # lastid = SensorData.query.order_by(SensorData.id.desc()).first()
    # marginid = int(lastid.id) - 30000
    # count = 0
    # if marginid > 0:
    #     datas = SensorData.query.filter(SensorData.id < marginid)
    #     for item in datas:
    #         db.session.delete(item)
    #         count += 1
    #     db.session.commit()

    sensordata = {}
    sensordetails = SensorDetails.query.all()
    sen_details = []
    for item in sensordetails:
        if SensorData.query.filter_by(sensorname=item.name).count() != 0:
            sen_details.append(item)
            sensordata[item.name] = SensorData.query.filter_by(sensorname=item.name).order_by(
                SensorData.time.desc()).limit(int(current_app.config['TABLE_MAX_VALUE']))
    sensordata['all'] = SensorData.query.order_by(SensorData.time.desc()).limit(
        int(current_app.config['TABLE_MAX_VALUE']))
    now = datetime.now()
    now += timedelta(hours=5, minutes=30)

    # Creating Chart
    chart = {}
    chart_24hour = {}
    for item in sensordetails:
        total = 24
        tw = timedelta(hours=total)
        time = now - tw
        result_count = SensorData.query.filter(SensorData.time > time, SensorData.sensorname == item.name).count()
        if result_count == 0 or result_count is None:
            c_data = {
                item.name: None
            }
            continue
        c_data = {
            item.name: SensorData.query.filter(SensorData.time > time, SensorData.sensorname == item.name).order_by(
                SensorData.time.desc())
        }
        timeframe = 1
        mean = {}
        for data in c_data[item.name]:
            delta = now - data.time
            index = int(((delta.seconds / 3600) + (delta.days * 24)) / timeframe)
            if index in mean:
                mean[index]['val'] = ((mean[index]['val'] * mean[index]['ind']) + round(data.value, 2)) / (
                        mean[index]['ind'] + 1)
                mean[index]['ind'] += 1
            else:
                mean[index] = {'val': round(data.value, 2), 'ind': 1}
            # print(str(index) + ' : Seconds : ' + str(delta.seconds / 3600) + ' Value: ' + str(data.value))
        count = 0
        sorted_mean = {}
        while count < (total / timeframe):
            if count not in mean:
                mean[count] = {'val': 0}
            sorted_mean[count] = mean[count]['val']
            count += 1
        chart[item.name.replace('-', '_')] = sorted_mean

        timeframe = 24
        total = 720
        tw = timedelta(hours=total)
        time = now - tw
        p_data = {
            item.name: SensorData.query.filter(SensorData.time > time, SensorData.sensorname == item.name).order_by(
                SensorData.time.desc())
        }
        mean = {}
        for data in p_data[item.name]:
            delta = now - data.time
            index = int(((delta.seconds / 3600) + (delta.days * 24)) / timeframe)
            if index in mean:
                mean[index]['val'] = ((mean[index]['val'] * mean[index]['ind']) + round(data.value, 2)) / (
                        mean[index]['ind'] + 1)
                mean[index]['ind'] += 1
            else:
                mean[index] = {'val': round(data.value, 2), 'ind': 1}
        count = 0
        sorted_mean = {}
        while count < (total / timeframe):
            if count not in mean:
                mean[count] = {'val': 0}
            sorted_mean[count] = mean[count]['val']
            count += 1

        chart_24hour[item.name.replace('-', '_')] = sorted_mean

    # Calculating AQI
    if 'PM2.5' in chart_24hour:
        ch = chart_24hour['PM2.5']
        chart_aqi = {}
        for average in ch:
            aqi = {}
            x = ch[average]
            if x < 30:
                aqi['val'] = 1.66 * x
                aqi['color'] = '27, 94, 32'
            elif x == 30:
                aqi['val'] = 50
                aqi['color'] = '27, 94, 32'
            elif 30 < x < 60:
                aqi['val'] = 1.689 * (x - 31) + 51
                aqi['color'] = '102, 187, 106'
            elif x == 60:
                aqi['val'] = 100
                aqi['color'] = '102, 187, 106'
            elif 60 < x < 90:
                aqi['val'] = 1.689 * (x - 61) + 101
                aqi['color'] = '255, 235, 59'
            elif x == 90:
                aqi['val'] = 200
                aqi['color'] = '255, 235, 59'
            elif 90 < x < 120:
                aqi['val'] = 3.41 * (x - 91) + 201
                aqi['color'] = '255, 111, 0'
            elif x == 120:
                aqi['val'] = 300
                aqi['color'] = '255, 111, 0'
            else:
                aqi['val'] = 500
                aqi['color'] = '183, 28, 28'
            aqi['val'] = int(aqi['val'])
            chart_aqi[average] = aqi
    else:
        chart_aqi = {
            0: {'val': 0}
        }
    return render_template('index.html', segment='index', sensordetails=sen_details, sensordata=sensordata,
                           chart=chart, chart_24hour=chart_24hour, chart_aqi=chart_aqi, now=now)


@blueprint.route('/populate')
@login_required
def populate():
    i = 0
    sensors = SensorDetails.query.all()
    count = 0
    for sens in sensors:
        while i < 20000:
            i += 1
            row = SensorData()
            row.sensorname = sens.name
            row.time = datetime.now() - timedelta(minutes=(i * 10))
            row.value = random.randint(1, current_app.config['SENSOR_MAX_VALUE'])
            db.session.add(row)
        db.session.commit()
        i = 0

    return "Populated!"


@blueprint.route('/table')
@login_required
def table():
    sensordata = SensorData.query.order_by(SensorData.time.desc()).limit(int(500))
    return render_template('tables.html', sensordata=sensordata)


@blueprint.route('/clear-db')
@login_required
def cleardb():
    lastid = SensorData.query.order_by(SensorData.id.desc()).first()
    marginid = lastid - 30000
    count = 0
    if marginid > 0:
        datas = SensorData.query.filter(SensorData.id < marginid)
        for item in datas:
            db.session.delete(item)
            count += 1
        db.session.commit()
    print()
    return 'Total ' + str(count) + ' is deleted!'


@blueprint.route('/data')
def data():
    pass


@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)
        # Loading Template Variables
        template_variables = {}

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template(template, segment=segment)

    except TemplateNotFound:
        return render_template('page-404.html'), 404

    except:
        return render_template('page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
