import nltk
from nltk.stem import PorterStemmer
import string 
import json 

class Stemmer:
    stemmer = PorterStemmer()
    file_path:str=""
    tokens:list[str]=[]
    json_data:dict[str] = {}
    documents:list[dict[str]]=[]
    def __init__(self,**kwargs):
        self.file = kwargs['file_path']
    
    def __get_json(self):
        with open(self.file,'r',encoding='utf-8') as json_file:
            return json.load(json_file)
    
    def __stem(self):
        self.documents = self.json_data['Data']
        for index, documents in enumerate(self.documents):
            for headers in self.documents[index].keys():
                try:
                    self.documents[index][headers][0] = [self.stemmer.stem(tokens) for tokens in lists for lists in self.documents[index][headers][0]]
                except:
                    pass
        self.json_data['Data'] = self.documents
    
    def __save(self,**kwargs):
        with open(kwargs['output_file'],'w+',encoding='utf-8') as json_file:
            json.dump(self.json_data,json_file,indent=4,ensure_ascii=False)
    
    def stem_and_save(self,**kwargs):
        self.json_data = self.__get_json()
        self.__stem()
        self.__save(output_file=kwargs['output_file'])

def main(**kwargs):
    stem = Stemmer(file_path=kwargs['file_path'])
    stem.stem_and_save(output_file=kwargs['output_file'])

if __name__ == '__main__':
    main(file_path=rf'./processed/lowercasing/lpdf.json',output_file=rf'./processed/stemmed/stemmed-pdf.json')

                    
            
