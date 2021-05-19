import nltk
from nltk.tokenize import WordPunctTokenizer
nltk.download('stopwords')

# 영어 불용어
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
tknzr = WordPunctTokenizer()

# stem(어간 찾는 친구)
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

text = '''The European languages are members of the same family.
        Many words in a language translate into familiar words in another.
        '''

# 토큰화 시키기
words = tknzr.tokenize(text)
print(words)

# 불용어에 없는 단어들 소문자로 치환
words_clean = [w.lower() for w in words if w not in stopwords]
print(words_clean)

# 어간으로 변환
words_clean_stem = [stemmer.stem(w) for w in words_clean]
print(words_clean_stem)
