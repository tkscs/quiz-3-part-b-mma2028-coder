
def check_palindrome(i):
    if i ==i[::-1]:
        return True
    else:
        return False

print(check_palindrome("bob"))