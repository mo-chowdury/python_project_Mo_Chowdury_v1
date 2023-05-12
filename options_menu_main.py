from readFilms import *
from addFilms import *
from updateFilms import *
from deleteFilms import *
# from reports import *
import reports

#create a function
"Main Menu options"
def menuOptions():
    options = 0 # local variable with a value 0
    # while 0 not in ["1","2","3","4","5","6"]:
    while options not in ["1","2","3","4","5","6",]:
        print("tblFilms Menu Options\nEnter\n1. To Print.\n2. To Add.\n3. To Update.\n4. To Delete.\n5. Report Menu.\n6. To Exit Options Menu")
        #re-assign the value of the options variable
        options = input("Enter an option from the Menu choices above: ") # defualt datatype for input is string
        if options not in ["1","2","3","4","5","6"]:
            print(f"{options} not a valid choice!")
    return options


"Report Menu"
def reportOptionsMenu():
    options = 0 # local variable with a value 0
    # while 0 not in ["1","2","3","4","5","6", "7", "8"]:
    while options not in ["1","2","3","4","5", "6", "7", "8"]:
        print("Report Menu Options\nEnter to Print By\n1. TO All records.\n2. To filmID.\n3. TO title.\n4. To yearReleased.\n5. To rating. \n6. To duration. \n7. To genre. \n8. To Exit Reports Menu")
        #re-assign the value of the options variable
        options = input("Enter an option from the Report Menu choices above: ") # defualt datatype for input is string
        if options not in ["1","2","3","4","5", "6", "7", "8"]:
            print(f"{options} not a valid choice!")
    return options



def films():

    "Main Program"
    mainProgram = True # assign mainProgram a variabe True of data type boolean

    # while True 
    while mainProgram:
        mainMenu = menuOptions()
        if mainMenu == "1":
            read() # call the read function from the readFilms.py file/application
        elif mainMenu == "2":
            insertFilms()
        elif mainMenu == "3":
            update()
        elif mainMenu == "4":
            delete() 
        elif mainMenu == "5":
            reportProgram = True
            while reportProgram:
                reportMenu = reportOptionsMenu()
                if reportMenu == "1":
                    reports.allrecords()
                elif reportMenu == "2":
                    reports.filmID()
                elif reportMenu == "3":
                    reports.title()
                elif reportMenu == "4":
                    reports.yearReleased()
                elif reportMenu == "5":
                    reports.rating()  
                elif reportMenu == "6":
                    reports.duration() 
                elif reportMenu == "7":
                    reports.genre()            
                else:
                    reportProgram = False
                    input("Press enter to exit the Report Menu: ")
        else:
            mainProgram = False
    input("Press enter to exit the Main Menu: ")
    return mainProgram
    
if __name__== "__main__":
    films()