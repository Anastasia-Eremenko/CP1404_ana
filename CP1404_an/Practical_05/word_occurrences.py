"""
CP1404 Practical
Word Occurrences
Estimate: 30 minutes
Actual: 20 minutes
"""


def main():
    """A program that counts the number of appearances of each word in a sentence"""
    message = input("Write your string here>>> ")
    words = message.strip().split(" ")
    words.sort()
    word_to_count = count_same_words(words)
    longest_word = find_longest_word(words)
    display_words(word_to_count, longest_word)


def display_words(word_to_count, longest_word):
    """Formats and displays the words and corresponding counts"""
    for word, count in word_to_count.items():
        print(f"{word:<{longest_word + 1}} : {count}")


def count_same_words(words):
    """Counts the number of times each word appears via a dictionary"""
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1
    return word_to_count


def find_longest_word(words):
    """Finds the length of the longest word"""
    longest_word = 0
    for word in words:
        if len(word) > longest_word:
            longest_word = len(word)
    return int(longest_word)


main()
