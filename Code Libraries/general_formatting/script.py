
import csv
import json

in_file = open("/Users/leo/Desktop/session_content2.csv", "r")
data = in_file.read()
in_file.close()

rows = data.split('\n')

splitted_rows = []
for row in rows: 
  splitted_rows.append(row.split(';'))



formatted = []
for splitted in splitted_rows:
  if len(splitted) == 2:
    content = json.loads(splitted[1])
    formatted.append([ splitted[0], content["buildVersion"], content["beacons"], content["id"], content["events"], content["language"], content["iosVersion"]])
  else :
    print(splitted)

out_file = open("/Users/leo/Desktop/session_content_formatted.csv", "w")
csvwriter = csv.writer(out_file, delimiter =';')
csvwriter.writerow(["id","buildVersion","beacons","content_id","events","language","iosVersion"])
csvwriter.writerows(formatted)
