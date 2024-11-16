import pandas as pd

tables=pd.read_html('https://en.wikipedia.org/wiki/Python_(programming_language)')
print(len(tables))

print(tables[0])
print(tables[1])
python_detail_table=tables[1]

python_detail_table.to_html('sample_table.html',index=False)
