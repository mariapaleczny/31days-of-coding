def is_palindrome(word: str) -> bool:
    return word.lower() == word[::-1].lower()


print(is_palindrome("kajak"), is_palindrome("kaja"))
