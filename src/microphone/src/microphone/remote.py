from typing import Optional
import paramiko


class RemoteDevice:
    def __init__(self, ip: str, port: int, username: str, password: str):
        self.ip: str = ip
        self.port: int = port
        self.username: str = username
        self.password: str = password
        self.ssh: Optional[paramiko.SSHClient] = None
        self.sftp: Optional[paramiko.SFTPClient] = None

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, self.port, self.username, self.password)

    def push(self, local_path: str, remote_path: str):
        sftp = self.ssh.open_sftp()
        sftp.put(local_path, remote_path)

    def pull(self, remote_path: str, local_path: str):
        sftp = self.ssh.open_sftp()
        sftp.get(remote_path, local_path)

    def close(self):
        self.sftp.close()
        self.sftp = None
        self.ssh.close()
        self.ssh = None

    def run_command(self, command: str):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        # return stdout.read().decode("utf-8")
