import json 

class LowerCase:
    file_path:str=""
    json_data:dict={}
    lowercase_data:dict={'Data':[]}
    def __init__(self,**kwargs):
        self.file_path = kwargs['file_path']
    def __load_data(self)->dict:
        with open(self.file_path,'r',encoding='utf-8') as file:
            return json.load(file)
    def __to_lowercase(self,**kwargs):
        for i in range(kwargs['start']-1,kwargs['end']-1):
            for key,value_list in self.json_data['Data'][i].items():
                for j in range(len(value_list)):
                    value_list[j] = value_list[j].lower()
                    self.lowercase_data['Data'][i][key].append(value_list[j])
    def lowercasing(self,**kwargs):
        self.json_data = self.__load_data()
        self.lowercase_data['Data'] = [{header:[] for header in self.json_data['Data'][0].keys()} for _ in range(kwargs['start']-1, kwargs['end'])]
        self.__to_lowercase(start=kwargs['start'],end=kwargs['end'])
    def convert(self,**kwargs):
        with open(kwargs['output_file_path'],'w+',encoding='utf-8') as file:
            json.dump(self.lowercase_data,file,ensure_ascii=False,indent=4)
                    

def main(**kwargs):
    lc = LowerCase(file_path=kwargs['file_path'])
    lc.lowercasing(start=kwargs['start'],end=kwargs['end'])
    lc.convert(output_file_path=kwargs['output_file_path'])

if __name__ == '__main__':
    main(file_path=rf'./raw/pdf.json',output_file_path=rf'./processed/lowercasing/lpdf.json',start=1,end=48)