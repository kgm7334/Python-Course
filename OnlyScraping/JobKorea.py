import requests
from bs4 import BeautifulSoup

PageIndex = 1
JobKorea_URL=f"https://www.jobkorea.co.kr/Search/RecruitList?stext=WPF&Page_No={PageIndex}"


def Get_Last_PageIndex():
  result = requests.get(JobKorea_URL)
  print("잡코리아-WPF 정보 가져오기")
  soup = BeautifulSoup(result.text,"html.parser")
  pgTotal = soup.find("span",{"class":"pgTotal"}) 
  Last_Page = pgTotal.get_text()
  return int(Last_Page)

def extract_job(html):
  CompanyName = html.find("a",{"class":"name"})["title"]
  JobTitle = html.find("a",{"class":"title"})["title"]
  Location = html.find("span",{"class":"long"}).string
  ApplyURL = html.find("a",{"class":"name"})["href"]

  if(ApplyURL.find("https")==-1):
    ApplyURL = "https://www.jobkorea.co.kr/"+ApplyURL

  return {'JobTitle':JobTitle,'Company':CompanyName,'Location':Location, 'ApplyURL':ApplyURL}      
  

 

def extract_jobs(Last_Page):
  jobs=[]
  for page in range(Last_Page):
    result = requests.get(f"https://www.jobkorea.co.kr/Search/RecruitList?stext=WPF&Page_No={page+1}")
    soup = BeautifulSoup(result.text,"html.parser")
    Jobs = soup.find_all("div",{"class":"post"})

    for Job in Jobs:
      jobinfo = extract_job(Job)
      jobs.append(jobinfo)
  return jobs  

def Get_JobKorea_Pages():
  Last_Page = Get_Last_PageIndex()
  jobs=extract_jobs(Last_Page)
  return jobs
