from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):  
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  
  response = get(f"{base_url}{keyword}")    
  if response.status_code != 200:
    print("Can't request website")
  else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    results = []
    
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop(-1)
      for post in job_posts:
        anchor = post.find_all('a')
        anchor = anchor[1]
        link = anchor['href']
        company, kind, region = anchor.find_all('span', class_="company")
        title = anchor.find('span', class_='title')
        #print(company.string, kind.string, region.string, title.string) 
        job_data = {
          'link': f"http://weworkremotly.com{link}",
          'company': company.string.replace(","," "),
          'location': region.string.replace(","," "),
          'position': title.string.replace(","," ")
        }
        results.append(job_data)
  
    return results
    '''
    for result in results:
      print(result)
      print("/////////")
    '''  