from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

# print(blob)

# print(blob.sentences)

# print(blob.words)


# print(blob.tags)

# print(blob.noun_phrases)

# print(blob.sentiment)


# print(round(blob.sentiment.polarity, 3))


# print(round(blob.sentiment.subjectivity, 3))


# sentences = blob.sentences

# for sentence in sentences:
#     print(sentence)
#     print(sentence.sentiment)
#     print(round(sentence.sentiment.polarity, 3))


# from textblob.sentiments import NaiveBayesAnalyzer

# blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

# print(blob.sentiment)

# for sentence in blob.sentences:
#     print(sentence.sentiment)

# Detect the language of the text

# print(blob.detect_language())

# japanese = blob.translate(to="ja")
# print(japanese)


# index = Word("index")

# print(index.pluralize())

# cacti = Word("cacti")

# print(cacti.singularize())

# animals = TextBlob("dog cat fish bird").words

# print(animals.pluralize())

# word = Word("theyr")

# print(word.spellcheck())

# corrected_word = word.correct()

# sentence = TextBlob("Ths sentenze hsa misspelled wordsa.")

# corrected_sentence = sentence.correct()

# print(corrected_word)
# print(corrected_sentence)

# Stemming algorithms work by cutting off the end or beginning of the word, taking
# Common prefixes and suffixes that can be found in an inflected word

# Varieties = would be variety
# Studies = would be studi

# Lemmatization, on the other hand, takes into consideration the morphologival analysis of the words

# Varieties = would be variety
# studies = would be study


from textblob import Word

word1 = Word("studies")
word2 = Word("varieties")

# print(word1.lemmatize())
# print(word2.lemmatize())

happy = Word("happy")

# print(happy.definitions)
"""
for synset in happy.synsets:
    print(synset)
    for lemma in synset.lemmas():
        print(lemma)
        # print(lemma.name())
lemmas = happy.synsets[0].lemmas()
for lemma in lemmas[0].antonyms():
    print(lemma.name())
"""
import nltk

# nltk.download("stopwords")

from nltk.corpus import stopwords

stops = stopwords.words("english")
blob = TextBlob("Toda is a beautiful day")


# print(blob.words)
# print(stops)

stop_words_removed = [i for i in blob.words if i not in stops]

print(stop_words_removed)