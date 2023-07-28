import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://iftp.chinamoney.com.cn/english/bdInfo/'
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
# 找到目标数据表格
table = soup.find('table')
# 定义用于存储数据的列表
data = []
# 解析表格数据
for row in table.find_all('tr'):
    row_data = [cell.text for cell in row.find_all('td')]
    if row_data:  # 忽略表头行
        data.append(row_data)
# 将数据转为DataFrame
df = pd.DataFrame(data, columns=['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating'])
# 根据条件筛选数据
df_filtered = df[(df['Bond Type'] == 'Treasury Bond') & (df['Issue Date'].str.endswith('2023'))]
df_filtered.to_csv('filtered_data.csv', index=False)
