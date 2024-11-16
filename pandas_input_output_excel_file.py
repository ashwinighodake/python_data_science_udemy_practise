import pandas as pd
df=pd.read_excel('/Users/ashwini/python-machine-learning-pdf/WinePredictor.xlsx',sheet_name='Sheet 1')
print(df)

wb=pd.ExcelFile('/Users/ashwini/python-machine-learning-pdf/WinePredictor.xlsx')
print(wb.sheet_names)
excel_sheet_dict=pd.read_excel('/Users/ashwini/python-machine-learning-pdf/WinePredictor.xlsx',sheet_name=None)
print(type(excel_sheet_dict))
print(excel_sheet_dict.keys())
our_df=excel_sheet_dict['Sheet 1']
our_df.to_excel('example.xlsx',sheet_name='Sheet 1',index=False)