#Boys Caloriimeter
#Principle: principle involved in this method is to burn the gas at a known
#constant rate in a vessel under such conditions that the entire amount of heat
#produced is absorbed by water which is also flowing at a constant rate.

W = float(input("Weight of water passed in time t \n"))
V = float(input("Volume of gas burnt at STP in time t \n"))
t1 = float(input("Temperature of the incomiing water \n"))
t2 = float(input('Temperature of the outgoing water \n'))
m = float(input("Weight of steam condensed in time t \n"))
GCV = (W*(t2-t1))/V
NCV = GCV - ((m*587))/V
print("GCV is:",GCV,"\n")
print("NCV is", NCV)


