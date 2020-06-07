#!/usr/bin/python

import os
import sys
import select
import paramiko
import time


class Commands:
    def __init__(self, retry_time=0):
        self.retry_time = retry_time
        pass

    def run_cmd(self, host_ip, cmd_list):
        i = 0
        while True:
        # print("Trying to connect to %s (%i/%i)" % (self.host, i, self.retry_time))
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host_ip,username='saint101', password='austere000')
                print('Trying to ssh connect')
                #ssh.connect(host_ip)
            except paramiko.AuthenticationException:
                print("Authentication failed when connecting to %s" % host_ip)
                return
            except:
                print("Could not SSH to %s, waiting for it to start" % host_ip)
                i += 1
                time.sleep(2)

            # If we could not connect within time limit
            """
            if i >= self.retry_time:
                print("Could not connect to %s. Giving up" % host_ip)
                return        # After connection is successful
            """
            # Send the command
            for command in cmd_list:
                # print command
                print ("> " + command)
                # execute commands
                stdin, stdout, stderr = ssh.exec_command(command)
                opt = stdout.readlines()
                opt = "".join(opt)
                print(opt)

            # Close SSH connection
            ssh.close()
            return

def main():

    filepath = 'log'
    ip_list = []
    with open(filepath) as fp:
        for line in fp:
            var = line.split()
            #print(var)

            if(var!=[] and var[-1][0:3]=='192'):
                #print(var[-1])
                ip_list.append(var[-1])
        
    # args = {'<ip_address>', <list_of_commands>}
    #ip_list = ['192.168.1.248', '192.168.1.248', '192.168.1.79', '192.168.1.248']
    #print(ip_list)
    #ip_list.remove('192.168.1.61')
    #ip_list.remove('192.168.1.78')
    #ip_list.remove('192.168.1.175')
    #ip_list.remove('192.168.1.201')
    #ip_list.remove('192.168.1.235')
    #ip_list.append('192.168.1.248')
    for ip in ip_list:
        mytest = Commands()
        print("Running IP: " + ip)
        mytest.run_cmd(host_ip=ip, cmd_list=['ls'])
    
    return


if __name__ == "__main__":
    main()
