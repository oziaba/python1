#3
import string
def count_unique_codes(words):
    morse_base = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
    "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
    "..-","...-",".--","-..-","-.--","--.."]
    res = ''
    result = []
    alf = 'abcdefghijklmnopqrstuvwxyz'
    for word in words:
        for i in range(len(word)):
            for j in range(len(alf)):
                if word[i] == alf[j]:
                    res += morse_base[j]
        result.append(res)
        res = ''
    result = set(result)
    return len(result)
count_unique_codes(["gin", "zen", "gig", "msg"])