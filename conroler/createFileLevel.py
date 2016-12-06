from moved.logic.Level import Level
from view.workWithFile import *

class NewFile():
    @staticmethod
    def createLevel():
        level = ['fileLevel\level1.bat', 'fileLevel\level2.bat', 'fileLevel\level3.bat', 'fileLevel\level4.bat', 'fileLevel\level5.bat',
                 'fileLevel\level6.bat', 'fileLevel\level7.bat', 'fileLevel\level8.bat', 'fileLevel\level9.bat', 'fileLevel\level10.bat' ]
        monitor = [4300, 600]
        period = 6;
        for i in range(0,len(level)):
            buflevel = Level.generationLevel(level[i], monitor, period)
            File.writeToFileByte(level[i], buflevel)
            period += 3
            monitor[0] += 500
