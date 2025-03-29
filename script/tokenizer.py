import spacy
from collections import Counter

class Tokenizer():
    def __init__(self):
        self.spacy_de = spacy.load('de_core_news_sm')
        self.spacy_en = spacy.load('en_core_web_sm')

    def _tokenize_de(self, text, remove_eos=True):
        if remove_eos:
            return [tok.text for tok in self.spacy_de.tokenizer(text)][:-1]
        else:
            return [tok.text for tok in self.spacy_de.tokenizer(text)]

    def _tokenize_en(self, text, remove_eos=True):
        if remove_eos:
            return [tok.text for tok in self.spacy_en.tokenizer(text)][:-1]
        else:
            return [tok.text for tok in self.spacy_en.tokenizer(text)]
    
    def build_vocab(self, lang, texts, special_tokens=['<unk>', '<pad>', '<start>', '<end>']):
        counter = Counter() # count up for frequency of words

        # separate for each word(token)
        for text in texts: # 1 line from dataset
            if lang == 'de':
                tokens = self._tokenize_de(text)
            if lang == 'en':
                tokens = self._tokenize_en(text)
            counter.update(tokens) # update count

        # add special tokens to counter
        token2idx = {token: idx + len(special_tokens) for idx, token in enumerate(counter.keys())}
        for idx, special_token in enumerate(special_tokens):
            token2idx[special_token] = idx
        
        # sort by frequency
        token2idx = dict(sorted(token2idx.items(), key=lambda item: item[1], reverse=False))
        
        # idx to token
        idx2token = {idx: token for token, idx in token2idx.items()}

        return token2idx, idx2token

    def max_text_len(self, texts):
        max_len = 0
        for text in texts:
            tokens = self.tokenize_de(text)
            if len(tokens) > max_len:
                max_len = len(tokens)
        return max_len