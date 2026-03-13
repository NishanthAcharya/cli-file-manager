print("Simple Notepad Application")

print("1. Create a new file")
print("2. Read an existing file")
print("3. Append content to a file")

user_input = input("Please enter your choice: ")

while True:
    if user_input == "1":
        user_file_name = input("Enter the file name: ")
        f = open(user_file_name,"x")
        user_content = input("Enter the content you want to store in the file: ")
        f = open(user_file_name,"w")
        f.write(user_content)

        print("File has been created and the content was successfully added.")


    elif user_input == "2":
        user_file_reading = input("Enter the file name you want to read: ")
        f = open(user_file_reading,"r")
        reading = f.read()
        print("File Content:")
        print(reading)

    elif user_input == "3":
        user_file = input("Enter the file name to which you want to append content: ")
        f = open(user_file,"a+")
        user_appending = input("Enter the text you want to append: ")
        f.write(user_appending)
        f.seek(0)

        print("Updated File Content:")
        print(f.read())

    else:
        print("Invalid choice. The application will now terminate.")
