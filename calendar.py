#!/usr/bin/python3
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    def isEmpty(self):
        return true if head == None else false
    def insertNode(self, data):
        if self.isEmpty():
            newNode = Node(data)
            self.head = newNode
        else:
            traverser = self.head
            while data.date > traverser.date and traverser.nextPointer != None:
                traverser = traverser.nextPointer
            newNode = Node(data)
            traverser.nextPointer = newNode

class Node(object):
    def __init__(self, data = None, nextPointer = None):
        self.data, self.nextPointer = data, nextPointer
    def getData(self):
        return self.data
    def getNext(self):
        return self.nextPointer
    def setNext(self, newNext):
        newNext.nextPointer = self.nextPointer
        self.nextPointer = newNext


class Data():
    def __init__(self, name, time, date, description = None):
        self.name, self.time, self.date, self.description = name, time, date, description

def readFile():
    #if calendar.txt doesn't exist python throws error
    fh = open('calendar.txt')
    import os
    if os.path.getsize("calendar.txt") == 0:
         return
    getEvents(fh)

def getEvents(fh):
    for line in fh:
        print (line)
def mainMenu():
    print("Please choose from the following options:")
    print("1. Add Event")
    print("2. Delete Event")
    print("3. Update Event")
    print("4. Check Events on a specific date")
    print("5. Print out all Events")
    print("6. Exit Program")

def main():
    readFile()
    mainMenu()

if __name__ == "__main__": main()
