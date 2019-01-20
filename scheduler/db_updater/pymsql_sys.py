import pymysql
from commands import *
from scheduler.sql_command.course import *


def recreate_db():
    print("Start creating new database with name 'course_info':")
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS course")
    sql = create_table
    cursor.execute(sql)
    db.close()
    print("New database successfully created!")


def insert_data(html_list):
    print("Start filling in the database:")
    for info in html_list:
        info = set_default(info)
        try:
            dict = {"CRN": int(info[1]), "Course_num": info[3], "Instructor": info[19],
                     "Title": info[7], "Instructor_rate": 0, "Instructor_url": "",
                     "GPA": 0, "Seat": int(info[18]), "Time_slot": info[9], "Section": info[4],
                     "Day": info[8], "Area": "", "Standing": ""}
            print(insert_course(dict))
        except Exception as e:
            print(e)

    print("Database filling finsihed")




def update_data(html_list):
    print("Start updating database:")
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "test")
    cursor = db.cursor()
    count = 0
    for info in html_list:
        info = set_default(info)
        dict = {"cap": info[10], "act": info[11], "rem": info[12],
                "wl_cap": info[13], "wl_act": info[14], "wl_rem": info[15],
                "xl_cap": info[16], "xl_act": info[17], "xl_rem": info[18],
                }
        try:
            sql = generate_update_command("crn", info[1], dict)
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            count = count + 1
    db.close()
    print("##################################")
    print("Database update finsihed with " + str(count) + " exceptions.")
    print("Time: " + str(dt.now()))
    print("##################################")