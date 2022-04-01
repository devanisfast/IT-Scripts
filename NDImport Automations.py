# Pre-configure CSV metadata for NDImport tool
import pandas as pd

# metadata file. Ensure xlsx or csv is saved as CSV UTF-8 format
filename = r"\\hgdata1\db\Secured\Song\00646 1161059 BC Ltd\00646 Exported from Worldox\File-Admin\Worldox metadata 00646.csv"
# Copy all files into 1 folder
# extract actual file paths from folder with CTRL a + SHIFT - right-click - Copy as Path
# eg. C:\Users\dfast\Downloads\RESEARCHES\STREET.PDF...
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
    # column data replace
    'SXUE': 'Song Xue',
    'ALI': 'Aileena Li',
}

# extract required columns from csv first (Based on Worldox Descriptions)
df = pd.read_csv(filename, usecols=['Owner', '#6 (Lawyer)', 'Location', 'Cabinet', 'Description', 'Date Created', '#7 (Typist)', 'Date Modified', '#1 (File #)', '#3 (Doc Type)', 'Comments'])

# rename column headers
for df in [df]: df.rename(columns=di, inplace=True)

# Apply dictionary replace to specific column contents
df['DocType'] = df['DocType'].map(di)
df['Author'] = df['Author'].map(di)
df['LAST MODIFIED BY'] = 'Song Xue'
df['Client'] = '25093'
df['Matter'] = '153069'
df['CREATED BY'] = df['CREATED BY'].map(di)

# remove directory path from filenames. Ensure to use \\ for all \
# remove extension from the description as well
# df['DOCUMENT NAME'] = df['DOCUMENT NAME'].str.replace(r"C:\\Users\\dfast\\Downloads\\RESEARCHES\\", "")
# df['DOCUMENT NAME'] = df['DOCUMENT NAME'].str.replace(r".PDF", "")
# df['DOCUMENT NAME'] = df['DOCUMENT NAME'].str.replace(r".MSG", "")
# df['DOCUMENT NAME'] = df['DOCUMENT NAME'].str.replace(r".PDF", "")
# df['DOCUMENT NAME'] = df['DOCUMENT NAME'].str.replace(r".DOCX", "")
# df['DOCUMENT NAME'] = df['DOCUMENT NAME'].str.replace(r".DOC", "")
# df['DOCUMENT NAME'] = df['DOCUMENT NAME'].str.replace(r".XLSX", "")

# convert dataframe to csv and export
df.to_csv(r'\\hgdata1\db\Secured\Song\00646 1161059 BC Ltd\00646 Exported from Worldox\File-Admin\00646_ImportReady.csv', index = False)

# print to console
pd.options.display.width = 0
print(df)