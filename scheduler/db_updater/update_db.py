#!/usr/bin/env python
# -*- coding:utf-8 -*-
from extract_content import *
from request_info import *
from pymsql_sys import *


# set up search content
subj = "CS"
num = ""

# user info
netid = ""
password = ""


def start_crawler():
    print("Starting Crawler")
    ssid = get_new_ssid()
    html_list = search_course_info(subj, num, ssid)

    recreate_db()
    insert_data(html_list)


def refresh_db():
    print("The automatic database update has started!")

    file_object = open('C:/course_rusher/code/rusher/files/ssid_storage.txt')
    ssid = file_object.read()
    html_list = search_course_info(subj, num, ssid)
    if not html_list:
        print("Trying to get a new ssid:")
        ssid = get_new_ssid()
        html_list = search_course_info(subj, num, ssid)
    recreate_db()
    insert_data(html_list)

    # print("Automatic registration start:")
    # register_courses(register_crns)


def get_new_ssid():
    jsessionid = get_jsessionid()
    ssid = courseLogin(netid, password, jsessionid)
    file_object = open('C:/cs_scheduler/code/scheduler/files/ssid_storage.txt', 'w')
    file_object.write(ssid)
    print("The ssid has been stored in the assigned file.")
    return ssid


def search_course_info(subj, num, ssid):
    html = course_search(subj, num, ssid)
    # if not html:
    #     return html
    html_list = extract_content(html)
    return html_list


start_crawler()