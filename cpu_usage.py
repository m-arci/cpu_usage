import subprocess
import re

def print_top():

    top = subprocess.Popen('top -b -n 1 -w 512 | grep vhost', shell=True, stdout=subprocess.PIPE, universal_newlines=True)

    top_comm = top.communicate()
    print(top_comm)

    # ensure correct float number parsing
    # qemu_list = re.sub(',', '.', top.communicate()[0])
    #qemu_list = re.sub(',', '.', top_comm[0])
    #print(qemu_list)


def print_top_1():

    top = subprocess.Popen('top -b -n 1 -w 512|grep marci', shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    top_comm = top.communicate()
    splitted_top = re.split('\n',top_comm[0])
    #print(top_comm)
    #print(splitted_top[0])
    #print(splitted_top[5])
    print(splitted_top)

    splitted_array = re.split(',',splitted_top[0])
    for i in splitted_top:
      print(splitted_array)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_top_1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
