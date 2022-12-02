# Selection sort in Python
import time
import matplotlib.pyplot as plt
import random


def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
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
      size1 = len(w)
    wct.append(selectionSort(w,size1))

    # Best Case
    for j in range(1,j+1):
      b.append(j)
      size2 = len(b)
    bct.append(selectionSort(b,size2))

    # Avg Case
    for j in range(0,i):
      a.append(random.randrange(1,100))
      size3 = len(a)
    act.append(selectionSort(a,size3))

  return wct,bct,act

#Ploting
wt,bt,at = cases(N)
plt.plot(N,wt)
plt.plot(N,bt)
plt.plot(N,at)
plt.show()
