import requests
from bs4 import BeautifulSoup

url_list:list[str] = [
    "https://journals.lww.com/jrsm/fulltext/2024/01000/phytochemical_characterization_of_siddha.8.aspx",
    "https://journals.lww.com/jrsm/fulltext/2024/01000/a_case_study_on_manjalkaram__medicated_alkaline.6.aspx",
    "https://journals.lww.com/jrsm/fulltext/2024/01000/unveiling_the_mystique_of_kulisam__amulet__with.1.aspx",
    "https://www.planetayurveda.com/herbs-a-to-z/",
    "https://www.wbhealth.gov.in/WBSMPB/medicinal_plants_available.php",
    "https://www.wbhealth.gov.in/WBSMPB/29_Very_prioritized_prohobited_species.php",
    
]