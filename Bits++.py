def execute_bit_program(n, program):
    x = 0  # Initial value of x

    for statement in program:
        if "++" in statement:
            x += 1
        elif "--" in statement:
            x -= 1

    return x

# Input
n = int(input().strip())
program = [input().strip() for _ in range(n)]

# Output
result = execute_bit_program(n, program)
print(result)
