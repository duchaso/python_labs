def menu():
    print("1) Create a new file")
    print("2) Display the file")
    print("3) Add a new item to the file")
    return int(input("Make a selection 1, 2 or 3: "))


#---main---#
usr_choice = menu()
while usr_choice < 1 or usr_choice > 3:
    print("Wrong input. Please enter choice 1, 2 or 3.")
    usr_choice = menu()

if usr_choice == 1:
    f = open("data/Subject.txt", 'w')
    usr_subj = input("Enter a subject: ")
    f.write(usr_subj+'\n')
elif usr_choice == 2:
    f = open("data/Subject.txt", 'r')
    print(f.read())
elif usr_choice == 3:
    f = open("data/Subject.txt", 'a')
    usr_subj = input("Enter a subject: ")
    f.write(usr_subj + '\n')
    f = open("data/Subject.txt", 'r')
    print(f.read())