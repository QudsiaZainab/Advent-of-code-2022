with open('6.txt') as file:
    dB = file.read()     #datastream buffer
    
#  task 1   
totChar = 3   
for i in range(len(dB)-4):
    SOPM = {dB[i],dB[i+1],dB[i+2],dB[i+3]}   #start of packet marker
    totChar += 1
    if len(SOPM) == 4:
        break
print(totChar)

# task 2
totChar = 13   
for i in range(len(dB)-14):
    SOMM = set()    #start of message marker
    for j in range(14):
        SOMM.add(dB[i+j])
    totChar += 1
    if len(SOMM) == 14:
        break
print(totChar)