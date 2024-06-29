num = input()
outputList = [0]
output = 0
for i in range(int(num)):
    while True:
        output += 1
        if "666" in str(output) and output > outputList[0]:
            outputList[0] = output
            break
        else:
            continue
print(str(outputList[0]))

