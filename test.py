def test(n):
  for i in range(n):
    print(i)
test(10)

def test_two(n):
  for i in range(n):
    for j in range(n):
      print(i,j)

test_two(3)