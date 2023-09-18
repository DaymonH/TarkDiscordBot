import requests
from bs4 import BeautifulSoup
from variables import *

anchorStr = "_anchor"

# html = "https://escapefromtarkov.fandom.com/wiki/Ballistics"
with open("test.txt", "r") as f:
  html = f.read()
  # webpage_response = requests.get(html)
  # webpage = webpage_response.content
  soup = BeautifulSoup(html, "html.parser")


def findChart(round):
  '''Find the correct html element and prints chart for all its rounds'''
  tag = str(round) + str(anchorStr)
  data = soup.find(id=tag)
  globalList = []
  globalList.append(columnValue)
  curRound = data.get("id")
  while data.get("id") is None or curRound is data.get("id"):
    '''Loop through all the round of that calibur'''
    #below removes unessary elements that some ammos have so scraping can go smoothly
    if data.td.a and data.select_one(":nth-child(2)").a:
      data.select_one(":nth-child(1)").decompose()
    if data.td.select_one(":nth-child(2)"):
      data.td.select_one(":nth-child(2)").decompose()
    if data.td.select_one(":nth-child(2)"):
      data.td.select_one(":nth-child(2)").decompose()
    curList = []

    str1 = data.select_one(":nth-child(1)").text.strip()[:28]
    while len(str1) < 28:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(2)").text.strip()
    while len(str1) < 5:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(3)").text.strip()
    while len(str1) < 4:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(4)").text.strip()
    while len(str1) < 9:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(5)").text.strip()
    while len(str1) < 5:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(6)").text.strip()
    while len(str1) < 7:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(7)").text.strip()
    while len(str1) < 6:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(8)").text.strip()
    while len(str1) < 7:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(9)").text.strip()
    while len(str1) < 7:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(10)").text.strip()
    while len(str1) < 5:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(11)").text.strip()
    while len(str1) < 5:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(12)").text.strip()
    while len(str1) < 5:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(13)").text.strip()
    while len(str1) < 5:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(14)").text.strip()
    while len(str1) < 5:
      str1 += " "
    curList.append(str1)
    str1 = data.select_one(":nth-child(15)").text.strip()
    while len(str1) < 4:
      str1 += " "
    curList.append(str1)
    globalList.append(curList)
    data = data.find_next_sibling()
  endStr = ''
  lineAdded = False
  for subList in globalList:
    endStr += f'{subList[0]} | {subList[1]}{subList[2]}{subList[3]}{subList[4]}{subList[5]}{subList[6]}{subList[7]}{subList[8]}{subList[9]}{subList[10]}{subList[11]}{subList[12]}{subList[13]}{subList[14]}\n'
    if lineAdded == False:
      endStr += lineStr
      lineAdded = True
  return endStr
