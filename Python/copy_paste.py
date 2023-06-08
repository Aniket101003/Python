print("Jo6")
print("name:Aniket More")
print("grade:12 Div:A")
print("program to write those lines which have character 't' from one\
text file to another text file")

source=open("source.txt","r")
dest=open("Destination.txt","w")

for line in source.readlines():
    if "t" in line:
        dest.write(line)

source.close()
dest.close()
print("done")
