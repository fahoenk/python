from PyQt6.QtWidgets import *
from gui import *

dict_upper_alphabet = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9,
                 "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18,
                 "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}

dict_lower_alphabet = {"a":26, "b":27, "c":28, "d":29, "e":30, "f":31, "g":32, "h":33, "i":34, "j":35,
                 "k":36, "l":37, "m":38, "n":39, "o":40, "p":41, "q":42, "r":43, "s":44,
                 "t":45, "u":46, "v":47, "w":48, "x":49, "y":50, "z":51}

def encrypt_in_place(str_list: list, k: int)->list:
    """
    Encrypts list in place
    :param str_list: list of only letters and space characters
    :param k: shift value
    :return: encrypted list
    """
    new_str_list = []

    for letter in str_list:
        if letter == " ":
            new_str_list.append(" ")

        elif letter in dict_upper_alphabet.keys():
            num = dict_upper_alphabet[letter]
            new_num = (num + k) % 26

            for key, value in dict_upper_alphabet.items():
                if new_num == value:
                    new_letter = key
                    new_str_list.append(new_letter)

        elif letter in dict_lower_alphabet.keys():
            num = dict_lower_alphabet[letter]
            new_num = (num + k) % 52

            if new_num < 26:
                new_num += 26

            for key, value in dict_lower_alphabet.items():
                if new_num == value:
                    new_letter = key
                    new_str_list.append(new_letter)

        else:
            new_str_list.append(letter)

    return new_str_list


def decrypt_in_place(user_str_list: list, k: int)->list:
    """
    Decrypt list of letters and spaces only
    :param user_str_list: user's list to be decrypted
    :param k: shift amount
    :return: decrypted list (according to value k)
    """
    new_str_list = []

    for letter in user_str_list:
        if letter == " ":
            new_str_list.append(" ")

        elif letter in dict_upper_alphabet.keys():
            num = dict_upper_alphabet[letter]
            new_num = (num - k) % 26

            for key, value in dict_upper_alphabet.items():
                if new_num == value:
                    new_letter = key
                    new_str_list.append(new_letter)

        elif letter in dict_lower_alphabet.keys():
            num = dict_lower_alphabet[letter]
            new_num = num - k

            if new_num < 26:
                new_num += 26

            for key, value in dict_lower_alphabet.items():
                if new_num == value:
                    new_letter = key
                    new_str_list.append(new_letter)

        else:
            new_str_list.append(letter)

    return  new_str_list


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.radio_encrypt.setChecked(True)
        self.slider_shift.valueChanged.connect(lambda: self.run_program())

    def run_program(self):
        try:

            if self.radio_encrypt.isChecked():
                k = self.slider_shift.value()
                user_message = self.input_plain.toPlainText()
                user_str_list = list(user_message)

                enc_str_list = encrypt_in_place(user_str_list, k)

                new_string = "".join(enc_str_list)
                self.input_cipher.setText(new_string)

            elif self.radio_decrypt.isChecked():
                k = self.slider_shift.value()
                user_message = self.input_cipher.toPlainText()
                user_str_list = list(user_message)

                dec_str_list = decrypt_in_place(user_str_list, k)

                new_string = "".join(dec_str_list)
                self.input_plain.setText(new_string)

        except ValueError:
             self.label_error.setText("uh oh ValueError")

        except:
             self.label_error.setText("uh oh you broke me")


#pyuic6 gui.ui -o gui.py

# test_list = ["A", "B", "C", "D", "a", "b", "c", "d"]
# test_list2 = ["H", "E", "L", "L", "O", ' ', 'h', 'e', 'l', 'l', 'o']
# test_list3 = ["E", "B", "I", "I", "L", " ", "e", 'b', 'i', 'i', 'l']
#
# print(encrypt_in_place(test_list2, 23))
# print(decrypt_in_place(test_list3, 23))


# letter_list = ["A", "B", "C", "D", "E", "F", "G"]
# number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# nums_list = letters_to_numbers(letter_list)
# let_list = numbers_to_letters(number_list)
# encrypted = encrypt(number_list, 14)
# encrypted_nums = letters_to_numbers(encrypted)
# decrypted = decrypt(encrypted_nums, 14)
# print(nums_list)
# print(let_list)
# print(encrypted)
# print(decrypted)

# def letters_to_numbers(user_list):
#     new_list = []
#     for letter in user_list:
#         if letter == " ":
#             new_list.append(" ")
#         elif letter in dict_upper_alphabet.keys():
#             for key, value in dict_upper_alphabet.items():
#                 if letter == key:
#                     new_list.append(value)
#         else:
#             raise ValueError
#
#     return new_list

# def numbers_to_letters(user_list):
#     new_list = []
#     for number in user_list:
#         if number == " ":
#             new_list.append(" ")
#         else:
#             for key,value in dict_upper_alphabet.items():
#                 if number == value:
#                     new_list.append(key)
#     return  new_list

# def encrypt(num_list, k):
#     encrypt_list = []
#     for number in num_list:
#         if number == " ":
#             encrypt_list.append(" ")
#         else:
#             new_num = (number + k) % 26
#             encrypt_list.append(new_num)
#
#     final_list = numbers_to_letters(encrypt_list)
#     return final_list

# def decrypt(num_list, k):
#     decrypt_list = []
#     for number in num_list:
#         if number == " ":
#             decrypt_list.append(" ")
#         else:
#             new_num = (number - k) % 26
#             decrypt_list.append(new_num)
#
#     final_list = numbers_to_letters(decrypt_list)
#     return final_list