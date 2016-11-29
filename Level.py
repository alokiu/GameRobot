import random

class Level:
    @staticmethod
    def generationLevel(level, monitor):
        lvl = []
        for i in range(int(monitor[0]/40)):
            lvl.append([])
        for i in range(len(lvl)):
            for j in range(int(monitor[0]/40)):
                if i<10:
                    lvl[i].append(" ")
                else :
                    lvl[i].append("*")
                if (j%6 == 0 and i == 11 ):
                    flag = random.randint(0,1)
                    lvl[i-2].insert(j,"|")
                    if (flag == 0):
                        lvl[i - 3].insert(j, "|")
        print("level complite!!")
        return lvl




