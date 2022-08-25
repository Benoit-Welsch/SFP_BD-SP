from os import listdir, path
from pydoc import describe
from time import sleep

def availableMacro():
    return [f for f in listdir("./macro") if (f.endswith('.nxbt'))]

class Macro:

    def __init__(self, name):
        if(not path.exists(path)):
            raise Exception('File do not exist')

        file = open("./macro/" + name, 'r')

        self.name = name
        self.action = []
        currentAction = {}

        for i, line in file:
            if(i == 0 and line.startsWith("###")):
                self.description = line
            elif(line.startsWith("#")):
                currentAction = {'description' : line.replace("# ", ""), "macro": []}
            else:
                currentAction["macro"].append(line)


        file.close()

    def run():
        input("Press ENTER when you are ready !")
        print("3 ...")
        sleep(1)
        print("2 ...")
        sleep(1)
        print("1 ...")
        sleep(1)
        print('0 Go!')
            

    def dryRun():
        print('Dry run')   
