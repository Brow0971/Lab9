import csv
#Task1
with open('2000_BoysNames.txt', 'r') as fileB:
    boy1 = fileB.read()
    boy2 = boy1.splitlines()
    boy3 = [line.split(' ') for line in boy2 if line]

with open('2000_BoysNames.csv', "w") as csvFileB:
    writer = csv.writer(csvFileB)
    writer.writerow(['Names', 'Count'])
    writer.writerows(boy3)

with open('2000_GirlsNames.txt', 'r') as fileG:
    girl1 = fileG.read()
    girl2 = girl1.splitlines()
    girl3 = [line.split(' ') for line in girl2 if line]

with open('2000_GirlsNames.csv', "w") as csvFileG:
    writer = csv.writer(csvFileG)
    writer.writerow(['Names', 'Count'])
    writer.writerows(girl3)
