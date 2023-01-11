import glob

import paramiko
from paramiko.client import AutoAddPolicy


class remote_operations:
     def __init__(self):
          pass

     def connect(self, hostname, username, password):
         client = paramiko.SSHClient()
         client.set_missing_host_key_policy(AutoAddPolicy) # Unsafe Connection
         # client.load_system_host_keys()
         client.connect(hostname=hostname, username=username, password=password)
         return client

     def open_remote_file(self, ssh_client, filename):
         sftp_client = ssh_client.open_sftp()
         file = sftp_client.open(filename)
         return file

     def open_remote_folder(self, ssh_client, folderpath):
         sftp_client = ssh_client.open_sftp()
         folder = sftp_client.listdir(folderpath)
         return folder

if __name__ == '__main__':
    test = remote_operations()
    client = test.connect(hostname='172.20.36.69', username='118512', password='ab@ntGLb')

    filenames = test.open_remote_folder(client, '/home/settlement_tob/bni/backup/recon/2022/12/01/')
    for filepath in filenames:
        file = test.open_remote_file(client, f'/home/settlement_tob/bni/backup/recon/2022/12/01/{filepath}')
        for index, line in enumerate(file):
            if index >= 1 :
                print(line)
            else:
                continue
    file.close()
    client.close()