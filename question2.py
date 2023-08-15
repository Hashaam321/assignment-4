import string

def word_frequency(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

def display_word_frequencies(word_freq):
    print("Word Frequencies:")
    for word, frequency in word_freq.items():
        print(f"{word}: {frequency}")

def main():
    user_input = input("Enter a text: ")
    frequencies = word_frequency(user_input)
    display_word_frequencies(frequencies)

if __name__ == "__main__":
    main()

