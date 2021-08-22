import scrapy
import csv
import requests
import pandas as pd
from pandas.core.base import DataError
from pathlib import Path 
from dotenv import load_dotenv


data = pd.read_csv("listasites.csv",sep=",")
data.columns = ["sites"]
rawsites = list(data.sites)
print()

