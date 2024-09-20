import torch 
from transformers import pipeline 
from transformers import AutoTokenizer, AutoModelForTokenClassification
import json 
model_name = 'dmis-lab/biobert-v1.1'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)
class NER:
    nlp = pipeline('ner',model=model,tokenizer=tokenizer,aggregation_strategy='simple')
    file_path:str=""
    json_data:dict[list[dict[str]]]={}
    section_headers:list[str] = ['Abstract','keywords',
        'Introduction', 'Background', 'Summary','Objectives','Discussion', 'Material and Methods',
        'Methods','Methodology', 'Observations', 'Clinical', 'Experiments', 'Effects','Results','conclusion',
        'References','Acknowledgement'
    ]
    labelled_data:dict[list[dict[str]]] = {}
    def __init__(self,**kwargs):
        self.file_path = kwargs['file_path']
    def __get_json(self):
        with open(self.file_path,'r',encoding='utf-8') as json_file:
            return json.load(json_file)   
    def __extract_labels(self,**kwargs):
        contents:str
        if kwargs['contents'] == [] or kwargs['contents'] == [[]]:
            return []
        if isinstance(kwargs['contents'],list):
            contents = "".join(kwargs['contents'][0])
        tmp = self.nlp(contents)
        return [{ent['word']:ent['entity_group']}for ent in tmp]
    def __save(self,**kwargs):
        with open(kwargs['output_file_path'],'w+',encoding='utf-8') as json_file:
            json.dump(self.labelled_data, json_file, indent=4,ensure_ascii=True)
    def ner_find(self):
        self.json_data = self.__get_json()
        self.labelled_data['Data'] = self.json_data['Data']
        list_item = self.json_data['Data']
        for index,document in enumerate(self.json_data['Data']):
                for field in self.section_headers:
                    entity:list = []
                    if field in document:
                        tmp = document[field]
                        entity = self.__extract_labels(contents=tmp)
                    self.labelled_data['Data'][index][f'{field} entity'] = entity
        self.__save(output_file_path=rf'../../data/processed/labelled/labelled-web.json')
def main():
    nerecog = NER(file_path=rf'../../data/processed/stemmed/lemmatized-web.json')
    nerecog.ner_find()

if __name__=='__main__':
    main()