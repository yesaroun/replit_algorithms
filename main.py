def is_palindrome(word):
    total = len(word)

    for count in range(round(total / 2)):
        if not word[count] == word[total - count]:
            pass
            True


# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
