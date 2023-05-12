from connect import *
import time


def search():
    # enter the name of the search field
    searchField = input(
        "Which field would you Search: (Film Title, yearReleased, Rating, Duration, Genre,  )? "
    ).title()
    # enter the value of the field you are searching through
    searchValue = input(
        f"Enter the value for the {searchField} you want to search "
    ) #.capitalize()
    print(f"The search value enter by user is {searchValue} ")

    searchValue = "'" + searchValue + "'"
    print(f" Amended search value {searchValue} ")

    cursor.execute("SELECT * FROM tblFilms WHERE " + searchField + "=" + searchValue)
    "Method 2"
    # cursor.execute(f"SELECT * FROM  films WHERE {searchField} = {searchValue}")
    conn.commit()

    time.sleep(3)
    row = cursor.fetchall()
    # casting(row) convert one datatype to another data type
    # casting the record(row) as a string to ensure we
    # are able to out put a msg
    # if the search string value not in database
    strRow = str(row)
    if searchValue in strRow:  # .title()
        for record in row:
            print(record)
    else:
        print(
            f"The field {searchField} does not contain a {searchValue} in the database!"
        )

    # conn.close()


search()