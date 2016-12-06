import pickle

class File():
    @staticmethod
    def readOfFileByte(name):
        file = open(name, 'rb')
        return pickle.load(file)

    @staticmethod
    def writeToFileByte(name, list):
        file = open(name, 'wb')
        pickle.dump(list, file)
        file.close()