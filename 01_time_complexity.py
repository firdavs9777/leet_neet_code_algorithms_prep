def test(n):
  for i in range(n):
    print(i)
test(10) ## Loop runs(n times)
def test_two(n):
  for i in range(n):
    for j in range(n):
      print(i,j)

test_two(3) # Look runs (n*n = n^2 times)

def add_items(n):
  return n + n + n #O(1) constant number of operations 

# Different terms for input
def print_items(a,b):
  for i in range(a):
    print(i)
  for j in range(b):
    print(j)
    ## O(a+b)

def print_items(a,b):
  for i in range(a):
    for j in range(b):
      print(i,j)
    ## O(a*b)

def cubic(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
                # O(n*n*n) = O(n^3)


        
