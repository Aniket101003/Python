print("program to calculate number of vowels present in a text file")
print()

file=open('story.txt' , "r")
content=file.read()
vowel_count=0
for i in content:
    if( i=='A' or i=='a' or i=='E' or i=='e' or i=='I' or i=='i' \
        or i=='O' or i=='o' or i=='U' or i=='u'):
        vowel_count+=1
print("The number of vowels present in the file are:", vowel_count)

file.close()
