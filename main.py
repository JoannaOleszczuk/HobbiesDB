def Welcome():
    print("Hello World2")
Welcome()

def HobbiesPrinter(localdb):
    for element in localdb:
        print("Hello, my name is " + str(element[0]) + ", my hobby is: " + str(element[1]))

db = []
while True:
    menu = int(input("Type 1 to add hobbies to db, 2 to see db, 3 to remove sth or 4 to exit: "))
    if menu == 1:
        temp_db = []
        while True:
            temp_hobby = input("TYpe your hobby ")
            # if temp_hobby.lower() == "exit":
            #     break
            temp_name = input("Type your name ")
            # if temp_name.lower() == "exit":
            #     break
            # Hobbies(temp_name, temp_hobby)
            temp_db.append(temp_name)
            temp_db.append(temp_hobby)
            db.append(temp_db)
        # print(db)
        db_file = open("pliczekTXT", 'a')
        db_file.write(str(db))
        db_file.close()  #zwolnienie RAMu
        db_file = open("pliczekTXT", 'r')
        print(db_file.read())
        db_file.close()
        # print("Type exit to exit")
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


HobbiesPrinter(db)
