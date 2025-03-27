# transformer re-implementation

## reference
- [Japanese transformer re-implementation](https://www.dskomei.com/entry/2021/05/24/165158)
- [torchtext is deprecated and alternative](https://qiita.com/Nezura/items/9744746b013d64c029e2)
- [hugging face Dataset library quick start](https://huggingface.co/docs/datasets/quickstart)
- [hugging face tokenizer tutorial jpn](https://tt-tsukumochi.com/archives/4908)
- [hugging face tokenizer tutorial npaka](https://note.com/npaka/n/n36acd2122192)


## progress
- 2025-03-26 : download dataset and unzip. next action is tokenize
- 2025-03-27 : tokenize. next action is embedding

## dependencies
- take a look requirements.txt
- [spaCy](https://spacy.io/usage) 
    - additional dictionary is required
    - `pip install -U pip setuptools wheel`
    - `python -m spacy download en_core_web_sm`
    - `python -m spacy download de_core_news_sm`