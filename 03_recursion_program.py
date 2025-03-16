def sumFirst(n):
    return n * (n + 1) // 2
def main():
    x  = int(input("Please enter a non-negative integer:  "))
    s = sumFirst(x)
    print("The sum of the first ",x, "integer is", str(s) + ".")

if __name__ == "__main__":
    main()

