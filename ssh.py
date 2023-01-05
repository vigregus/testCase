import argparse
import subprocess
from threading import Thread


def sshConnect(hosts,user,password,cmd):
    try:
        cmd = subprocess.run([
                "sshpass -p "+password+" ssh -o StrictHostKeyChecking=no -o LogLevel=ERROR -o UserKnownHostsFile=/dev/null "+user+"@"+hosts+" "+cmd],
                shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(cmd.stdout)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--hosts', action='store', dest='hosts', required=True,
                        help='hosts ips: e.g. xxx.xxx.xxx.xxx,yyy.yyy.yyy.yyy')
    parser.add_argument('--user', action='store', dest='user', required=True, help='user name')
    parser.add_argument('--password', action='store', required=True, dest='password', help='password')
    parser.add_argument('--cmd', action='store', required=True, dest='cmd', help='cmd name')
    args = parser.parse_args()
    for ip in args.hosts.split(','):
        print("connecting to ", ip)
        Thread(target=sshConnect, args=(ip, args.user, args.password, args.cmd,)).start()
