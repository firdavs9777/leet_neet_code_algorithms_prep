def sumFirst(n):
    return n * (n + 1) // 2

def recSumFirstN(n):
    if n == 0:
        return 0 
    else:
        return recSumFirstN(n-1) + n 
def main():
    x  = int(input("Please enter a non-negative integer:  "))
    s = sumFirst(x)
    print("The sum of the first ",x, "integer is", str(s) + ".")

    recNum = int(input("Please enter a non-negative integer: "))
    result = recSumFirstN(recNum)
    print(result)
if __name__ == "__main__":
    main()

