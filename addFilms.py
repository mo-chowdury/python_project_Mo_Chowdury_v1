from connect import *
from time import sleep
from readFilms import *

#subroutine
def insertFilms():
    # create an empty list
    films = [] #0, 1, 2
    # ask for user input for the songs table(SongID, Title, Genre)
    title = input("Enter Film Title: ")
    rating = input("Enter Age Rating: ")
    genre =  input("Enter Film Genre: ")
    yearReleased = input("Enter Film Year: ")

    # append data from user to the table list
    title.append(title)
    rating.append(rating)
    genre.append(genre)
    yearReleased.append(yearReleased)
    # INSERT INTO songs (Title, Genre) VALUES("A","b","c")

    # INSERT INTO songs VALUES(NULL,"A","b","c")

    # INSERT DATA                            filmID, Title, Genre           
    # cursor.execute("INSERT INTO table VALUES(NULL, ?,?,?)", films)
    # or 
    try:
        cursor.execute("INSERT INTO Films (Title, Rating, Genre, yearReleased) VALUES(filmID,duration,)", films)
        conn.commit() # make the change permanent
        print(f"Title {title} added into the tblFilms table")
        # read from the database
        sleep(3) # delay the execution of any code that follows for 3 seconds
        read() # call/invoke the function/subroutine
    except sql.OperationalError as e: 
        conn.rollback()
        print(f"Record not added to database: {e}")

       
  

#prevent the file/methods from the file to be automatically executed when imported
#into another python file
if __name__ == "__main__":
    insertFilms()
    




