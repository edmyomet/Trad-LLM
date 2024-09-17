from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

import nltk
from nltk.corpus import stopwords

import json
from collections import Counter


def get_json_data(**kwargs)->dict:
    with open(kwargs['file_path'],'r',encoding='utf-8') as file:
        return json.load(file)

class SubWordTokenizer:
    tokenizer=None
    trainer = None
    file_path:str=""
    corpus:list[str]=[]
    json_data:dict={}
    encoded:dict={}
    def __init__(self,**kwargs):
        self.tokenizer = Tokenizer(BPE())
        self.tokenizer.pre_tokenizer = Whitespace()
        self.json_data = get_json_data(file_path=kwargs['file_path'])
        self.encoded['Data'] = [{header:[] for header in self.json_data['Data'][0].keys()} for _ in range(kwargs['start']-1,kwargs['end'])]
        
    def __build_trainer(self,**kwargs):
        vocab_size,min_freq = kwargs['vocab_size'], kwargs['min_freq']
        self.trainer = BpeTrainer(vocab_size=vocab_size,min_freq=min_freq)
    
    def __train(self):
        for documents in self.json_data['Data']:
            for key,value_list in documents.items():
                for sentence in value_list:
                    self.corpus.append(sentence)
        self.tokenizer.train_from_iterator(self.corpus,self.trainer)
    def __encode(self,**kwargs):
        for i in range(kwargs['start']-1,kwargs['end']):
            for key,value_list in self.json_data['Data'][i].items():
                tmp = []
                for sentence in value_list:
                    tmp.append(self.tokenizer.encode(sentence).tokens)
                self.encoded['Data'][i][key].append(tmp)
        with open(kwargs['output_file_path'],'a+',encoding='utf-8') as file:
            json.dump(self.encoded,file,ensure_ascii=False,indent=4)
                    
    def __save_tokenizer(self,**kwargs):
        self.tokenizer.save(path=kwargs['save_path'])
    def train_encode(self,**kwargs):
        self.__build_trainer(vocab_size=kwargs['vocab_size'],min_freq=kwargs['min_freq'])
        self.__train()
        self.__encode(output_file_path=kwargs['output_file_path'],start=kwargs['start'],end=kwargs['end'])
        self.__save_tokenizer(save_path=kwargs['save_path'])
        
        
class WordTokenizer:
    pass

class CharacterTokenizer:
    pass

def main(**kwargs):
    swt = SubWordTokenizer(file_path='./processed/lowercasing/lpdf.json',start=1,end=48)
    swt.train_encode(vocab_size=kwargs['vocab_size'],min_freq=kwargs['min_freq'],start=1,end=48,
                     save_path=kwargs['save_path'],output_file_path=kwargs['output_file_path'])
    

if __name__ == '__main__':
    main(vocab_size=20000,min_freq=2,save_path=rf'./processed/tokenised/tokeniser_config.json',
         output_file_path=rf'./processed/tokenised/tokenised-pdf.json')