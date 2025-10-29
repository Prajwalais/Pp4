numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0
odd_count = 0

# Count even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
