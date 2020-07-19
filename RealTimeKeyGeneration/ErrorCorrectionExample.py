import numpy as np
from RealTimeKeyGeneration.HammingCode import hamming_interface

G = [

    [1, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1]

]


H = [
    [0, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1]
]

original_key = [1, 1, 0, 1]

error_key = [1, 1, 0, 0]

one_error_hamming_code = [1, 1, 0, 0, 0, 0, 1]

hamming_interface = hamming_interface(hamming_matrix=G, error_checking_matrix=H)

if __name__ == '__main__':

    hamming_code = hamming_interface.hamming_code_generation(original_key)
    print("Generate hamming code: ")
    print(hamming_code)

    error_position_matrix = hamming_interface.error_position_matrix(one_error_hamming_code)
    print(error_position_matrix)

    code_after_correction = hamming_interface.error_correction(one_error_hamming_code, error_position_matrix)
    print(code_after_correction)

