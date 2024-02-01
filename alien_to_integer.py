# Declared Function
def alien_to_integer(s):

    # Init variables
    roman_to_int_mapping = {'A': 1, 'B': 5, 'Z': 10, 'L': 50, 'C': 100, 'D': 500, 'R': 1000}
    result = 0
    prev_value = 0

    # Loop char in s
    for char in reversed(s):

        # Get current number
        current_value = roman_to_int_mapping[char]

        # Condition
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value

        # keep prev_value for compare next value
        prev_value = current_value

    return result

# Example Usage:
print(alien_to_integer("AAA"))      # Output: 3
print(alien_to_integer("LBAAA"))    # Output: 58
print(alien_to_integer("RCRZCAB"))  # Output: 1994
