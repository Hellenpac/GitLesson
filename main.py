# main.py

#import math_utils
#import string_utils
from utils import math_utils
from utils import string_utils

def main():
    # --- Using math_utils ---
    print("Math Utils Examples:")
    print("5 + 3 =", math_utils.add(5, 3))
    print("10 - 4 =", math_utils.subtract(10, 4))
    print("6 * 7 =", math_utils.multiply(6, 7))
    print("20 / 5 =", math_utils.divide(20, 5))

    # --- Using string_utils ---
    print("\nString Utils Examples:")
    text = "Hello, World!"
    print(f"Original: {text}")
    print("Vowel Count:", string_utils.count_vowels(text))
    print("Without punctuation:", string_utils.remove_punctuation(text))
    print("Reversed:", string_utils.reverse_string(text))

if __name__ == "__main__":
    main()
