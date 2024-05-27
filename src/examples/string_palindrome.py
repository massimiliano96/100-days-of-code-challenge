# Two-Pointer approach to determine if a string is a Palindrome


def is_palindrom(random_s):
    left = 0
    right = len(random_s) - 1

    while left <= right:
        if random_s[left] != random_s[right]:
            return False
        left = left + 1
        right = right - 1

    return True
