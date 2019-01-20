import pymysql


def insert_user(dictionary):
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    # db = pymysql.connect("localhost","csscheduler_root","teamzaran1","csscheduler_course_info" )
    cursor = db.cursor()
    sql = """INSERT INTO User1(netID,FirstName,LastName,Area,Standing)
         VALUES ('%s','%s','%s','%s','%s')""" % (dictionary["netID"], dictionary["FirstName"],dictionary["LastName"],dictionary["Area"],dictionary["Standing"])

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


def get_user(netID):
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    # db = pymysql.connect("localhost","csscheduler_root","teamzaran1","csscheduler_course_info" )
    cursor = db.cursor()
    sql = """ Select * From User1 
              Where netID= "%s" """ % (netID)

    ret_info = ""
    try:
        cursor.execute(sql)
        ret_info = cursor.fetchone()
    except Exception as e:
        print(e)
        ret_info = "fail"

    if ret_info is None:
        ret_info = "fail"
    db.close()
    return ret_info


def update_user(dictionary):
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    # db = pymysql.connect("localhost","csscheduler_root","teamzaran1","csscheduler_course_info" )
    cursor = db.cursor()
    sql = """ Update User1 
              Set Area="%s", Standing="%s" 
              Where netID = "%s" """ % (dictionary["Area"],dictionary["Standing"], dictionary["netID"])

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
    
    
# mydic = {"netID":"ziqiw2", "FirstName":"ziqi", "LastName":"wang", "Area":"AI", "Standing":"junior"}
# print(insert_user(mydic))
# print(get_user("ziqiw2"))
# mydic = {"netID":"ziqiw2", "FirstName":"ziqi", "LastName":"wang", "Area":"DATA", "Standing":"senior"}
# update_user(mydic)
