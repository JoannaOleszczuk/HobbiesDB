import sys

def Welcome():
    print("Hello :) ")
Welcome()

def HobbiesPrinter(localdb):

    for element in localdb:
        print("Hello, my name is " + str(element[0]) + ", my hobby is: " + str(element[1]))
try:
    while True:
        menu = int(input("Type 1 to add hobbies to db, 2 to see db, 3 to remove sth or 4 to exit: "))
        db = []
        if menu == 1:
            while True:
                temp_name = input("Type your name ")
                temp_hobby = input("Type your hobby ")
                temp_db = [temp_name + ", " + temp_hobby + "\n"]
                db_file = open("pliczekTXT", 'a')
                db_file.writelines(temp_db)
                db_file.close()  #zwolnienie RAMu

                endNo1 = int(input("Type 1 to add data or 0 to exit: "))
                if endNo1 == 1:
                    pass
                else:
                    print("Please see current db: ")
                    db_file = open("pliczekTXT", 'r')
                    print(db_file.read())
                    db_file.close()
                    break
        elif menu == 2:
            print("Please see current db: ")
            db_file = open("pliczekTXT", 'r')
            print((db_file.read()))
            db_file.close()
        elif menu == 3:
            while True:
                # removingQuestion = input("Type the person u would like to remove: ")

        elif menu == 4:
            break
        else:
            print("Please use the numbers from the menu!")
except ValueError as e:
    print("Incorrect type of value. Value must be integer. See the error", e)
except FileNotFoundError as notOkFile:
    print(notOkFile)
except:
    print("Error occurs!", sys.exc_info())
else:
    pass
finally:
    print("Thank u for being a part of db users")

HobbiesPrinter(db)
