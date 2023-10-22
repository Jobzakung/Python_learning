import base64


def encode(input_str):
    # Encode to hexadecimal
    hex_encoded = input_str.encode("utf-8").hex()

    # Convert hexadecimal to binary
    binary_encoded = bin(int(hex_encoded, 16))[2:]

    formatted_binary_number = f'0{binary_encoded}'

    # Split binary into 4-bit and 6-bit groups
    split_4_bits = [
        f'{formatted_binary_number[i:i + 4]:0<4}' for i in range(0, len(formatted_binary_number), 4)]

    split_6_bits = [
        f'{formatted_binary_number[i:i + 6]:0<6}' for i in range(0, len(formatted_binary_number), 6)]

    # Ensure the last binary string has 6 bits
    decimal_numbers = [int(binary, 2) for binary in split_6_bits]

    # Convert binary to decimal
    binary_to_decimal = int(binary_encoded, 2)

    # Encode the input string to base64
    base64_encoded = base64.b64encode(
        input_str.encode("utf-8")).decode("utf-8")

    print("Input: ", input_str)
    print("Hexadecimal Encoding: ", hex_encoded)
    print("Split Binary (4 bits): ", split_4_bits)
    print("Split Binary (6 bits): ", split_6_bits)
    print("Binary to Decimal 6bit : ", decimal_numbers)
    print("Binary to Decimal: ", binary_to_decimal)
    print("Base64 Encoding: ", base64_encoded)


def decode():
    input_string = "VUhsMSNHOXVJRTlUVXk0PQ"
    padding = 4 - (len(input_string) % 4)
    input_string += '=' * padding
    print("before converted : ", base64.b64decode(input_string))


encode('SuKiRd O.')
