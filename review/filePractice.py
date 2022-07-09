myFile = open("fileToWriteTo.txt", "r")
lineFromFile = myFile.readline()
myFile.close
print(lineFromFile)

myFile = open("fileToWriteTo.txt", "a")
myFile.write("\nThis is the second line added to the file by Python.")
myFile.close()