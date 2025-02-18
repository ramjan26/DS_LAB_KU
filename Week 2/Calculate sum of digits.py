import string
def is_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Output: True
