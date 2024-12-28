import struct

def float_to_bin(num):
    # Convert float to binary string using IEEE 754 format
    packed = struct.pack('>f', num)  # Big-endian single precision
    return ''.join(f'{byte:08b}' for byte in packed)

def double_to_bin(num):
    # Convert double to binary string using IEEE 754 format
    packed = struct.pack('>d', num)  # Big-endian double precision
    return ''.join(f'{byte:08b}' for byte in packed)

def number_to_bases(num):
    # Checking if the input is a floating-point number
    if isinstance(num, float):
        # For float (single precision)
        binary = float_to_bin(num)
        hex_value = format(struct.unpack('!I', struct.pack('!f', num))[0], 'x')
        octal = oct(struct.unpack('!I', struct.pack('!f', num))[0])
        
        return binary, hex_value, octal
    else:
        # If the input number is not recognized
        return "Please enter a valid float number."

# Get user input
user_input = float(input("Enter a float number: "))

# Get the binary, hexadecimal, and octal representations
binary, hex_value, octal = number_to_bases(user_input)

# Print the results
print(f"Binary: {binary}")
print(f"Hexadecimal: {hex_value}")
print(f"Octal: {octal}")
