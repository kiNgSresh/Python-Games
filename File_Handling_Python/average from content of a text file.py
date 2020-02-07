fname = input('Enter the file name\n')
handle = open(fname,'r')
num = 0
sum = 0
countl = 0
count = 0
for line in handle:
    if line.startswith('X-DSPAM-Confidence:'):
        countl= len(line)
        num = line[countl-7:countl]
        num = float(num)
        sum = sum + num
        count = count +1
print ('Average spam confidence:', sum/count)
