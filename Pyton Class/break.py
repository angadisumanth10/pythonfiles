#Print 1 to 4
from bdb import Breakpoint


for i in range(1,11):
    if(i==5):
        break
    print(i)
