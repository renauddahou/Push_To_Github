import threading #threading is a module that allows multiple procceses to run concurrenlty
from threading import Thread
import time
class CPUPainter:
    def paintwall(self):
        time.sleep(2)
        print("Wall Painted")
    def __init__(self):
        t = threading.Thread(target= self.paintwall)
        t.start()
#syntax to create thread class: Thread(group= None, target= None, name= None, args=(), kwargs=())
CPUPainter()