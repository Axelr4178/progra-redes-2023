"""
    Autor:Axel Alejandro Almaguer Rodriguez
    Descripcion: Problemas Python Institute
"""

class Timer:
    def __init__( self, a,b,c ):
        self.num = a*60*60 + b*60 + c 

    def __str__(self):
        return str(int(self.num/(60*60)))+":"+str(int(self.num/60%60))+":"+str(self.num%60)

    def next_second(self):
        self.num = self.num + 1
        if(self.num >= 60*60*24):
            self.num = 0

    def prev_second(self):
        self.num = self.num - 1
        if(self.num < 0):
            self.num = 60*60*24 - 1

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
