import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect('158.174.251.106', port=8001, username='xpgroup', password='dhaka123')
    print('Connected to the server')
    while True:
        command = input('Enter a Linux command: ')
        if command == 'exit':
            break
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.readlines())
except paramiko.AuthenticationException:
    print('Authentication failed, please verify your credentials')
except paramiko.SSHException as sshException:
    print(f'Unable to establish SSH connection: {sshException}')
except paramiko.Exception as e:
    print(f'Exception in connecting to the server: {e}')

ssh.close()