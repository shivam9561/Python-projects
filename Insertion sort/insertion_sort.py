import time
import matplotlib.pyplot as plt
import random


def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key
    return time.process_time()
  
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

    wct.append(insertionSort(w))

    # Best Case
    for j in range(1,j+1):
      b.append(j)

    bct.append(insertionSort(b))

    # Avg Case
    for j in range(0,i):
      a.append(random.randrange(1,100))

    act.append(insertionSort(a))

  return wct,bct,act



#Ploting
wt,bt,at = cases(N)
plt.plot(N,wt)
plt.plot(N,bt)
plt.plot(N,at)
plt.show()
