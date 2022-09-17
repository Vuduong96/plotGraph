
import matplotlib.pyplot as plt
import re
import numpy as np


list_acc = []
comm_rnd = []
count = 0
with open("ditto_cifar10.txt", "r") as f:
    s = f.readlines()
    # print(s)
    for x in s:
        
        if x.__contains__("test_acc"):
            count = count + 1
            comm_rnd.append(count)

            print('Round: ',count)
            start = x.find("{'test_acc': ")
            end = x.find(",")
            substring = x[start:end] + " } "

            # extract number from text
            accuracy = re.findall(r"\d+\.\d+", substring)
            x = str(accuracy).strip("[]'")
            list_acc.append(x)

            #substring += x[start:end]
            print(x)
    f.close()

# Plot a Line chart in Python using Matplotlib

list_float = []

for item in list_acc:
    rnd = round(float(item), 2)
    list_float.append(rnd)

x = comm_rnd
y = np.array(list_float)

plt.plot(x,y)
plt.title('Cifar 10 - ditto')
plt.xlabel('Round')
plt.ylabel('Accuracy')
#plt.show()
plt.savefig('ditto_cifar10.png')