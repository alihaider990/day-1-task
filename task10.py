def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word
print(find_longest_word(" I am driving the at the speed of 270 km/h"))








