import pandas as pd
import sqlite3

database = 'basketball.sqlite'
conn = sqlite3.connect(database)
print('Opened data successfully')

tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type='table';""",conn)
print(tables)

salary = pd.read_sql("""SELECT * FROM Player_Salary;""",conn)
print(salary)

player = pd.read_sql("""SELECT * FROM Player;""",conn)
print(player)
