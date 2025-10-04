def is_palindrome(s):
    print(s.lower())
    print(s[::-1].lower())
    return s.lower() == reversed(s.lower())
​