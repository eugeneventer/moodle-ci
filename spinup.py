import sys
from openstack import CloudSlave

if __name__ == "__main__":
    instancename = sys.argv[1]  # use argparse to be proper :D

    minion = CloudSlave(instancename)
    instanceip = minion.spinup()

    # write ip to a file, to be picked up by bash
    filepath = '/tmp/%s' % instancename
    f = open(filepath, 'w+')
    f.seek(0)
    f.write(instanceip)
    f.truncate()  # truncate any following lines, just in case
    f.close()

    print('Cloud instance up at %s!' % instanceip)
