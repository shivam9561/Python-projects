import time
import matplotlib.pyplot as plt
import random

# Algorithm

def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return time.process_time()


data = [-2, 45, 0, 11, -9]

bubbleSort(data)
data

N = []
for i in range(2,4*100,4):
    N.append(i)

#Worst case, Avg Case, Best Case
def cases(N):
  wct = []
  bct = []
  act = []
  for i in N:
    # Worst Case
    w = []
    a = []
    b = []
    for j in range(i,0,-1):
      w.append(j)
    wct.append(bubbleSort(w))

    # Best Case
    for j in range(1,j+1):
      b.append(j)
    bct.append(bubbleSort(b))

    # Avg Case
    for j in range(0,i):
      a.append(random.randrange(1,100))
    act.append(bubbleSort(a))

  return wct,bct,act

#Ploting

wt,bt,at = cases(N)
plt.plot(N,wt)
plt.plot(N,bt)
plt.plot(N,at)
plt.show()
