# Pre-configure CSV metadata for NDImport tool
import pandas as pd

# metadata file. Ensure xlsx or csv is saved as CSV UTF-8 format
filename = r"\\filepath\Worldox metadata.csv"
# Copy all files into 1 folder
# extract actual file paths from folder with CTRL a + SHIFT - right-click - Copy as Path
# eg. C:\Users\username\Downloads\file.PDF...
# paste into metadata csv file under location (sort data first in another excel sheet A->Z)
# ensure location column aligns with the description column
# edit as necessary (usually more metadata than available files, delete extra metadata rows)

# dictionary to replace values - needs exact netdocs values for import
di = {
    # DocTypes
    'ACCOUNT': 'Accounting',
    'CORRESP': 'GENERAL-COMM',
    'DOC': 'GENERAL-DOC',
    'DRAFT': 'GENERAL-DOC',
    'FILE-ADM': 'GENERAL-DOC',
    'MEMO': 'GENERAL-DOC',
    'MISC': 'GENERAL-DOC',
    'PLEADING': 'GENERAL-DOC',
    'RESEARCH': 'RESEARCH',
    'APPLICAT': 'GENERAL-DOC',
    'TRIAL': 'COURT',
    'EMAIL': 'GENERAL-COMM',
    'EXPERT': 'EXP-REPORT',
    'XFD': 'GENERAL-COMM',
    'AGREE': 'AGREEMENT',
    'PREC': 'GENERAL-DOC',
    'PLOD': 'GENERAL-DOC',
    'DLOD': 'GENERAL-DOC',
    # Column headers
    'Location': 'filepath',
    '#7 (Typist)': 'Author',
    '#1 (File #)': 'Client',
    '#3 (Doc Type)': 'DocType',
    'Description': 'DOCUMENT NAME',
    'Date Created': 'CREATED DATE',
    'Date Modified': 'LAST MODIFIED DATE',
    'Cabinet': 'Matter',
    '#6 (Lawyer)': 'CREATED BY',
    'Owner': 'LAST MODIFIED BY',
}

# extract required columns from csv first (Based on Worldox Descriptions)
df = pd.read_csv(filename, usecols=['Owner', '#6 (Lawyer)', 'Location', 'Cabinet', 'Description', 'Date Created', '#7 (Typist)', 'Date Modified', '#1 (File #)', '#3 (Doc Type)', 'Comments'])

# rename column headers
for df in [df]: df.rename(columns=di, inplace=True)

# Apply dictionary replace to specific column contents
df['DocType'] = df['DocType'].map(di)
df['Author'] = df['Author'].map(di)
df['LAST MODIFIED BY'] = 'username'
df['Client'] = '12345'
df['Matter'] = '54321'
df['CREATED BY'] = df['CREATED BY'].map(di)

# convert dataframe to csv and export
df.to_csv(r'\\filepath\ImportReady.csv', index = False)

# print to console
pd.options.display.width = 0
print(df)

#upload using our csv file via ndimport tool
