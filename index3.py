sum = int(input("Enter a number: "))
if sum > 1:
    for i in range(2, int(sum**0.5) + 1):
        if sum % i == 0:
            print(f"{sum} is not a prime number.")
            break
    else:
        print(f"{sum} is a prime number.")
else:
    print(f"{sum} is not a prime number.")