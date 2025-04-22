import sqlite3

with sqlite3.connect('roster.db') as connection:
    cursor = connection.cursor()

    query = "drop table if exists Roster"
    cursor.execute(query)

    query = "create table Roster (Name TEXT, Species TEXT, Age INT)"
    cursor.execute(query)

    print("Jadval yaratildi.")


import sqlite3

with sqlite3.connect('roster.db') as connection:
    cursor = connection.cursor()

    query = "insert into Roster values ('Benjamin Sisko', 'Human', 40)"
    cursor.execute(query)

    query = "insert into Roster values ('Jadzia Dax', 'Trill', 300)"
    cursor.execute(query)

    query = "insert into Roster values ('Kira Nerys', 'Bajoran', 29)"
    cursor.execute(query)

    print("Ma'lumotlar qo'shildi.")

import sqlite3

with sqlite3.connect('roster.db') as connection:
    cursor = connection.cursor()

    query = "update Roster set Name = 'Ezri Dax' where Name = 'Jadzia Dax'"
    cursor.execute(query)

    print("Ism yangilandi.")

import sqlite3

with sqlite3.connect('roster.db') as connection:
    cursor = connection.cursor()

    query = "select Name, Age from Roster where Species = 'Bajoran'"
    cursor.execute(query)

    results = cursor.fetchall()
    print("Natija:")
    print(results)
