import requests
from bs4 import BeautifulSoup


def Get_Last_PageIndex(JobKorea_URL):
    result = requests.get(JobKorea_URL)
    print("잡코리아-WPF 정보 가져오기")
    soup = BeautifulSoup(result.text, "html.parser")
    pgTotal = soup.find("span", {"class": "pgTotal"})
    Last_Page = pgTotal.get_text()
    return int(Last_Page)


def extract_job(html):
    CompanyName = html.find("a", {"class": "name"})["title"]
    JobTitle = html.find("a", {"class": "title"})["title"]
    Location = html.find("span", {"class": "long"}).string
    ApplyURL = html.find("a", {"class": "name"})["href"]

    if(ApplyURL.find("https") == -1):
        ApplyURL = "https://www.jobkorea.co.kr/"+ApplyURL

    return {'JobTitle': JobTitle, 'Company': CompanyName, 'Location': Location, 'ApplyURL': ApplyURL}


def extract_jobs(Last_Page, word):
    jobs = []
    print("검색결과"+str(Last_Page)+"페이지를 찾았습니다")
    for page in range(Last_Page):
        print(str(page+1)+"페이지 채용정보 추출중")
        result = requests.get(
            f"https://www.jobkorea.co.kr/Search/RecruitList?stext={word}&Page_No={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        Jobs = soup.find_all("div", {"class": "post"})

        for Job in Jobs:
            jobinfo = extract_job(Job)
            jobs.append(jobinfo)
        if(page>5): break
    return jobs


def Get_JobKorea_Pages(word):
    JobKorea_URL = f"https://www.jobkorea.co.kr/Search/RecruitList?stext={word}&Page_No=1"
    Last_Page = Get_Last_PageIndex(JobKorea_URL)
    jobs = extract_jobs(Last_Page, word)
    return jobs
