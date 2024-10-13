# Function to check if the number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# Function to reverse the digits of a number
def reverse_digits(num):
    reversed_num = int(str(num)[::-1])
    print(f"Reversed number: {reversed_num}")

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to display all prime numbers up to a given limit
def prime_numbers(limit):
    primes = [i for i in range(2, limit + 1) if is_prime(i)]
    print(f"Prime numbers up to {limit}: {primes}")

# Function to calculate the factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Function to sum the digits of a number
def sum_of_digits(num):
    sum_digits = sum(int(digit) for digit in str(num))
    print(f"Sum of digits: {sum_digits}")

# Function to display the menu and perform the required operations
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Check Even or Odd")
        print("2. Reverse Digits of a Number")
        print("3. Find Prime Numbers up to a Limit")
        print("4. Factorial of a Number")
        print("5. Sum of Digits of a Number")
        print("6. Exit")
        
        choice = int(input("Enter your choice (1-6): "))
        
        if choice == 1:
            num = int(input("Enter a number: "))
            check_even_odd(num)
        
        elif choice == 2:
            num = int(input("Enter a Number: "))
            reverse_digits(num)
        
        elif choice == 3:
            limit = int(input("Enter the upper limit: "))
            prime_numbers(limit)
        
        elif choice == 4:
            num = int(input("Enter a number: "))
            print(f"Factorial of {num} is {factorial(num)}")
        
        elif choice == 5:
            num = int(input("Enter a number: "))
            sum_of_digits(num)
        
        elif choice == 6:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

# Start the program
if __name__ == "_main_":
    menu()