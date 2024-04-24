class Neon(MagicalPrimeChecker):
    def is_neon(n):
        square = n * n
        digit_sum = sum(int(digit) for digit in str(square))
        return digit_sum == n

# Example usage:
num = int(input("Enter a number to check if it's a neon number: "))
if is_neon(num):
    print(num, "is a neon number.")
else:
    print(num, "is not a neon number.")
