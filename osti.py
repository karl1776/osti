import requests
import json
import openpyxl

start_report_number = "HEDL-SA-1274" # start of report number range
end_report_number = "HEDL-SA-1288" # end of report number range

# set up the API endpoint and parameters
url = "https://www.osti.gov/api/v1/records"
params = {
 "report_number": f"{start_report_number} TO {end_report_number}",
 "includeFields": "all",
 "has_fulltext":"true"
}

# send the API request and get the response
response = requests.get(url, params=params)
data = json.loads(response.text)

# create a new Excel workbook and worksheet
wb = openpyxl.Workbook()
ws = wb.active

# add headers to the worksheet
ws.append(["Report_number", "title"])



# loop through the records in the response data and add them to the worksheet

for record in data:['report_number','title'] 

 # check if the record is full text

#has_fulltext = "Yes" if record["has_fulltext"== True] else "False"

 # add the record data to the worksheet - not working -- problem is here!!
my_tuple = (report_number, title)

ws.append (my_tuple)
        

# save the Excel file
wb.save(r"C:\Users\Karl\Desktop\OSTIRecords.xlsx")