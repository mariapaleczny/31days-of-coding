def is_anagram(word1: str, word2: str) -> bool:
    if sorted(word1.lower()) == sorted(word2.lower()):
        return True
    else:
        return False


print(is_anagram("The Morse code", "Here come dots"), is_anagram("nie", "tak"))