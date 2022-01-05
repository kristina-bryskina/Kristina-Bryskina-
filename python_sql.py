import sqlite3

def init_db(cursor):
	
	cursor.executescript('''
		DROP TABLE if exists product;
		DROP TABLE if exists users;
		DROP TABLE if exists history;

		CREATE TABLE  "product" (
		"id"	INTEGER,
		"name"	TEXT,
		"amount"	INTEGER,
		"price"	INTEGER,
		"info" TEXT,
		"discount" INTEGER,
		"pic_url" TEXT,
		PRIMARY KEY("id" AUTOINCREMENT)
	);

		CREATE TABLE  "users"  (
		"id"	INTEGER,
		"login" TEXT,
		"password"	TEXT,
		"registration_date"	TEXT,
		"birth_date" TEXT,
		PRIMARY KEY("id" AUTOINCREMENT)
	);

		CREATE TABLE  "history"  (
		"id"	INTEGER,
		"user_id"	INTEGER,
		"product_id"	INTEGER,
		"amount"	INTEGER,
		"discount"	INTEGER,
		"date"	TEXT,
		FOREIGN KEY("product_id") REFERENCES "product"("id"),
		PRIMARY KEY("id" AUTOINCREMENT),
		FOREIGN KEY("user_id") REFERENCES "users"("id")
	);
		INSERT INTO "users" ('id','login','password','registration_date', 'birth_date') VALUES
		(1,'aaa','a1a','20.11.2021','23.12.2008'),
		(2,'bbb','b1b','01.01.2022','25.09.2006'),
		(3,'ccc','c1c','20.09.2000','16.10.2000');


		INSERT INTO "product" ('id','name','amount','price','info','discount','pic_url') VALUES
		(1,'мяч',10,50,'...',20,'aaaa'),
		(2,'футболка',50,100,'...',30,'bbbb'),
		(3,'сетка',20,500,'...',10,'cccc');


		INSERT INTO "history" ('id','user_id','product_id','amount','discount','date') VALUES
		(1,1,2,1,0,'21.11.2020'),
		(2,1,3,10,0,'11.05.2006'),
		(3,2,1,100,0,'17.10.2013'),
		(4,3,2,50,0,'31.01.2019');

	''')


def task1(cursor):
	cursor.execute('SELECT registration_date FROM users;')    
	mas = cursor.fetchall()
	for i in mas:
		i = i[0]
		s = i[6:]+'-'+i[3:5]+'-'+i[:2]

		cursor.execute(f'''update "users"
		SET registration_date = "{s}"
		where registration_date = "{i}";
	''')

def task11(cursor):
	cursor.execute('SELECT birth_date FROM users;')    
	mas = cursor.fetchall()
	for i in mas:
		i = i[0]
		s = i[6:]+'-'+i[3:5]+'-'+i[:2]

		cursor.execute(f'''update "users"
		SET birth_date = "{s}"
		where birth_date = "{i}";
	''')


def task2(cursor):
	cursor.execute('SELECT login FROM users ORDER BY registration_date DESC limit 1')
	mas = cursor.fetchall()
	return (mas[0][0])


def task3(cursor):
	res = []
	cursor.execute('SELECT birth_date FROM users')
	mas = cursor.fetchall()
	for i in mas:
		i = i[0]
		s = i[:4]
		res.append(int(s))
	res = set(res)
	return res

def task4(cursor):
	cursor.execute('SELECT amount FROM history')
	mas = cursor.fetchall()
	res = 0
	for ch in mas:
		ch = ch[0]
		res+=int(ch)
	return (res)


def task5(cursor):
	cursor.execute('''
	SELECT 
	AVG( CAST(strftime('%Y', DATETIME("now")) as integer) -
	CAST(strftime('%Y', DATETIME(birth_date)) as integer))
	 FROM users
	 WHERE DATETIME(registration_date, '+2 months')>DATETIME("now")
	 ''')
	
	mas = cursor.fetchall()
	return mas[0]


	


name = 'hhmm.db'

con = sqlite3.connect(name)

cursor = con.cursor()


print("Логин пользователя, зарегестрировавшегося последним:", task2(cursor))

print("Уникальные года рождения пользователей:",*task3(cursor))

print("Общее количество купленных товаров:",task4(cursor))

print("Средний возраст зарегистрировавшихся покупателей, чья дата регистрации не позже двух месяцев:", *task5(cursor))

con.commit()
con.close()


