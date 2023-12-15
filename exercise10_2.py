# User input:
user_choice = input("Would you like to read or write into the guestbook? (r/w)\n")

# check input:
if user_choice == "r":
    f = open('guestbook.txt')
    content = f.read()
    # converting text into a list:
    data_into_list = content.split("\n")
    # printing each line in a loop:
    for line in data_into_list:
        print(line)
elif user_choice == "w":
    # ask user for input:
    new_message = input("Write a new message:\n")
    # open a file in an append mode:
    file = open("guestbook.txt", "a")
    # append new message to the file:
    file.write(new_message)
    file.write("\n")
    # close the file:
    file.close()
else:
    raise ValueError("Try again")
