import itertools
import operator

unknown_token = "UNKNOWN_TOKEN"
word_freq = nltk.FreqDist(itertools.chain(*input_x))
sorted_word_freq = sorted(word_freq.items(), key = operator.itemgetter(1))
vocab = word_freq.most_common(vocab_size-1)