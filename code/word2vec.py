import gensim
import codecs
from smart_open import open

class MySentences(object):
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        for line in open(self.filename, mode='r', encoding='utf-8'):
            yield line.split()


def main(domain):
    source = '../preprocessed_data/%s/train.txt' % (domain)
    model_file = '../preprocessed_data/%s/w2v_embedding' % (domain)
    sentences = MySentences(source)
    model = gensim.models.Word2Vec(sentences, size=200, window=5, min_count=10, workers=4)
    model.save(model_file)


print('Pre-training word embeddings ...')
main('speaker')
#main('restaurant')
#main('beer')

