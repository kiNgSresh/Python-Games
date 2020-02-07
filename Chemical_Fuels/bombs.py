x = float(input("Mass of fuel used \n"))
W = float(input("Mass of water \n"))
w = float(input('water equi. \n'))
t1 = float(input("temp1 \n"))
t2 = float(input("temp2 "))
tc = float(input("cold \n"))
ta = float(input("acid \n"))
tf = float(input("fuse \n"))
tt = float(input('cotton \n'))
h = float(input("Hydrogen"))
GCV = (((w +W)*(t1-t2+tc))-(ta+tt+tf))/x
print(GCV,'\n')
NCV = GCV -(9*h*587)/100
print(NCV)


