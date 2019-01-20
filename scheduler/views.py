#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import request, jsonify
from scheduler.sql_command.user1 import *
from scheduler.sql_command.registration import *
from scheduler.sql_command.course import *

cs_scheduler = Blueprint('cs_scheduler', __name__)


@cs_scheduler.route("/", methods=['POST', 'GET'])
def welcome():
    return "Welcome to CS_Scheduler!"


@cs_scheduler.route('/get_user', methods=['POST', 'GET'])
def view_get_user():
    netid = request.form.get('netid')
    if not netid:
        return "error input"

    message = get_user(netid)
    if message == "fail":
        return jsonify(message)

    ret = {}
    ret["netid"] = message[0]
    ret["firstname"] = message[1]
    ret["lastname"] = message[2]
    ret["area"] = message[3]
    ret["standing"] = message[4]

    message = get_registration(netid)
    if message == "fail":
        ret["courses"] = []

    course_list = []
    for course in message:
        crn = course[1]
        dict = {"CRN": int(crn)}
        course_info = get_course(dict)[0]
        course_info["notification"] = course[2]
        course_list.append(course_info)
    ret["courses"] = course_list

    return jsonify(ret)


@cs_scheduler.route('/insert_user', methods=['POST', 'GET'])
def view_insert_user():
    netid = request.form.get('netid')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    area = request.form.get('area')
    standing = request.form.get('standing')
    if (not netid) or (not firstname) or (not lastname) or (not area) or (not standing):
        return "error input"

    dict = {}
    dict["netID"] = netid
    dict["FirstName"] = firstname
    dict["LastName"] = lastname
    dict["Area"] = area
    dict["Standing"] = standing
    message = insert_user(dict)

    return jsonify(message)


@cs_scheduler.route('/update_user', methods=['POST', 'GET'])
def view_update_user():
    netid = request.form.get('netid')
    area = request.form.get('area')
    standing = request.form.get('standing')
    if (not netid) or (not area) or (not standing):
        return "error input"

    dict = {}
    dict["Area"] = area
    dict["Standing"] = standing
    dict["netID"] = netid
    message = update_user(dict)
    return jsonify(message)


@cs_scheduler.route('/get_registration', methods=['POST', 'GET'])
def view_get_registration():
    netid = request.form.get('netid')
    if not netid:
        return "error input"

    message = get_registration(netid)
    if message == "fail":
        return jsonify(message)

    ret = []
    for course in message:
        crn = course[1]
        dict = {"CRN": int(crn)}
        course_info = get_course(dict)[0]
        course_info["notification"] = course[2]
        ret.append(course_info)
    return jsonify(ret)


@cs_scheduler.route('/insert_registration', methods=['POST', 'GET'])
def view_insert_registration():
    netid = request.form.get('netid')
    crn = request.form.get('crn')
    if (not netid) or (not crn):
        return "error input"

    dict = {}
    dict["CRN"] = int(crn)
    dict["netID"] = netid
    message = insert_registration(dict)
    return jsonify(message)


@cs_scheduler.route('/delete_registration', methods=['POST', 'GET'])
def view_delete_registration():
    netid = request.form.get('netid')
    crn = request.form.get('crn')
    if (not netid) or (not crn):
        return "error input"

    message = delete_registration(netid, int(crn))
    return jsonify(message)


@cs_scheduler.route('/update_registration', methods=['POST', 'GET'])
def view_update_registration():
    netid = request.form.get('netid')
    crn = request.form.get('crn')
    notification = request.form.get('notification')
    if (not netid) or (not crn) or (not notification):
        return "error input"

    dict = {}
    dict["netID"] = netid
    dict["CRN"] = int(crn)
    dict["Notification"] = int(notification)
    message = update_registration(dict)
    return jsonify(message)


@cs_scheduler.route('/get_course', methods=['POST', 'GET'])
def view_get_course():
    crn = request.form.get('crn')
    if not crn:
        return "error input"

    dict = {"CRN": int(crn)}
    message = get_course(dict)
    if message == "fail":
        return jsonify(message)

    if message == []:
        return jsonify("fail")

    return jsonify(message[0])


@cs_scheduler.route('/get_recommend', methods=['POST', 'GET'])
def view_get_recommend():
    area = request.form.get('area')
    standing = request.form.get('standing')
    if not area or not standing:
        return "error input"

    message = get_recommend(area,standing)
    if message == "fail":
        return jsonify(message)

    return jsonify(message)


