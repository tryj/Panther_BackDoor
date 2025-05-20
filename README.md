**

# Panther_BackDoor
Back door program that I wrote to study the attack principle of Backdoor with python.

## How to install
``` bash
git clone https://github.com/tryj/Panther_BackDoor.git
cd Panther_BackDoor
pip install -r requirements.txt
``` 

## How to use
Activate the server
``` bash
python server.py
```

Launch the client on the victim machine
``` bash
python client.py
```

## command
view_cmd: View path address

custom_dir: View folders and files

download_file:
1.Enter the file address and file name you want to download.
2.Enter the address where you want to place the file and specify the file name and extension (you can rename it).

remove_file:
1.Enter the address where you want to delete the file and specify the file name and extension.

send_files:
1.Enter the address where you want to send the file and specify the file name and extension.
2.Enter the address where you want the sent files to be delivered, along with the file name and extension.

sleep: Turn off the victim
