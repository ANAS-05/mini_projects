import requests
from bs4 import BeautifulSoup
import os

url = "https://www.osmania.ac.in/res07/20231281.jsp"

headers = {
  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Encoding':'gzip, deflate, br, zstd',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Content-Length':'57',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie':'JSESSIONID=D7704E61A70640C3BA7F79F20FF930E8',
  'DNT': '1',
  'Origin': 'https://www.osmania.ac.in',
  'Referer': 'https://www.osmania.ac.in/res07/20231281.jsp',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

for roll in range(160422733061,160422733121):

  payload = f'mbstatus=SEARCH&htno={roll}'

  response = requests.request("POST", url, headers=headers, data=payload)
  soup = BeautifulSoup(response.content,'html.parser')

  rollno_result = soup.select('[align="center"][width="50%"]')[-1].get_text().lstrip() #lstrip : remove starting spaces

  cwd = os.getcwd()
  file_path = os.path.join(cwd,'web_scraper/results2sem.txt')

  try:
    with open(file_path,'a') as file:
      file.write(f'{roll} : {rollno_result},\n')
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
  except Exception as e:
    print(f"Error: {e}")

