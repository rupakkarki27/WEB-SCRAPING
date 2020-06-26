"""
Created on Thu Jun 25 2020
@author: Rupak Karki (@rupakkarki27)
"""

import ny_times_scraper as ny
import pandas as pd

url = 'https://www.nytimes.com/search?dropmab=false&query=Machine%20Learning&sort=newest'

df = ny.ny_scraper(url, 60, 3)

df.to_csv('ny_data.csv', index=False)