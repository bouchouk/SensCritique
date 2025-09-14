import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re
from system.load import fightclub, interstellar 

def remove_html(text):
    soup = BeautifulSoup(text, "html.parser")
    for a in soup.find_all("a"):
        a.decompose()
    return soup.get_text(" ", strip=True)

def remove_poc(text):
    return re.sub(r"[^\w\s]", " ", text)

#Remove the Null value in fightclub and create new dataframes for the cleaning
f_content = fightclub[['review_content', 'id']].dropna()
i_content = interstellar[['review_content', 'id']]

#Remove Html tags from our content    
f_content['review_content'] = f_content['review_content'].apply(remove_html)
i_content['review_content'] = i_content['review_content'].apply(remove_html)

#Remove all regular expressions for a smooth encoding
f_content['review_content'] = f_content['review_content'].apply(remove_poc)
i_content['review_content'] = i_content['review_content'].apply(remove_poc)

#Lower case the text
f_content["review_content"] = f_content["review_content"].str.lower()
i_content["review_content"] = i_content["review_content"].str.lower()

#Remove the content that becomes empty (like the row 998 in the fightclub data)
f_content = f_content[f_content["review_content"].str.strip() != ""]
i_content = i_content[i_content["review_content"].str.strip() != ""]

#Drop index
f_content = f_content.reset_index(drop=True)
i_content = i_content.reset_index(drop=True)