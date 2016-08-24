import mechanize
from bs4 import BeautifulSoup
import csv

#using mechanize for authentication
br = mechanize.Browser()
br.open('https://supremo.nic.in/knowyourofficerIAs.aspx')

br.select_form(nr=0)
form = br.form

# years=['1990','1991','1992',]
allotyearstart = 1900
allotyrend = 2017
years = []
for i in range(allotyearstart,allotyrend):
    years.append("%s" % i)
officerdata = []
i = ""
for i in range(len(years)):
    # print type(years[i])
    str = years[i]

    form["txtAllotYr"] = str
    br.form = form
    res = br.submit(name='btnSubmit')
    final = res.geturl()
    # print res.geturl()+""

    soup = BeautifulSoup(br.response().read(), 'lxml')
    for mytable in soup.find_all('table'):
        for trs in mytable.find_all('tr'):
            tds = trs.find_all('td')
            row = [elem.text.strip().encode('utf-8') for elem in tds]
            officerdata.append(row)

# print officerdata

csv_columns = ['Name', 'Service', 'Cadre', 'Allotment year', 'Date of Birth', 'Date of Joining']
with open("iasofficerdata.csv", "wb") as output:

    writer = csv.writer(output)
    writer.writerow(csv_columns)
    writer.writerows(officerdata)

# print "file closed successfully.."
