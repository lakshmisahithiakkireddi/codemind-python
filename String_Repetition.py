def count_a_in_infinite_string(s, n):
    # Step 1: Count occurrences of 'a' in the given string
    a_count_in_s = s.count('a')

    # Step 2: Find the number of complete repetitions of the string 's' in the first 'n' characters
    complete_repetitions = n // len(s)

    # Step 3: Calculate the remaining characters after complete repetitions
    remaining_characters = n % len(s)

    # Step 4: Count occurrences of 'a' in the remaining characters
    a_count_in_remaining = s[:remaining_characters].count('a')

    # Calculate total count of 'a' in the first 'n' characters
    total_a_count = (complete_repetitions * a_count_in_s) + a_count_in_remaining

    return total_a_count

# Sample Input
s = input().strip()
n = int(input().strip())

# Sample Output
result = count_a_in_infinite_string(s, n)
print(result)
