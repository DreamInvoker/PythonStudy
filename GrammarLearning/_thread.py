import _thread
import time


def print_time(threadNmae, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadNmae, time.ctime(time.time())))


try:
    _thread.start_new_thread(print_time, ('Thread-1', 1))
    _thread.start_new_thread(print_time, ('Thread-2', 1))
except:
    print('Error：无法启动线程')


while 1:
    pass