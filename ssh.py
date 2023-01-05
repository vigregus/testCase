import argparse
import subprocess

def sshConnect(hosts,user,password,cmd):
    cmd = subprocess.run([
                             "sshpass -p "+password+" ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null "+user+"@"+hosts+" "+cmd],
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(cmd.stdout)  

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', action='store', dest='action',
                        choices=['env-start', 'connect'], required=True,
                        help='Actions for aws')
    parser.add_argument('--hosts', action='store', dest='hosts', required=True,
                        help='hosts ips: e.g. xxx.xxx.xxx.xxx,yyy.yyy.yyy.yyy')
    parser.add_argument('--user', action='store', dest='user', help='user name')
    parser.add_argument('--password', action='store', dest='password', help='ELB name')
    parser.add_argument('--cmd', action='store', dest='cmd', help='cmd name')

    args = parser.parse_args()
    print(args.hosts)
    print(args.password)
    print(args.cmd)

    sshConnect(args.hosts,args.user,args.password,args.cmd)
