print("This program converts an integer to a Roman numeral.")s

# Defining a class to convert integers to Roman numerals
class RomanConverter:
    # Function to convert an integer to a Roman numeral
    def int_to_roman(self, num):
        # List of integer values in descending order
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        # List of Roman numeral symbols corresponding to the above values
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        roman_num = ""   # This will store the final Roman numeral string after conversion
        i = 0            # it is to go through val[] and syms[] together

        # Continue looping until the number is fully converted (num becomes 0)
        while num > 0:
            # Checks how many times the current value fits into num
            for _ in range(num // val[i]):
                roman_num += syms[i]   # Add the Roman symbol to the result
                num -= val[i]          # Subtract that value from num
            # Move to the next (smaller) value/symbol pair
            i += 1

        # Return the complete Roman numeral string
        return roman_num


# Asks the user to enter an integer
number = int(input("Enter an integer (1 - 3999): "))

# Creates an instance of the RomanConverter class, so uses all the above code
converter = RomanConverter()

# finally calls upon the int_to_roman function and prints the result
print("Roman numeral:", converter.int_to_roman(number))
