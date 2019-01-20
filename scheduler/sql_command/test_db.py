import pymysql


def create_test_db():
    print('Creating Data Base...')
    db = pymysql.connect("127.0.0.1", "sflog", "sf123456", "cs_scheduler")
    cursor = db.cursor()

    course_sql = '''
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

    user_sql = '''
    Create Table User1(
	netID char(40),
	FirstName char(40),
	LastName char(40),
	Area char(40),
	Standing char(40),
	Email char(100),
	Primary Key(netID));
    '''

    registration_sql = '''
    Create Table Registration(
	netID char(20),
	CRN int,
	Notification int,
	Primary Key(netID,CRN));
    '''

    # cursor.execute(course_sql)
    cursor.execute(user_sql)
    # cursor.execute(registration_sql)
    db.close()

create_test_db()