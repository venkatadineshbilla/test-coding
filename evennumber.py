# Program to print numbers between two given numbers

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Numbers between {start} and {end} are:")

for i in range(start, end + 1):   # +1 to include the ending number
    print(i, end=" ")
