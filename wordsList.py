import random


def get_random_word():
    return random.choice(words_list)


words_list = ['step', 'such', 'made', 'young', 'science', 'dog', 'right', 'bed', 'stay', 'than',
              'word', 'apple', 'people', 'state', 'when', 'must', 'mile', 'paint', 'correct', 'five', 'teach', 'for',
              'he', 'found', 'vowel', 'in', 'show', 'begin', 'day', 'list', 'time', 'rain', 'train', 'hundred', 'dark',
              'main', 'firstly', 'think', 'whole', 'thousand', 'world', 'fast', 'only', 'hold', 'miss', 'friend',
              'sleep', 'too', 'food', 'yet', 'came', 'dark', 'both', 'miss', 'mark', 'at', 'oh', 'box', 'thought', 'is',
              'said', 'my', 'course', 'since', 'slow', 'much', 'always', 'usually', 'often', 'ship', 'yes', 'no',
              'begin', 'ease', 'them', 'they', 'her', 'his', 'cat']

random_words_list = []
for _ in words_list:
    random_words_list.append(random.choice(words_list))
print(random_words_list)

