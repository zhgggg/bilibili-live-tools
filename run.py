from OnlineHeart import OnlineHeart
from Silver import Silver
from LotteryResult import LotteryResult
from Tasks import Tasks
from connect import connect
import asyncio

from printer import Printer
import bilibili
import os
import sys
import threading

# fileDir = os.path.dirname(os.path.realpath('__file__'))
# print(fileDir)
# file_color = fileDir + "/conf/color.conf"



printer = Printer()

bilibili = bilibili.bilibili()

bilibili.login()


bilibili.user_info()
bilibili.get_bag_list()
bilibili.fetchmedal()
task = OnlineHeart()
task1 = Silver()
task2 = Tasks()
task3 = LotteryResult()
task4 = connect(printer)


def main(loop):  
    tasks = [
        task.run(),
        task1.run(),
        task2.run(),
        task4.connect(),
        task3.query(),
        printer.clean_printlist()
    ]
    
    asyncio.set_event_loop(loop)
    
    loop.run_until_complete(asyncio.wait(tasks))
    
    loop.close()
    
def controler():
    while True:
        code = input('')
        if code == '1':
            bilibili.getlist()
        
loop = asyncio.get_event_loop()        
mainthread = threading.Thread(target=main, args=(loop,))
controlthread = threading.Thread(target=controler)

mainthread.start()
controlthread.start()

mainthread.join()
controlthread.join()

