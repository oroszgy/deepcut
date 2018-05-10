import plac
from tqdm import tqdm
import deepcut


def main(file_path):
    data = open(file_path)
    sentences = [sent for article in data for sent in article.split() if len(sent) > 10]
    print("Tokenizing {} articles total {} characters".format(len(sentences), sum(map(len, sentences))))
    for s in tqdm(sentences):
        deepcut.tokenize(s)


if __name__ == "__main__":
    plac.call(main)
