# Reference alphabets to handle logic without character codes (ord/chr)
ALPHABET_CLEAN = "abcdefghjkmnpqrstuvwxyz"  # Excludes i, o, l
ALPHABET_FULL = "abcdefghijklmnopqrstuvwxyz" # Used to check for straights

def get_next_char(char):
    # Finds the current letter in the restricted alphabet and returns the next one.
    # If the letter is 'z', it returns 'a' and signals a 'carry' to the next position.
    idx = ALPHABET_CLEAN.find(char)
    if idx == -1 or idx == len(ALPHABET_CLEAN) - 1:
        return ALPHABET_CLEAN[0], True
    return ALPHABET_CLEAN[idx + 1], False

def increment_recursive(s):
    # Mimics manual counting by updating the last character of the string.
    # If a carry occurs, it recursively calls itself to update the character to the left.
    if not s:
        return ""
    new_char, carry = get_next_char(s[-1])
    if carry:
        return increment_recursive(s[:-1]) + new_char
    return s[:-1] + new_char

def has_straight(s):
    # Checks if any 3-character slice of the password exists within the full alphabet.
    # This replaces the need for mathematical comparisons like (x + 1 == y).
    for i in range(len(s) - 2):
        if s[i:i+3] in ALPHABET_FULL:
            return True
    return False

def has_two_pairs(s):
    # Scans the string for two distinct, non-overlapping pairs (like 'aa' and 'cc').
    # It uses a counter and index jumping to ensure pairs don't overlap (like 'aaa').
    count, i = 0, 0
    found_chars = ""
    while i < len(s) - 1:
        if s[i] == s[i+1] and s[i] not in found_chars:
            count += 1
            found_chars += s[i]
            i += 2 # Jump past the pair
        else:
            i += 1
    return count >= 2

def find_next(pwd):
    # The main loop: increments the password string until both the
    # 'straight' and 'two-pairs' requirements are satisfied.
    while True:
        pwd = increment_recursive(pwd)
        if has_straight(pwd) and has_two_pairs(pwd):
            return pwd

# Initial Input
current_pwd = "hxbxxyzz"
result = find_next(current_pwd)
print(f"The next password is: {result}")