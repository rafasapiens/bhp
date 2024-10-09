import paramiko
#1 
def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    #2 
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    #3
    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())

if __name__ == '__main__':
    #4 
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Enter server IP: ') or '192.168.1.203'
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter command or <CR>: ') or 'id'
    #5 
    ssh_command(ip, port, user, password, cmd)

'''
We create a function called ssh_command 1, which makes a connection 
to an SSH server and runs a single command. Note that Paramiko supports 
authentication with keys instead of (or in addition to) password authentica-
tion. You should use SSH key authentication in a real engagement, but for 
ease of use in this example, we’ll stick with the traditional username and 
password authentication.
Because we’re controlling both ends of this connection, we set the pol-
icy to accept the SSH key for the SSH server we’re connecting to 2 and make 
the connection. Assuming the connection is made, we run the command 3
that we passed in the call to the ssh_command function. Then, if the command 
produced output, we print each line of the output.
In the main block, we use a new module, getpass 4. You can use it to 
get the username from the current environment, but since our username 
is different on the two machines, we explicitly ask for the username on the 
command line. We then use the getpass function to request the password 
(the response will not be displayed on the console to frustrate any shoulder-
surfers). Then we get the IP, port, and command (cmd) to run and send it to 
be executed 5.
'''
