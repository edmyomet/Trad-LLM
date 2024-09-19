import requests
from bs4 import BeautifulSoup
import json
import time

url_list:list[str] = [
    "https://journals.lww.com/jrsm/fulltext/2024/01000/phytochemical_characterization_of_siddha.8.aspx",
    "https://journals.lww.com/jrsm/fulltext/2024/01000/a_case_study_on_manjalkaram__medicated_alkaline.6.aspx",
    "https://journals.lww.com/jrsm/fulltext/2024/01000/unveiling_the_mystique_of_kulisam__amulet__with.1.aspx",
    "https://www.planetayurveda.com/herbs-a-to-z/",
    "https://www.wbhealth.gov.in/WBSMPB/medicinal_plants_available.php",
    "https://www.wbhealth.gov.in/WBSMPB/29_Very_prioritized_prohobited_species.php",
    "https://journals.lww.com/aayu/fulltext/2018/39040/in_vitro_anti_inflammatory_activity_of_ficus.8.aspx#",
    "https://journals.lww.com/aayu/fulltext/2024/45020/dip_eyes_in_water_technique__akshi_nimanjjana__.7.aspx",
    "https://journals.lww.com/aayu/fulltext/2024/45020/evaluation_of_jati__jasminum_grandiflorum_l__.4.aspx",
    "https://pubmed.ncbi.nlm.nih.gov/25379463/",
    "https://pubmed.ncbi.nlm.nih.gov/38685809/",
    "https://pubmed.ncbi.nlm.nih.gov/37254529/",
    "https://pubmed.ncbi.nlm.nih.gov/33033566/",
    "https://pubmed.ncbi.nlm.nih.gov/27011715/",
    "https://pubmed.ncbi.nlm.nih.gov/35929620/",
    "https://pubmed.ncbi.nlm.nih.gov/39138188/",
    "https://www.wbhealth.gov.in/WBSMPB/32_prioritized_species_enlisted_by_NMPB.php",
    "https://www.wbhealth.gov.in/WBSMPB/district_wise_suitability_for_cultivation.php",
    "https://www.wbhealth.gov.in/WBSMPB/32_consumption_medicinal_plants%20in_ayurvedic.php",
    "https://www.wbhealth.gov.in/WBSMPB/medicinal_plants_related_web_site.php",
    "https://www.sciencedirect.com/science/article/pii/S0975947623001249",
    "https://pubmed.ncbi.nlm.nih.gov/39282188/"
    "https://pubmed.ncbi.nlm.nih.gov/39283965/",
    "https://pubmed.ncbi.nlm.nih.gov/39270421/",
    "https://pubmed.ncbi.nlm.nih.gov/39269343/",
    "https://pubmed.ncbi.nlm.nih.gov/39197202/",
    "https://pubmed.ncbi.nlm.nih.gov/39184668/",
    "https://pubmed.ncbi.nlm.nih.gov/39167989/",
    "https://pubmed.ncbi.nlm.nih.gov/39143605/",
    "https://pubmed.ncbi.nlm.nih.gov/39135328/",
    "https://pubmed.ncbi.nlm.nih.gov/39128430/",
    "https://pubmed.ncbi.nlm.nih.gov/39121783/",
    "https://pubmed.ncbi.nlm.nih.gov/39085970/",
    "https://pubmed.ncbi.nlm.nih.gov/39081888/",
    "https://pubmed.ncbi.nlm.nih.gov/39067943/",
    "https://pubmed.ncbi.nlm.nih.gov/23049182/",
    "https://pubmed.ncbi.nlm.nih.gov/22557316/",
    "https://pubmed.ncbi.nlm.nih.gov/24695779/",
    "https://pubmed.ncbi.nlm.nih.gov/24501516/",
    "https://pubmed.ncbi.nlm.nih.gov/22529646/",
    "https://journals.lww.com/aayu/fulltext/2024/45020/evaluation_of_jati__jasminum_grandiflorum_l__.4.aspx",
    "https://journals.lww.com/aayu/fulltext/2024/45020/management_of_biliary_calculi_through_ayurveda___a.3.aspx",
    "https://journals.lww.com/aayu/fulltext/2024/45020/safety_profile_of_naga_bhasma_prepared_by_two.6.aspx",
    "https://journals.lww.com/aayu/fulltext/2024/45020/dip_eyes_in_water_technique__akshi_nimanjjana__.7.aspx",
    "https://pubmed.ncbi.nlm.nih.gov/9701897/",
    "https://journals.lww.com/aayu/fulltext/2011/32040/effect_of_ayurvedic_herbs_on_control_of_plaque_and.18.aspx",
    "https://journals.lww.com/aayu/abstract/2009/30040/a_review_on_herbs_used_in_treatment_of_diabetes.3.aspx",
    "https://journals.lww.com/aayu/fulltext/2019/40020/gut_microbiota__one_of_the_new_frontiers_for.3.aspx",
    "https://journals.lww.com/aayu/fulltext/2024/45020/management_of_lupus_thrombocytopenia_through.2.aspx",
    "https://journals.lww.com/aayu/fulltext/2022/43020/a_lexical_review_on_vishaghna_dravyas_of_kaideva.3.aspx"
    "https://journals.lww.com/jped/fulltext/2008/26010/effect_of_oil_pulling_on_streptococcus_mutans.4.aspx",
    "https://www.tandfonline.com/doi/full/10.1080/17425255.2024.2378895#d1e440",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11223638/",
    "https://www.sciencedirect.com/science/article/abs/pii/S0378874124008134?via%3Dihub",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11382864/"
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11171552/",
    "https://linkinghub.elsevier.com/retrieve/pii/S0378-8741(24)00672-X",
    "https://pubs.acs.org/doi/10.1021/jasms.4c00016",
    "https://www.sciencedirect.com/science/article/pii/S0952818024001028?via%3Dihub",
    "https://www.mdpi.com/2072-6643/16/7/934",
    "https://www.eurekaselect.com/article/139130",
    "https://www.sciencedirect.com/science/article/abs/pii/S0378874124001326?via%3Dihub",
    "https://www.eurekaselect.com/article/137598",
    "https://www.sciencedirect.com/science/article/abs/pii/S0001706X24002201?via%3Dihub",
    "https://www.sciencedirect.com/science/article/abs/pii/S0019570723002202?via%3Dihub",
    "https://www.sciencedirect.com/science/article/pii/S0378874123014058?via%3Dihub",
    "https://link.springer.com/article/10.1007/s10534-023-00556-z",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10456159/",
    "https://www.spandidos-publications.com/mmr/28/4/187"
    "https://www.sciencedirect.com/science/article/abs/pii/S0378874123000211?via%3Dihub",
    "https://onlinelibrary.wiley.com/doi/10.1155/2022/1108569",
    "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0277614",
    "https://www.mdpi.com/2072-6643/14/19/3926",
    "https://link.springer.com/article/10.1007/s00266-022-03048-6"
]

def get_from_tags(**kwargs):
    tag_name = kwargs['tag']
    if tag_name:
        next_sibling = tag_name.find_next_sibling()
        tmp_info = []
        '''for child in tag_name.find_all(recursive=False):
            tmp_info.append([sentence] for sentence in child.get_text(strip=True).split("."))'''
        while next_sibling:
            tmp_info.append(next_sibling.get_text(strip=True))
            next_sibling = next_sibling.find_next_sibling()
        return "".join(tmp_info) if tmp_info else ""
    return ""
class WebScraper:
    response=None
    data:dict[str]= {}
    section_headers:list[str] = ['title','Abstract','keywords',
        'Introduction', 'Background', 'Summary','Objectives','Discussion', 'Material and Methods',
        'Methods','Methodology', 'Observations', 'Clinical', 'Experiments', 'Effects','Results','conclusion',
        'References','Acknowledgement'
    ]
    supplementary_headers:list[str] =[]
    url_list:list[str] = []
    html_content=None
    soup = None
    file_path:str=""
    html_content = None
    start = 0
    end = 0
    header_tags = ['h1','h2','h3','strong']
    other_tags = ['p','div','ul','ol','li']
    def __init__(self,**kwargs):
        self.url_list = kwargs['url_list']
        self.data['Data'] = [{header:[] for header in self.section_headers} for i in range(len(url_list))]
        self.file_path = kwargs['file_path']
    def __get_html_content(self,**kwargs)->str:
        self.response = requests.get(kwargs['url'])
        if self.response.status_code == 200:
            return self.response.text
        return None
    def __get_info(self,**kwargs)->str:
        for header in self.section_headers:
            title_tag = self.soup.find(lambda tag: tag.name in self.header_tags[1:] and header.lower() in tag.get_text(strip=True).lower())
            self.supplementary_headers.append(self.soup.find(lambda tag:tag.name in self.header_tags and header.lower() not in tag.get_text(strip=True).lower()))
            self.data['Data'][kwargs['entity_no']][header].append(get_from_tags(tag=title_tag))
        
        '''for header in self.supplementary_headers:
            if header:
                header = header.get_text(strip=True)
            else:
                continue 
            title_tag = self.soup.find(lambda tag:tag.name in self.header_tags and header.lower() in tag.get_text(strip=True).lower())
            self.data['Data'][kwargs['entity_no']][header] = [].append(get_from_tags(tag=title_tag))'''
    def __save(self):
        with open(self.file_path,'w+',encoding='utf-8') as json_file:
            print(type(self.data))
            json.dump(self.data,json_file,indent=4,ensure_ascii=False)
    
    def extract_and_save(self):
        for url in self.url_list:
            self.html_content = self.__get_html_content(url=url)
            if self.html_content:
                self.soup =  BeautifulSoup(self.html_content,'html5lib')
                self.__get_info(entity_no=self.url_list.index(url))
                time.sleep(1.5)
        self.__save()

def main():
    ws = WebScraper(url_list = url_list, file_path = rf'../../data/raw/web-1.json')
    ws.extract_and_save()

if __name__ == '__main__':
    main()