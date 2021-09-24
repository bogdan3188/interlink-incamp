import csv
import re
from datetime import datetime

# default values
lines = []
dates = []
workers = []
writeLines = []

# open file and fill lines, workers, dates no-repat
with open('acme_worksheet.csv') as inputfile:
	firstLine = []
	firstLine.append('Name / Date')

	reader = csv.DictReader(inputfile)
	for line in reader:

		if line['Date'] not in dates:
			dates.append(line['Date'])
			# change date format
			firstLine.append(datetime.strptime(line['Date'], '%b %d %Y').strftime('%Y-%m-%d'))

		if line['Employee Name'] not in workers:
			workers.append(line['Employee Name'])

		lines.append(line)
	writeLines.append(firstLine)

# sorts workers and dates
workers.sort()
dates.sort(key=lambda date: datetime.strptime(date, "%b %d %Y"))


# search work days for each worker
# search all days for each worker
for worker in workers:
	workerWorkDays = {line['Date'] : line['Work Hours'] for line in lines if line['Employee Name'] == worker}
	workerAllDays = [workerWorkDays[date] if date in workerWorkDays.keys() else 0 for date in dates ]
	workerAllDays.insert(0, worker)
	writeLines.append(workerAllDays)

#write new csv file
with open('output.csv', "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(writeLines)

inputfile.close()
file.close()
