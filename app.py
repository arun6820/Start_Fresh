from requests.auth import HTTPBasicAuth
from flask import Flask, jsonify, render_template, request
import requests

from service.api_service import ApiService



app=Flask(__name__)
app.static_folder = 'static'
api_service=ApiService()

@app.route("/")
def home():
    job_results = api_service.search()
    return render_template('home.html', job_results=job_results)




def searchResult(job_results,employer_names):
    return render_template('search_result.html', job_results=job_results,employer_names=employer_names)






@app.route('/search', methods=['GET'])
def search():
    looking = request.args.get('looking')
    where = request.args.get('where')
    job_results = api_service.searchByKeyword(looking,where)
    employer_names = [] 
    for job_result in job_results:
        employer_info = {
            "employerId": job_result["employerId"],
            "employerName": job_result["employerName"]
        }
        employer_names.append(employer_info)
    return render_template('search_result.html', job_results=job_results,employer_names=employer_names)


@app.route('/filter_jobs', methods=['POST'])
def searchJobs():
    salary_from = request.form.get('salary_from')
    salary_to = request.form.get('salary_to')
    date_filter = request.form.get('date_filter')
    employers = request.form.getlist('employers[]')
    job_results = api_service.filterJobs(salary_from,salary_to,date_filter,employers)
    return jsonify(job_results)

@app.route('/job-details', methods=['GET'])
def jobDetails():
    jobId = request.args.get('jobId')
    job_details = api_service.getJobDetailsById(jobId)

    return render_template('job_details.html',job_details=job_details)


@app.route('/advanced-search', methods=['GET', 'POST'])
def advancedSearchTemplate():
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            search_data = request.json
            job_results =  api_service.advancedSearch(search_data)
            employer_names = [] 
            for job_result in job_results:
                employer_info = {
                    "employerId": job_result["employerId"],
                    "employerName": job_result["employerName"]
                }
                employer_names.append(employer_info)

            response_data = {
            "job_results": job_results,
            "employer_names": employer_names
            }
            searchResult(job_results,employer_names)
            return jsonify(response_data)
                
        else:
            return render_template('advanced_search.html')
            
    return render_template('advanced_search.html')

@app.route('/advanced-search_page', methods=['GET'])
def advancedSearchTemplatePage():
    looking = request.args.get('looking')
    where = request.args.get('where')
    salary_from = request.args.get('salaryFrom')
    salary_to = request.args.get('salaryTo')
    jobTypes = request.args.get('jobTypes')
    otherTypes = request.args.get('otherTypes')
    
    search_data = {
        "looking": looking,
        "where": where,
        "salary_from": salary_from,
        "salary_to": salary_to,
        "jobtype": jobTypes,
        "others": otherTypes
    }

    print(search_data)
    job_results =  api_service.advancedSearch(search_data)
    employer_names = [] 
    for job_result in job_results:
        employer_info = {
                    "employerId": job_result["employerId"],
                    "employerName": job_result["employerName"]
                }
        employer_names.append(employer_info)
    return render_template('search_result.html', job_results=job_results,employer_names=employer_names)

@app.route('/popular-jobs', methods=['GET'])
def searchPopular():

    job_results = api_service.search()
    employer_names = [] 
    for job_result in job_results:
        employer_info = {
            "employerId": job_result["employerId"],
            "employerName": job_result["employerName"]
        }
        employer_names.append(employer_info)
    return render_template('popular_jobs.html', job_results=job_results,employer_names=employer_names)



if __name__ == '__main__':
    app.run()