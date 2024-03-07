def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1

    return vowel_count

input_sentence = input("Enter a sentence: ")
num_vowels = count_vowels(input_sentence)
print("Number of vowels in the sentence:", num_vowels)
