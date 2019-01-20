import pymysql


def insert_registration(dictionary):
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    # db = pymysql.connect("localhost","csscheduler_root","teamzaran1","csscheduler_course_info" )
    cursor = db.cursor()
    sql = """INSERT INTO Registration(netID, CRN, Notification)
         VALUES ('%s',%d,%d)""" % (dictionary["netID"], dictionary["CRN"], 1)

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


def get_registration(netID):
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    # db = pymysql.connect("localhost","csscheduler_root","teamzaran1","csscheduler_course_info" )
    cursor = db.cursor()
    sql = """ Select * From Registration 
              Where netID= "%s" """ % (netID)

    ret_info = ""
    try:
        cursor.execute(sql)
        ret_info = cursor.fetchall()
    except Exception as e:
        print(e)
        ret_info = "fail"

    if ret_info is None:
        ret_info = "fail"

    db.close()
    return ret_info


def delete_registration(netID, CRN):
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    # db = pymysql.connect("localhost","csscheduler_root","teamzaran1","csscheduler_course_info")
    cursor = db.cursor()
    sql = """DELETE FROM Registration WHERE netID= "%s" AND CRN=%d """ % (netID, CRN)

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


def update_registration(dictionary):
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    # db = pymysql.connect("localhost","csscheduler_root","teamzaran1","csscheduler_course_info" )
    cursor = db.cursor()
    sql = """ Update Registration 
              Set Notification=%d   
              Where netID="%s" AND CRN=%d """ % (dictionary["Notification"],dictionary["netID"], dictionary["CRN"])

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
    
# mydic = {"netID":"ziqiw2", "CRN":61821, "Notification":1}
# mydic1 = {"netID":"ziqiw2", "CRN":61820, "Notification":1}
# mydic2 = {"netID":"jiaweit2", "CRN":61821, "Notification":1}
# insert_registration(mydic)
# insert_registration(mydic1)
# insert_registration(mydic2)
# print(get_registrations("ziqiw2"))
# mydic3 = {"netID":"jiaweit2", "CRN":61821, "Notification":0}
# update_registration(mydic3)
# delete_registration("jiaweit2",61821)
# # mydic = {"netID":"ziqiw2", "FirstName":"ziqi", "LastName":"wang", "Area":"DATA", "Standing":"senior"}
# # update_user(mydic)
    
    
    
    
    