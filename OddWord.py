def solution(s):
    answer = ''
    words = s.split(" ")
    new_words = []
    for word in  words:
        temp = ''
        for i in range(len(word)):
            if i % 2 == 0:
                temp += word[i].upper()
            else:
                temp += word[i].lower()
        new_words.append(temp)
        answer = " ".join(new_words)
    return answer

print(solution("this is sparta  !! roma"))