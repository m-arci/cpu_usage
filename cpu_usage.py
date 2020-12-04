import subprocess
import re

def print_top_1():

    top = subprocess.Popen('top -b -n 1 -w 512|grep marci', shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    top_comm = top.communicate()
    #print(top_comm)
    splitted_top = re.split('\n',top_comm[0])
    del splitted_top[-1]
    #print(splitted_top)

    for i in splitted_top:
      split = re.split('\s+',i)
      print(split[9])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_top_1()


