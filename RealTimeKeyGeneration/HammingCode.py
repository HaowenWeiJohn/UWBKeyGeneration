import numpy as np


# def hamming_code_generation(original_key, hamming_matrix):
#     multi_result = np.dot(original_key, hamming_matrix)
#
#     hamming_code = multi_result % 2
#
#     return hamming_code
#
#
# def error_position_matrix(receive_code, error_checking_matrix):
#     receive_code = np.array(receive_code)
#     code_transpose = np.transpose(receive_code)
#     error_position = np.dot(error_checking_matrix,code_transpose)
#
#     return error_position%2
#
#
# hamming_matrix = [
#
#     [1, 0, 0, 0, 0, 1, 1],
#     [0, 1, 0, 0, 1, 0, 1],
#     [0, 0, 1, 0, 1, 1, 0],
#     [0, 0, 0, 1, 1, 1, 1]
#
# ]
#
# error_checking_matrix = [
#     [0, 0, 0, 1, 1, 1, 1],
#     [0, 1, 1, 0, 0, 1, 1],
#     [1, 0, 1, 0, 1, 0, 1]
# ]
#
# original_key = [1, 1, 0, 1]
#
# one_error_hamming_code = [1, 1, 0, 1, 0, 0, 1]


class hamming_interface:

    def __init__(self, hamming_matrix, error_checking_matrix):

        self.hamming_matrix = hamming_matrix
        self.error_checking_matrix = error_checking_matrix

    def hamming_code_generation(self, original_key):
        multi_result = np.dot(original_key, self.hamming_matrix)

        hamming_code = multi_result % 2

        return hamming_code

    def error_position_matrix(self, hamming_code):
        receive_code = np.array(hamming_code)
        code_transpose = np.transpose(receive_code)
        error_position = np.dot(self.error_checking_matrix, code_transpose)

        return error_position % 2

    def error_correction(self, hamming_code, error_position_matrix):
        error_index = int("".join(str(x) for x in error_position_matrix), 2)

        if error_index == 0:
            return hamming_code
        else:
            # toggle that bit
            hamming_code[error_index - 1] = hamming_code[error_index - 1] ^ 1
            return hamming_code

