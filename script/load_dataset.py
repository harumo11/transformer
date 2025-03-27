import os

class Multi30k:
    def __init__(self):
        self.datasets = {'texts_src_de_train': None, 'texts_tgt_en_train': None, 'texts_src_de_valid': None, 'texts_tgt_en_valid': None}
        self.datasets = self.load_texts()

    def _path_to_multi30k(self, data_dir_path = '/home/sasatake/repos/python/transformer/data/processed/multi30k_unziped/'):
        train_de_path = os.path.join(data_dir_path, 'train.de.txt')
        train_en_path = os.path.join(data_dir_path, 'train.en.txt')
        val_de_path = os.path.join(data_dir_path, 'val.de.txt')
        val_en_path = os.path.join(data_dir_path, 'val.en.txt')

        return train_de_path, train_en_path, val_de_path, val_en_path


    def _read_texts(self, file_path):
        with open(file_path, 'r') as f:
            texts = f.readlines()
        return texts
    
    def load_texts(self):
        train_de_path, train_en_path, val_de_path, val_en_path = self._path_to_multi30k()
        datasets = {}
        datasets['texts_src_de_train'] = self._read_texts(train_de_path)
        datasets['texts_tgt_en_train'] = self._read_texts(train_en_path)
        datasets['texts_src_de_valid'] = self._read_texts(val_de_path)
        datasets['texts_tgt_en_valid'] = self._read_texts(val_en_path)

        return datasets
    
    def show_example(self):
        texts_src_train = self.datasets['texts_src_de_train']
        texts_tgt_train = self.datasets['texts_tgt_en_train']

        for src, tgt in zip(texts_src_train[:3], texts_tgt_train[:3]):
            print(src.strip('\n'))
            print('|')
            print(tgt.strip('\n'))
            print('')