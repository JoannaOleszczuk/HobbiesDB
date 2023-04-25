import sys

def Welcome():
    print("Hello :) ")
Welcome()

def HobbiesPrinter(localdb):

    for element in localdb:
        print("Hello, my name is " + str(element[0]) + ", my hobby is: " + str(element[1]))
try:
    db = []
    while True:
        temp_db = []
        menu = int(input("Type 1 to add hobbies to db, 2 to see db, 3 to remove sth or 4 to exit: "))
        if menu == 1:
            while True:
                temp_hobby = input("Type your hobby ")
                temp_name = input("Type your name ")
                temp_db.append(temp_name)
                temp_db.append(temp_hobby)
                db.append(temp_db)
                endNo1 = int(input("Type 1 to add data or 0 to exit: "))
                if endNo1 == 1:
                    pass
                else:
                    break
            # print(db)
            db_file = open("pliczekTXT", 'a')
            db_file.write(str(db))
            db_file.close()  #zwolnienie RAMu
            db_file = open("pliczekTXT", 'r')
            print(db_file.read())
            db_file.close()
        elif menu == 2:
            db_file = open("pliczekTXT", 'r')
            print((db_file.read()))
            db_file.close()
        elif menu == 3:
            pass
        elif menu == 4:
            break
        else:
            print("Please use the numbers from the menu!")
except ValueError as e:
    print("Incorrect type of value. Value must be integer. See the error", e)
except:
    print("Error occurs!", sys.exc_info())

HobbiesPrinter(db)
