import os,time,random
def filetimeset(path):
    # f_time = year + '-' + month + '-' + day #访问时间
    x_time = '2016' + '-' + str(random.randint(3,12)) + '-' + str(random.randint(1,30)) + ' ' + str(random.randint(8,17)) + ':' + str(random.randint(0,59)) + ':' + str(random.randint(0,59))#修改时间
    x_time = time.mktime(time.strptime(x_time,"%Y-%m-%d %H:%M:%S"))
    os.utime(path, (x_time, x_time))
    print('success!')

def listfiles(dir):
    files = os.listdir(dir)
    n =0
    for root, dirs, files in os.walk(dir):
        for name in files:
            filetimeset(os.path.join(root, name))
            n += 1
    print(n)
listfiles('J:/')
