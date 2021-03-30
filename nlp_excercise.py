from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from pathlib import Path
from operator import itemgetter
from pathlib import Path
import imageio
from wordcloud import WordCloud
import matplotlib.pyplot as plt


john_blob = TextBlob(Path("book of John text.txt").read_text())

stop = stopwords.words("english")
extra_stops = [
    "thy",
    "ye",
    "verily",
    "thee",
    "hath",
    "say",
    "thou",
    "art",
    "shall",
    "unto",
]
stop += extra_stops


items = john_blob.word_counts.items()


items = [item for item in items if item[0] not in stop and item[0] in john_blob.noun_phrases]

top_sorted = sorted(items, key=itemgetter(1), reverse=True)

top15 = top_sorted[:15]

wordcloud = WordCloud(colormap="prism", background_color="black")
wordcloud = wordcloud.generate(str(top15))

wordcloud = wordcloud.to_file("JohnText.png")

plt.imshow(wordcloud)
