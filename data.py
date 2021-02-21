from nltk import pos_tag
import pandas as pd
import openpyxl

# Create variable to hold file name/path
excelFile = 'Coding Task.xlsx'

# Read Excel file
data = pd.read_excel(excelFile, sheet_name='Coding')
# Create pandas dataframe from Excel file with specified columns
df = pd.DataFrame(data, columns=['Index','Phrase'])
# Assign Part of Speech tags to each word within Phrase
dfTags = df['Phrase'].str.split().map(pos_tag)
# Write dataframe w/tags back to excel file
with pd.ExcelWriter(excelFile, engine='openpyxl', mode='a') as \
        writer:
    dfTags.to_excel(writer, sheet_name='sheet2', index=False)
    writer.save()


