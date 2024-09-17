import requests
from bs4 import BeautifulSoup

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
]

