#Dulongs formula


c = float(input("Enter Carbon % \n "))
h = float(input("Enter Hydrogen % \n"))
s = float(input("Enter Sulphur % \n"))
o = float(input("Enter oxygen % \n"))

GCV = ((8080*c)+(34500*(h-(o/8)))+ (2240*s))/100

print(GCV,'\n')


NCV= GCV - (9*h*587)/100

print(NCV)


