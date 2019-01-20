#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import pymysql

my_sender = ''  # 发件人邮箱账号
my_pass = ''  # 发件人邮箱密码


def mail():
    print("sending email")
    fail = 0

    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    # db = pymysql.connect("localhost","csscheduler_root","teamzaran1","csscheduler_course_info" )
    cursor = db.cursor()
    sql = """ Select * From User1"""

    try:
        cursor.execute(sql)
        user_info = cursor.fetchall()
        db.close()
    except Exception as e:
        print(e)
        db.close()

    for info in user_info:
        print(info[5])
        my_user = info[5]

        try:
            msg = MIMEText('Please check your courses for registration', 'plain', 'utf-8')
            msg['From'] = formataddr(["CS_Scheduler", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["User", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "Course Notification"  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            fail += 1
    return fail


ret = mail()
if not ret:
    print("邮件发送成功")
else:
    print("邮件发送失败: " + str(ret))