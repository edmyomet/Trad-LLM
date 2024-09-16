import json
import fitz

def open_doc(file_name:str):
    return fitz.open(file_name)
class Extract_ELD:
    file_name:str
    output_file_name:str
    temp_data_store:dict
    doc = None
    def __init__(self,file_name:str):
        self.file_name = file_name
        self.doc = open_doc(self.file_name)
        self.temp_data_store = {
            'pdf_name' : self.file_name.split('/')[-1],
            'total_pages' : self.doc.page_count,
            'content' : {}
        }
    
    def __iter(self)->None:
        page:None
        for page_num in range(self.temp_data_store['total_pages']):
            page = self.doc.load_page(page_num)
            page_text = page.get_text('text')
            
            self.temp_data_store['content'][f'page_{page_num+1}'] = self.temp_data_store['content'].get(f'page_{page_num+1}', "") + page_text.strip()
    def __close(self)->None:
        self.doc.close()
    
    def save_to_json(self,output_file_name:str)->None:
        self.__iter()
        self.__close()
        self.output_file_name = output_file_name
        with open(self.output_file_name, "a+", encoding='utf-8') as file:
            json.dump(self.temp_data_store, file,ensure_ascii=False, indent=4)
    
    def reopen_doc(self,file_name:str)->None:
        self.file_name = file_name
        self.doc = open_doc(self.file_name)

class Extract_MLD:
    pass
    
def main(**kwargs):
    et = Extract_ELD(file_name=kwargs['file_name'])
    et.save_to_json(output_file_name=kwargs['output_file_name'])
    
if __name__ == '__main__':
    #for i in range(3,4):
    main(file_name=rf'../../data/doc/pdf-{3}.pdf', output_file_name=rf'../../data/raw/pdf.json')