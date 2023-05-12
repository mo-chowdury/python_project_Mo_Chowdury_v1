from connect import *

# subroutines
def allrecords():
    cursor.execute("SELECT * FROM tblFilms") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for aRecord in row:
        print(aRecord)

def genre():
    genre = input("Enter Genre: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE Genre = '{genre}' ") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for aRecord in row:
        print(aRecord)

def year():
    yearReleased = input("Enter film year: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = '{yearReleased}' ") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for aRecord in row:
        print(aRecord)
  

def rating():
    artistName = input("Enter rating: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{rating}' ") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for aRecord in row:
        print(aRecord)

def title():
    genre = input("Enter film name: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE title = '{title}' ") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for aRecord in row:
        print(aRecord)

"""def filmID():
    idField = int(input("Enter film ID: "))
    cursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idField} ") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for aRecord in row:
        print(aRecord)"""


if __name__ == "__main__":
    # call/invoke the function/subroutine
    allrecords()
    genre()
    year()
    rating()
    title()
    #filmID()

