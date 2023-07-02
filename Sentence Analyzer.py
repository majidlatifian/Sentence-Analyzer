sentence = input()
sentence_list = sentence.split('.')

modified_sentence = sentence.replace('.', '')
words = modified_sentence.split()

result_list = []

for i in range(len(sentence_list)):
    word_list = sentence_list[i].split()[1:]
    for word in word_list:
        if word[0].isupper():
            for j in range(len(words)):
                if word == words[j]:
                    result_list.append((str(j + 1), word))
                    words[j] = '!'
                    break

if len(result_list) > 0:
    for item in result_list:
        print(':'.join(item))
else:
    print('None')
