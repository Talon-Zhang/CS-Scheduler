#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 " \
             "(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"


def get_jsessionid():
    print("Start getting Jsessionid: ")
    jsession_url = "https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/" \
                   "ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1&target=G"
    r = requests.get(jsession_url, timeout=300)
    jsessionid = r.cookies.get_dict()["JSESSIONID"]
    print("Got Jsessionid = " + jsessionid)
    return jsessionid


def courseLogin(id, password, jsessionid):
    print("Start logging in Enterprise：")
    log_session = requests.session()
    referer = "https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/" \
              "servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1&target=G"
    cookie = "JSESSIONID="+jsessionid
    log_header = {
        "Referer": referer,
        "Cookie": cookie,
        "User-Agent": user_agent
    }
    log_url = "https://eas.admin.uillinois.edu/eas/servlet/login.do;jsessionid="+jsessionid
    log_data = {
        "inputEnterpriseId": id,
        "password": password,
        "BTN_LOGIN": "Log In"
    }

    r = log_session.post(log_url, data=log_data, headers=log_header, allow_redirects=True, timeout=300)
    ssid = r.cookies.get_dict()["SESSID"]
    print("Got SESSID = " + ssid)
    return ssid


def course_search(subject, num, ssid):
    print("Start searching for course content of " + subject + num+":")
    course_url = 'https://ui2web1.apps.uillinois.edu/BANPROD1/bwskfcls.P_GetCrse'
    course_header = {
        "Referer": "https://ui2web1.apps.uillinois.edu/BANPROD1/bwskfcls.P_GetCrse",
        "Cookie": "SESSID=" + ssid,
        "User-Agent": user_agent
    }
    course_data = "term_in=120188&sel_subj=dummy&sel_subj=" + subject + "&SEL_CRSE=" + num + "&" \
        "SEL_TITLE=&BEGIN_HH=0&BEGIN_MI=0&BEGIN_AP=a&SEL_DAY=dummy&SEL_PTRM=dummy&END_HH=0&END_MI=0&END_AP=a" \
        "&SEL_CAMP=dummy&SEL_SCHD=dummy&SEL_SESS=dummy&SEL_INSTR=dummy&SEL_INSTR=%25&SEL_ATTR=dummy&SEL_ATTR=%25" \
        "&SEL_LEVL=dummy&SEL_LEVL=%25&SEL_INSM=dummy&sel_dunt_code=&sel_dunt_unit=&call_value_in=&rsts=dummy&crn=dummy" \
        "&path=1&SUB_BTN=View+Sections"
    r = requests.post(course_url, data=course_data, headers=course_header, timeout=300)
    # cookies = r.cookies.get_dict()
    # print(cookies)
    # if not cookies:
    #     return cookies
    print("The course html file is collected!")
    return r.text


