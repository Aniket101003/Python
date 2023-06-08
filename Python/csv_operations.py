import csv


print("program to perform read and write operation with .csv file")
print()

def WriteToFile():
    file=open("cars.csv","w", newline='')
    rec=csv.writer(file, delimiter=',')
    rec.writerow(['COMPANY','MODEL','PRICE'])
    rec.writerow(['Ferrari','F8','4,00,00,000'])
    rec.writerow(['McLaren','P1','11,00,00,000'])
    rec.writerow(['RollsRoyce','Phantom','10,00,00,000'])

def display():
    file=open("cars.csv","r")
    rec=csv.reader(file)
    for i in rec:
        print(i)

WriteToFile()
display()
