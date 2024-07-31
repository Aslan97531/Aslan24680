def single_root_words(root_word, *other_words):
    same_words = []
    word = root_word.lower()
    for i in other_words:
        a = i.lower()
        if word in a or a in word:
            same_words.append(i)
        else:
            continue

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)