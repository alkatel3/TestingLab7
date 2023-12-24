import paramiko
import subprocess
import pytest
import time

@pytest.fixture(scope='function')
def server():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect('192.168.157.4', 5001, 'alkatel3', 'My_Password')
        ssh_client.exec_command("iperf -s")
        time.sleep(2)
    except Exception as e:
        print("Fail: {}".format(e))
    finally:
        ssh_client.close()

@pytest.fixture(scope='function')
def client(server):
    _ = server
    command = ["iperf", "-c", '192.168.157.4', "-i", "1"]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout.splitlines()
        errors = result.stderr.splitlines() if result.stderr else []
        return output, errors
    except subprocess.CalledProcessError as e:
        return [], ["Error: {}".format(e)]
