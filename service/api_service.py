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
        
    