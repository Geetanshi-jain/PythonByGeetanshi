
#2.. Reading from a File
f = open("example.txt", "r")
print(f.read())           # Read entire file
print(f.read(5))          # Read first 5 characters
print(f.readline())       # Read first line
print(f.readlines())      # Read all lines as list
f.close()

 #3. Writing to a File
f = open("example.txt", "w")
f.write("Hello, Python!\n")
f.write("Second line.")
f.close()

#4. Appending to a File
f = open("example.txt", "a")
f.write("\nThis will be added at the end.")
f.close()

#5. Using with (Best Practice)
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
    
#Automatically closes the file.
#file modes
"""read()	Read entire file
readline()	Read one line
readlines()	Returns a list of lines
write(str)	Writes a string
writelines()	Writes a list of strings"""
