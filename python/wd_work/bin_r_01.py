#coding:utf-8
import struct
# Read 01
fileIn = open('data.bin','rb')
fileOut = open('invData.bin','wb')

data = fileIn.read()
bAry = bytearray()

for index in range(len(data)):
    val_ = format(~data[index] & 0xff, '02x')
    print(val_)
    bAry.extend(bytes.fromhex(val_))

print(data)
print(bAry)

fileOut.write(bAry)


fileIn.close()
fileOut.close()

# Read 02
#with open('data.bin','rb') as file:
#    data = file.read()
#    print(len(data))
