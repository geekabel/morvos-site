# import base64

# def xor_with_byte(encoded_bytes, xor_byte):
#     return bytes([b ^ xor_byte for b in encoded_bytes])

# def decode_base64(encoded_string):
#     return base64.b64decode(encoded_string)

# # encoded_string = "IConIT0+KTQZNjMyNRkyLiMZIDMoGS8oGSAzKCInKyMoMicqOw=="
# encoded_string = "IAUPA1sVCjQ2HhFUHjoyAQs7UBgLGQAAO1AYCxkLDxdFCTogBQ8DXQ=="
# decoded_bytes = decode_base64(encoded_string)

# for xor_byte in range(256):
#     result = xor_with_byte(decoded_bytes, xor_byte)
#     print(f"XOR with 0x{xor_byte:02X}: {result}")



import base64

def xor_decrypt(key, data):
    return bytes([a ^ b for a, b in zip(key, data)])

def is_flag_format(text):
    return text.startswith(b'flag{') and text.endswith(b'}')

def brute_force_decrypt(data, key_length):
    for i in range(256 ** key_length):
        key = i.to_bytes(key_length, 'big')
        decrypted_data = xor_decrypt(key, data)
        if is_flag_format(decrypted_data):
            return decrypted_data.decode()

encoded_bytes = "IAUPA1sVCjQ2HhFUHjoyAQs7UBgLGQAAO1AYCxkLDxdFCTogBQ8DXQ=="
decoded_bytes = base64.b64decode(encoded_bytes)

# Brute-force attack with a key length of 7 characters
flag = brute_force_decrypt(decoded_bytes, 7)

print("Decrypted flag:", flag)


