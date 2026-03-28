import pandas as pd
import sqlite3

database = 'basketball2.sqlite'
conn = sqlite3.connect(database)
print('Opened data successfully')

tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type='table';""",conn)
print(tables)

team = pd.read_sql("""SELECT * FROM Team;""",conn)
print(team)

name1 = pd.read_sql("""SELECT full_name,nickname,city,year_founded FROM Team
                    WHERE year_founded > 1990; """,conn)
print(name1)

state = pd.read_sql("""SELECT full_name,state FROM Team
                    WHERE state = 'Texas';""",conn)
print(state)

state1 = pd.read_sql("""SELECT full_name,state FROM Team
                    WHERE state = 'New York';""",conn)
print(state1)

team2 = pd.read_sql("""SELECT full_name FROM Team
                    WHERE full_name LIKE 'Los%';""",conn)
print(team2)

year1 = pd.read_sql("""SELECT full_name,MIN(year_founded) FROM Team;""",conn)
print(year1)

year2 = pd.read_sql("""SELECT full_name,MAX(year_founded) FROM Team;""",conn)
print(year2)