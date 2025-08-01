from pkg1 import pattern,prime,armstrong,Fibo

pattern(int(input("\nEnter number of lines for pattern --> ")))

num = int(input("Enter a number to check prime or non-prime -->"))
if prime(num):
    print(f"{num} is Prime")
else:
    print(f"{num} is Non-Prime")

n1 = int(input("Enter the number to check armstong or not --> "))
if armstrong(n1):
    print(f"{n1} is ArmStrong!!")
else:
    print(f"{n1} is Common!!")
