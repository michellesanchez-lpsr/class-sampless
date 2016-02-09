# open a file for writing
# second argument:
# r is for reading 
# r+ is for reading and writing (existing file)
# w is for writing but (be careful it starts writing from the begining)
# a is append - writing *from the end  
myFile = open("numList.txt ", "w")

# create a list to write to my file
nums = range(1,500)

# write each item to the file
for n in nums :
	myFile.write(str(n) + '\n')

myFile.close()

# close the file


