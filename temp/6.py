## This is for stercth names on ACS

from bs4 import BeautifulSoup
import requests
# import csv
import bs4
 

def check_link(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('No response')
 
 
def get_contents(ulist):
   for fundings in ulist:
        # print
        rurl=fundings
        rs = check_link(rurl)
        # totalP = BeautifulSoup(rs,'lxml').find_all('a')
        # totalP = int(totalP[-12].get('href').split('=')[-1])
        print rs

    #   for pages in range(1,1+totalP):
    #         rs = check_link(rurl+str(pages))
    #         tds = BeautifulSoup(rs,'lxml').find_all('td')
    #         tds = [ x.string.strip().encode('ascii', 'ignore') for x in tds[9:]]
    #         # tds = [ x.decode('utf-8') for x in tds]
    #         for i in range(len(tds)/6):
    #             j=6*i
    #             print '\t'.join(tds[j:j+6])
    #         # print tds
 
def main():
#    urli=["600360","600030","600060","600090","600180","601030","601060","601090","601180","601360","600035","600063","600091","601035","601063","601091","620035","620063","620182","620364","620091X"]
   # urli=["600360","600030","600060","600090","600180","600035","600063","600091"]
   # urli=["600360"]
#    urla, urlb = "http://www.cmbchina.com/cfweb/Personal/productdetail.aspx?code=","&type=prodvalue&PageNo="
    urli=["https://tpa.acs.org/session/acsnm251/CATL/computational-chemistry-across-catalysis"]
    get_contents(urli)


# main()

a={}
a.add('aa')
a.add('bb')


