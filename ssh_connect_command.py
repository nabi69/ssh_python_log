import paramiko
import datetime

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

now = datetime.datetime.now()
filename = now.strftime("%Y%m%d_%H%M%S") + '.txt'

ip = input('Enter an IP address: ')
port = input('Enter a port number: ')
user = input('Enter username: ')
password = input('Enter password: ')

try:
    # ssh.connect('158.174.251.106', port=8001, username='xpgroup', password='dhaka123')
    ssh.connect(ip, port=port, username=user, password=password)
    print('Connected to the server')
    while True:
        command = input('Enter a Linux command: (exit to terminate) ')
        if command == 'exit':
            break
        stdin, stdout, stderr = ssh.exec_command(command)
        # print('Command : '+ command)
        # print('output:\n')
        with open(filename, 'a') as f:
            f.write('Command : '+ command)
            f.write('\noutput:\n')
            for line in stdout:
                f.write(line.strip()+ '\n')
                # print(line.strip())
        # for line in stdout:
        #     print(line.strip())


except paramiko.AuthenticationException:
    print('Authentication failed, please verify your credentials')
except paramiko.SSHException as sshException:
    print(f'Unable to establish SSH connection: {sshException}')
except paramiko.Exception as e:
    print(f'Exception in connecting to the server: {e}')

ssh.close()