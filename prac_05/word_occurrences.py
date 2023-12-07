"""Word Occurrences"""
word_to_count = {}
text = input("Text: ")
words = text.split(" ")
# print(words)
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
# print(word_to_count)
words = list(word_to_count.keys())
words.sort()
maximum_word_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{maximum_word_length+1}}: {word_to_count[word]}")

