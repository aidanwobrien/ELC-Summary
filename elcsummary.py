# Importing the required modules 
import tkinter
from tkinter import filedialog
import pandas as pd
from bs4 import BeautifulSoup

# Make the tkinter dialogue box
from tkinter.filedialog import askopenfilename, asksaveasfile
from pandas.core.frame import DataFrame
filename = askopenfilename()
path = filename
   
# make an empty list
data = []
   
# get the header from the HTML file
list_header = []
soup = BeautifulSoup(open(path),'html.parser')
header = soup.find_all("table")[0].find("tr")
  
for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue
  
# get the data from the HTML file
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
  
for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)

  
# Storing the data into a Pandas dataframe
df = pd.DataFrame(data, columns = ["value", "pixel", "area"])

# Create a dictionary that labels specific values
dict = {
    "11":"Open Beach/Bar",
    "21":"Open Sand Dune",
    "23":"Treed Sand Dune",
    "41":"Open Cliff and Talus",
    "43":"Treed Cliff and Talus",
    "52":"Open Alvar",
    "53":"Shrub Alvar",
    "64":"Treed Alvar",
    "65":"Open Bedrock",
    "81":"Open Tallgrass Praire",
    "82":"Tallgrass Savannah",
    "83":"Tallgrass Woodland",
    "90":"Forest-other",
    "91":"Coniferous Forest",
    "92":"Mixed Forest",
    "93":"Deciduous Forest",
    "131":"Treed Swamp",
    "135":"Thicekt Swamp",
    "140":"Fen",
    "150":"Bog",
    "160":"Marsh",
    "170":"Open Water",
    "191":"Plantations-Tree Cultivated",
    "192":"Hedge Rows",
    "193":"Tilled",
    "201":"Transportation",
    "202":"Built-Up Area - Pervious",
    "203":"Built-Up Area - Impervious",
    "204":"Extraction - Aggregate",
    "205":"Extraction-Peat/Topsoil",
    "250":"Undifferentiated"
    }

# Create a new column called "name" with the mapped columns
df["name"] = df["value"].map(dict)

# Create a new column called "ha" with the property area in hectares
df["ha"] = (df["area"].astype(float)) / 10000

# Create a new coloumn called "acres" with the property area in acres
df["ac"] = (df["ha"].astype(float)) * 2.47105

# # Calling your file some name

output_file = input("Enter filename: ")

# Converting Pandas DataFrame into a csv file called "ELC_Summary"
df.to_csv(rf"{output_file}.csv")
