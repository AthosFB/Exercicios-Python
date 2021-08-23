from sys import stdout
from time import sleep
for c in range(10, -1, -1):
    print("   ", c)
    sleep(1)

for b in range(0, 10):
    def animation():
        stdout.write("\r\033[m")
        sleep(0.3)
        stdout.write("\r\033[1;33m I")
        sleep(0.3)
        stdout.write("\r\033[1;31mI I")
        sleep(0.3)
        stdout.write("\r\033[1;36mIII")
        sleep(0.3)
    animation()
