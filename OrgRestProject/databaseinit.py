import sqlite3
from pathlib import Path

con = sqlite3.connect("Project.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ADULT_TRAIN (RECORD_ID int NOT NULL PRIMARY KEY,AGE int,WORKCLASS TEXT,FNLWGT int,EDUCATION TEXT,EDUCATION_NUM int,MARITAL_STATUS TEXT,OCCUPATION TEXT,RELATIONSHIP TEXT,RACE TEXT,SEX TEXT,CAPITAL_GAIN int,CAPITAL_LOSS int,HOURS_PER_WEEK int,COUNTRY TEXT,PROXY TEXT,TARGET int,PART_DATE text)")
con.commit()
sql = "INSERT INTO ADULT_TRAIN VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

p = Path(__file__).with_name('Adult_train_data_sqlite.txt')

with open(p) as file:
    lines = file.readlines()
    lines.pop(0)
    lines = [line.rstrip() for line in lines]

LineArray = [line.split(',') for line in lines]


cursor.executemany(sql,LineArray)
con.commit()

con.close()