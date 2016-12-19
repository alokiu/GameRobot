import random

class Level:
    @staticmethod
    def generationLevel(level, monitor, period):
        lvl = []
        for i in range(int(monitor[1]/40)):
            lvl.append([])
        for i in range(len(lvl)):
            for j in range(int(monitor[0]/40)):
                if i<14:
                    lvl[i].append(" ")
                else :
                    lvl[i].append("*")
                if (j%period == 0 and i == 14  ):
                    flag = random.randint(0,1)
                    lvl[i-1].insert(j,"|")
                    if (flag == 0):
                        lvl[i - 2].insert(j, "|")
        return lvl




