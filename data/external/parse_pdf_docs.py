import json
import pdfplumber

class Extract_EDL:
    file_path:str=""
    output_file_path:str=""
    section_headers:list[str] = ['Abstract','keywords',
        'Introduction', 'Background', 'Summary','Objectives','Discussion', 'Material and Methods',
        'Methods','Methodology', 'Observations', 'Clinical', 'Experiments', 'Effects','Results','conclusion',
        'References','Acknowledgement'
    ]
    data:dict[str]={}
    
    def __init__(self,**kwargs):
        #self.file_path = kwargs['file_path']
        self.output_file_path = kwargs['output_file_path']
        self.data['Data'] = [{header:[] for header in self.section_headers} for _ in range(kwargs['start']-1,kwargs['end'])]
        #self.start = kwargs['start']-1
    def __extract_data(self,**kwargs):
        section_title = kwargs['header']
        self.file_path = kwargs['input_file_path']
        with pdfplumber.open(self.file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                lines = text.split('\n')
                in_section = False
                for line in lines:
                    if line.strip().lower() == section_title.lower():
                        in_section = True
                    elif in_section and line.strip() == '':
                        break
                    elif in_section:
                        self.data['Data'][self.start][section_title].append(line.strip())
    def __format(self):
        with open(self.output_file_path,'w+',encoding='utf-8') as json_file:
            json.dump(self.data, json_file,indent=4,ensure_ascii=False)
    
    def extract_and_format(self,**kwargs):
        for header in self.section_headers:
            self.__extract_data(input_file_path=kwargs['input_file_path'],header=header)
        self.__format()
    
def main(**kwargs):
    et = Extract_EDL(output_file_path=kwargs['output_file_path'],start=kwargs['start'],end=kwargs['end'])
    for i in range(kwargs['start'],kwargs['end']):
        et.start = i
        et.extract_and_format(input_file_path=rf"../../data/doc/image_pdf/pdf-{i+1}.pdf")
        
    
if __name__ == '__main__':
    main(output_file_path=rf'../../data/raw/pdf-2.json',start=0,end=100)