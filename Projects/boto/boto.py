import boto3
import json

# Access keys to access the data buckets
ACCESS_KEY        = ""
SECRET_ACCESS_KEY = ""

# Authentication
client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_ACCESS_KEY)

# Retrieve data from bucket named class6-logs which has logs files
resp = client.list_objects(Bucket='class6-logs')

"""
@param count: A counter to append names in front of different logs file
@param data : List to append all the lines in log
"""
count = 0
data = []

for object in resp['Contents']:
  
  # This function download files available in the contents
  client.download_file('class6-logs', resp['Contents'][count]['Key'], str(count)+'.json')

  # This here loads the file line by line and converts into python dict from json object
  with open(str(count)+'.json') as f:
    for line in f:
      data.append(json.loads(line))
  count += 1


"""
@param count_404_500: A counter to count for the errors
@param itr_count    : Iterator variable for list
"""
count_404_500 = 0
itr_count = 0


# Searches for error in data
for itr in data:
  if data[itr_count]["status"] == 404 or data[itr_count]["status"] == 500:
    count_404_500 += 1
  itr_count += 1

print("Lines scanned:",len(data))
print("Number of 404 and 500:",count_404_500)