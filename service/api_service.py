from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
class ApiService():

    api_username = "da64c0aa-3360-4e53-bc9e-1eb561635767"
    api_password = ""
    base_url="https://www.reed.co.uk/api/1.0/"

    def search(self):
        api_url = f"{self.base_url}search?postedByDirectEmployer=true&resultsToTake=15"
        response = requests.get(api_url, auth=HTTPBasicAuth(self.api_username,self.api_password))
        if response.status_code == 200:
            api_data = response.json()
            job_results = api_data.get('results', [])
            return job_results
        else:
            return []
        
    def searchByKeyword(self,looking,where):
        api_url = f"{self.base_url}search?keywords={looking}&locationName={where}"
        response = requests.get(api_url, auth=HTTPBasicAuth(self.api_username,self.api_password))

        if response.status_code == 200:
            api_data = response.json()
            job_results = api_data.get('results', [])
            return job_results
        else:
            return []

    def filterJobs(self,salary_from,salary_to,date_filter,employers):
        api_url = f"{self.base_url}search?minimumSalary={salary_from}&maximumSalary={salary_to}&employerId={employers[0] if len(employers)>0 else '':}"
        print(api_url)
        response = requests.get(api_url, auth=HTTPBasicAuth(self.api_username,self.api_password))
        if response.status_code == 200:
            api_data = response.json()
            job_results = api_data.get('results', [])
            if date_filter is not None:
                def convert_date(date_str):
                    return datetime.strptime(date_str, "%d/%m/%Y")
                if(date_filter=="Newest first"):
                    sorted_job_results = sorted(job_results, key=lambda x: convert_date(x["date"]), reverse=True)
                    return sorted_job_results
                else:
                    sorted_job_results = sorted(job_results, key=lambda x: convert_date(x["date"]))
                    return sorted_job_results

            return job_results
        else:
            return []
    

    def advancedSearch(self,params):

        looking = params['looking']
        where = params['where']
        salary_from = params['salary_from']
        salary_to = params['salary_to']
        permanent = True
        contract = True
        temp = True
        partTime = True
        fullTime = True
        graduate = True
        postedByRecruitmentAgency = True
        postedByDirectEmployer = True

        permanent = "permanent" in params['jobtype']
        contract = "contract" in params['jobtype']
        temp = "temporary" in params['jobtype']
        partTime = "partTime" in params['jobtype']
        fullTime = "fullTime" in params['jobtype']
        graduate = "graduate" in params['others']
        postedByRecruitmentAgency = "postedByRecruitmentAgency" in params['others']
        postedByDirectEmployer = "postedByDirectEmployer" in params['others']

       
        api_url = (
            f"{self.base_url}search?keywords={looking}&locationName={where}&minimumSalary={salary_from}&maximumSalary={salary_to}"
            f"&permanent={'True' if permanent else ''}&contract={'True' if contract else ''}&temp={'True' if temp else ''}"
            f"&partTime={'True' if partTime else ''}&fullTime={'True' if fullTime else ''}"
            f"&postedByRecruitmentAgency={'True' if postedByRecruitmentAgency else ''}"
            f"&postedByDirectEmployer={'True' if postedByDirectEmployer else ''}&graduate={'True' if graduate else ''}"
)
        print(api_url)
        response = requests.get(api_url, auth=HTTPBasicAuth(self.api_username,self.api_password))

        if response.status_code == 200:
            api_data = response.json()
            job_results = api_data.get('results', [])
            return job_results
        else:
            return []
    