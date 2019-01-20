import pymysql


def insert_course(dictionary):
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    # db = pymysql.connect("localhost", "csscheduler_root", "teamzaran1", "csscheduler_course_info")
    cursor = db.cursor()
    sql = """INSERT INTO Course
         VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
    dictionary["CRN"], dictionary["Course_num"], dictionary["Instructor"], dictionary["Title"],
    dictionary["Instructor_rate"], dictionary["Instructor_url"], dictionary["GPA"], dictionary["Seat"],
    dictionary["Time_slot"], dictionary["Section"], dictionary["Day"], dictionary["Area"], dictionary["Standing"])

    ret_info = ""
    try:
        cursor.execute(sql)
        db.commit()
        ret_info = "success"
    except Exception as e:
        print(e)
        db.rollback()
        ret_info = "fail"

    db.close()
    return ret_info


def get_course(dictionary):
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    # db = pymysql.connect("localhost", "csscheduler_root", "teamzaran1", "csscheduler_course_info")
    cursor = db.cursor()
    sql = " Select * From Course Where "
    for key in dictionary:
        sql += "%s='%s' AND " % (key, dictionary[key])
    sql = sql[:-4]

    try:
        cursor.execute(sql)
        message = cursor.fetchall()
    except Exception as e:
        print(e)
        db.close()
        return "fail"

    if message is None:
        db.close()
        return "fail"

    ret_info = []
    for course in message:
        ret = {}
        ret["crn"] = course[0]
        ret["course_number"] = course[1]
        ret["instructor"] = course[2]
        ret["title"] = course[3]
        ret["instructor_rate"] = course[4]
        ret["instructor_url"] = course[5]
        ret["gpa"] = course[6]
        ret["seat"] = course[7]
        ret["time_slot"] = course[8]
        ret["section"] = course[9]
        ret["day"] = course[10]
        ret["area"] = course[11]
        ret["standing"] = course[12]
        ret_info.append(ret)
    db.close()
    return ret_info

def get_recommend(area,standing):
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    cursor = db.cursor()
    sql1 = """ Select *  
               From Course   
               Where Area ='%s' """ % (area)
    sql2 = """ Select *  
               From Course   
               Where Standing ='%s' """ % (standing)
    try:
        cursor.execute(sql1)
        message = cursor.fetchall()
        if message==None:
            return "fail"
        if len(message)>10:
            message = message[:10]
        ret_info = [message]
    except Exception as e:
        print(e)
        db.rollback()
        return "fail"

    cursor = db.cursor()
    try:
        cursor.execute(sql2)
        message = cursor.fetchall()
        if message==None:
            return "fail"
        if len(message)>10:
            message = message[:10]
        ret_info += [message]
    except Exception as e:
        print(e)
        db.rollback()
        return "fail"

    return ret_info

def update_course(dictionary):
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    # db = pymysql.connect("localhost", "csscheduler_root", "teamzaran1", "csscheduler_course_info")
    cursor = db.cursor()
    sql = """ Update Course 
              Set Seat='%s'   
              Where CRN='%s' """ % (
    dictionary["Seat"], dictionary["CRN"])

    ret_info = ""
    try:
        cursor.execute(sql)
        db.commit()
        ret_info = "success"
    except Exception as e:
        print(e)
        db.rollback()
        ret_info = "fail"

    db.close()
    return ret_info


# mydic = {"CRN": 61820, "Course_num": "cs411", "Instructor": "abdu", "Title": "database", "Instructor_rate": 2.1,
#          "Instructor_url": "https://web.illinois.edu:2083/cpsess6392010926/frontend/paper_lantern/filemanager/editit.html?file=course.py&fileop=&dir=%2Fhome%2Fcsscheduler&dirop=&charset=&file_charset=_DETECT_&baseurl=&basedir=&edit=1",
#          "GPA": 3.5, "Seat": 12, "Time_slot": "11:00-12:00", "Section": "ADL", "Day": "MT", "Area": "Data",
#          "Standing": "junior"}
# insert_course(mydic)
# mydic1 = {"CRN": 61820, "Seat": 11}
# # update_course(mydic1)
# print(get_courses(mydic1))


