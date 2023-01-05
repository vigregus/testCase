import argparse
import subprocess
import shutil
import psutil
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--countZ', action='store', dest='z', help='user name')
    parser.add_argument('--sizeY', action='store', dest='y', help='user name')
    parser.add_argument('--freeX', action='store', dest='x', help='user name')
    args = parser.parse_args()
#    print(psutil.disk_partitions())
#    print(shutil.disk_usage('/home'))
    suitable_local_drives = {}
    for disk in psutil.disk_partitions():
        # check network disk or not
        #print(disk[0],disk[1],shutil.disk_usage(disk[1])[2])
        if not disk[0].startswith('//'):
            free_space = shutil.disk_usage(disk[1])[2]
            if  free_space > int(args.x):
                suitable_local_drives[(disk[1])] = free_space
            else:
                print("Not enought free space")
                sys.exit(0)
        else:
            print(disk[0]+' is network Drive')
    #calculating mount point
    print("List of suitable disks with Free Space ")
    print(suitable_local_drives)
    mount_point = list(suitable_local_drives.keys())[0]
    #print(mount_point)

    if mount_point.endswith('/'):
        work_folder =  mount_point+"data"
    else:
        work_folder =  mount_point+"/data"

    print("Work folder is: "+work_folder)
    try:
        subprocess.run("mkdir "+work_folder, shell=True )
    except:
        print("couldnt create working Dir")
        sys.exit(0)
    
    #creating Z files with Y size

    for i in range(int(args.z)):
        subprocess.call("base64 /dev/urandom | head -c "+args.y+">"+work_folder+"/"+str(i)+".dat",shell=True)
    
    #copy with dd
    for i in range(int(args.z)):
        print("Working with "+str(i)+".dat")
        try:
            time = subprocess.run("dd if="+work_folder+"/"+str(i)+".dat of="+work_folder+"/"+str(i)+"_new.dat",shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print(str(time.stdout).split(',')[2])
        except:
            print('smth wrong')
