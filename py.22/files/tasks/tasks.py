def censor(file):
    with open('forbidden_words.txt') as forbidden_file, open(file) as censor_file:
        pattern = forbidden_file.read().split()
        print(pattern)
        text = censor_file.read()
        print(text)
        text_lower = text.lower()

        print(list(zip(text_lower, text)))

        result = ''.join([y, x][x == '*'] for x, y in zip(text_lower, text))
        print()
        print(result)




        # for word in pattern:
            
        #     text_lower = text_lower.replace(word, "*" * len(word))
        # print(text_lower)
        # result = ''
        # i = 0
        # for x in text_lower:
        #     if x == '*':
        #         result += x
        #     else:
        #         result += text[i]
        #     i += 1
        # print()
        # print(result)

censor('input.txt')