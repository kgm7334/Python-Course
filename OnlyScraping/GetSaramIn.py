import requests
from bs4 import BeautifulSoup

def Call_Saramin_Pages():
  SaramIn_URL="https://www.saramin.co.kr/zf_user/search?searchType=auto&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&keydownAccess=&searchword=WPF&loc_mcd=102000%2C101000&cat_cd=407&panel_type=&search_optional_item=y&search_done=y&panel_count=y"

  jobs=[]

  SaramIn_Result=requests.get(SaramIn_URL)

  print("사람인-WPF 정보 가져오기")

  SaramIn_Soup = BeautifulSoup(SaramIn_Result.text,"html.parser")

  JobInfos = SaramIn_Soup.find_all("div",{"class":"item_recruit"})

  for jobinfo in JobInfos:
    Full_Location=""
    JobTitle = jobinfo.find("h2",{"class":"job_tit"}).find("a")["title"]
    Company = jobinfo.find("strong",{"class":"corp_name"}).find("a")["title"]
    JobLoc = jobinfo.find("div",{"class":"job_condition"}).findAll('a')
    Job_List_URL_Value = jobinfo["value"]
    ApplyURL = f"https://www.saramin.co.kr/zf_user/jobs/relay/view?view_type=search&rec_idx={Job_List_URL_Value}&location=ts&searchword=WPF&searchType=auto&paid_fl=n"

    for Job in JobLoc:
      Job.find("a")
      Full_Location = Full_Location + Job.string

    jobs.append({'JobTitle':JobTitle,'Company':Company,'Location':Full_Location, 'ApplyURL':ApplyURL})

 
  return jobs  
  
    