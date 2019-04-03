# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:48:19 2019

@author: Leonard
"""

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\Leonard\Desktop\\My First Project-6a369352a7b2.json"

#-*- coding: utf-8 -*-





from google.cloud import translate



import pandas as pd

df= pd.DataFrame({'Spanish':['piso','cama']})



df["City_English"] = ""

for index, row in df.iterrows():
    translate_client = translate.Client()
    eng_text = translate_client.translate(row["Spanish"],target_language= 'en')
    eng_text = eng_text.get('translatedText')
    row["City_English"] = eng_text
