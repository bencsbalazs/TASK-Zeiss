class heavyLifter:

    '''
    This is the HeavyLifter class what will
    do the simulation of the reorder of the 
    warehouse.
    '''

    orders = []
    stacks = []

    def __init__(self, inputFile) -> None:
        self.processFile(inputFile)

    def moveElement(self, moveFrom, boxes=1):
        return moveFrom[-boxes:]

    def getRemainingPlace(self, elements, place):
        return elements[place][:-1]

    def placeBoxToPosition(self, elements, place, box):
        return str(elements[place] + box)

    def processFile(self, filePath) -> None:
        places = []
        # Processing the instruction set file...
        # Create the data structures.
        with open(filePath) as file:
            for line in file:
                if "move" in line:
                    self.orders.append(line)
                if line in ['\n', '\r\n']:
                    continue
                if "|" in line:
                    stack = 0
                    for i in range(1, len(line), 4):
                        if len(places) < stack+1:
                            places.append("")
                        places[stack] += line[i]
                        stack += 1
            self.stacks = list(map(lambda x:x[::-1].strip(), places))

    def executeOrders(self):

        # Walk through the commands
        for order in self.orders:
            o = order.split()
            i = int(o[1])
            while i >= 1:
                # Get the box identifier to replace
                letterToAdd = self.moveElement(self.stacks[int(o[3])-1])
                # Remove box from position
                self.stacks[int(o[3])-1] = self.getRemainingPlace(self.stacks, int(o[3])-1)
                # Add box to new position
                self.stacks[int(o[5])-1] = self.placeBoxToPosition(self.stacks, int(o[5])-1, letterToAdd)
                i = i-1

    def showTopBoxes(self) -> None:
        boxesOnTop = ""
        for stack in self.stacks:
            boxesOnTop += stack[-1]
        print(boxesOnTop)


# Example from the readme.md and task.md files
heavyLifterV1 = heavyLifter("docs/instruction_set_01.txt")
heavyLifterV1.executeOrders()
heavyLifterV1.showTopBoxes()
