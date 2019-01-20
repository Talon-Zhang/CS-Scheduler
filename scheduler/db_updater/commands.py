create_table =  course_sql = '''
    Create Table Course(
	CRN int,
	Course_num char(20),
	Instructor char(100),
	Title char(50),
	Instructor_rate double,
	Instructor_url text,
	GPA double,
	Seat int,
	Time_slot char(40),
    Section char(40),
    Day char(40),
    Area char(100),
    Standing char(40),
	Primary Key(CRN));
	'''


column_name = "(sel, crn, subj, crse, sec, cmp, cred, title, days, times," \
              "cap, act, rem, wl_cap, wl_act, wl_rem, xl_cap, xl_act, xl_rem," \
              "instructor, dates, location, attribute, created_at)"

value_format = "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'," \
               "'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'," \
               "'%s', '%s', '%s', '%s', '%s')"

command_insert = "INSERT INTO course_info" + column_name + value_format


def generate_search_command(column, value):
    sql = "SELECT * FROM course_onfp WHERE %s = %s" % (column, value)
    return sql


def generate_update_command(column, value, dict):
    set = "SET "
    for k, v in dict.items():
        set = set + "%s = %s, " % (k, v)
    set = set[0:-2]
    where = " WHERE %s = %s" % (column, value)
    sql = "UPDATE course_info " + set + where
    return sql


def set_default(info):
    for i in range(10, 19):
        try:
            if info[i] is None:
                info[i] = 0
        except:
            pass
    return info

