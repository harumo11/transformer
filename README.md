# transformer re-implementation

## reference
- [Japanese transformer re-implementation](https://www.dskomei.com/entry/2021/05/24/165158)
- [torchtext is deprecated and alternative](https://qiita.com/Nezura/items/9744746b013d64c029e2)
- [hugging face Dataset library quick start](https://huggingface.co/docs/datasets/quickstart)

## progress
- 2025-03-26 : download dataset and unzip. next action is tokenize

## dependencies
- take a look requirements.txt
- [spaCy](https://spacy.io/usage) 
    - additional dictionary is required
    - `python -m spacy download en_core_web_sm`
    - `python -m spacy download de_core_news_sm`