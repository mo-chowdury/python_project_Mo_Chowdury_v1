from connect import *

def read():
    try:
        cursor.execute("SELECT * FROM tblFilms") # select all records
        row = cursor.fetchall() # get all the selected records from the table in the db
        for aRecord in row:
            print(aRecord)
    except sql.OperationalError as e: 
        print(f"Records not found: {e}")

if __name__ == "__main__":
        read() # call/invoke the function/subroutine