# Task 1

def analyze_scores(scores):
    # Return a dictionary with min, max, average, and passed count
    pass


# Task 2

def count_words(sentence):
    # Return a dictionary with word frequency (case-insensitive)
    pass


def top_n_words(freq_dict, n=3):
    # Return a list of tuples sorted by frequency in descending order
    pass


if __name__ == "__main__":
    sample_scores = [55, 72, 90, 41, 66, 78, 84, 59]
    summary = analyze_scores(sample_scores)
    print("Score summary:", summary)

    sample_sentence = "Python is fun and python is powerful and fun"
    frequencies = count_words(sample_sentence)
    print("Word frequencies:", frequencies)
    print("Top 3:", top_n_words(frequencies, 3))
