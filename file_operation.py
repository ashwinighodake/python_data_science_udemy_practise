fd=open("practise.txt",'r',encoding='ISO-8859-1')
print("Information about file:",fd)
print("Contents of whole file")
print(fd.read())
print("Reading single line from file")
print(fd.readline())

print("Current file position is:",fd.tell())
fd.seek(0)

print("contents of whole file")
print(fd.read())

fd.close()
fd=open("practise.txt",'a')
fd.write("Hi i am ashwini here\n")
fd.write("How are you? \n")
fd.seek(0)
fd=open("practise.txt",'r',encoding='ISO-8859-1')

print(fd.read())

fd.close()