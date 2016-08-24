from urllib2 import urlopen
from bs4 import BeautifulSoup
import sys

def make_soup(url):
    thepage = urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

officerdatasaved = ""
start = 133
end = 26116
for i in range(start,end):
    try:
        soup = make_soup('https://supremo.nic.in/ERSheetHtml.aspx?OffIDErhtml=%s&PageId=' %i)
        # print soup
        # print 'https://supremo.nic.in/ERSheetHtml.aspx?OffIDErhtml='+str(i)+'&PageId='
        identity = ""
        count = 0
        for row in soup.findAll('table')[0].tbody.findAll('tr'):
                for data in row.findAll("td")[1:]:
                    for bval in data.findAll("b"):
                        count += 1
                        if count == 2:
                            identity = bval.text
        try:
            for row in soup.findAll('table')[3].tbody.findAll('tr'):
                officerdata = ""
                for data in row.findAll("td")[1:]:
                    officerdata = officerdata+","+data.text
                officerdatasaved = officerdatasaved + "\n" + identity+","+officerdata[1:]
        except:
            for row in soup.findAll('table')[3].thead.findAll('tr'):
                officerdata = ""
                for data in row.findAll("td")[1:]:
                    officerdata = officerdata+","+data.text
                officerdatasaved = officerdatasaved + "\n" + identity+","+officerdata[1:]

    except:
        pass

# print officerdatasaved
header = "Identity,Designation,Department/Office,Organisation,Experience,Period"+""
file = open(os.path.expanduser("ssofficer1.csv"), "wb")
file.write(bytes(header).encode('ascii', 'ignore').decode('ascii', 'ignore'))
file.write(bytes(officerdatasaved).encode('ascii', 'ignore').decode('ascii', 'ignore'))

