# many_ssh
A script which tries brute force ssh many system and locates the working IP corresponding to login credentials

# Example:
Let's say you know the credentials of your computer in a remote location. The username is 'saint101' and password is 'austere000'. Now, you wish to know the IP address of your system. So, somebody who is present in the remote location can run the following commands to locate the IP address.

# Commands: 
1. Install nmap
2. Run this command to find all the pingable IP's in the range [0,255] for base IP: 192.168.1.0 
```
$ nmap 192.168.1.0/24 > log
```
3. Run this command which executes the python script. Open the file 'log1' to find the corresponding IP address.
```
time python3 many_ssh.py > log1
```

# Reference:
https://stackoverflow.com/questions/3586106/perform-commands-over-ssh-with-python
