import sqlite3

connection = sqlite3.connect('fomo.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text UNIQUE, email text UNIQUE, age INTEGER, password text, location text, option_1 text, option_2 text, option_3 text, option_4 text)"
cursor.execute(create_table)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
  print(row)

connection.commit()

connection.close()