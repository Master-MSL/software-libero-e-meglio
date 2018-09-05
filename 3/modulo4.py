import urllib
import re
from collections import OrderedDict

prkhrs = [] #{}
for i in range(0,100, 100):
##    url="https://it.search.yahoo.com/search?n=100&ei=UTF-8&va_vt=any&vo_vt=any&ve_vt=any&vp_vt=any&vf=all&vc=it&vm=i&fl=0&p=%22opendata%22+.comune.*.it&fr=yfp-t-909&b=" + ( "%d" % (i) )
    url='https://search.yahoo.com/search?n=100&ei=UTF-8&va_vt=any&vo_vt=any&ve_vt=any&vp_vt=any&vf=all&vc=it&vm=i&fl=0&p=%22libre office%22.comune.*.to.it&fr=yfp-t-909&b=' + ( "%d" % (i) )
    ##url='https://search.yahoo.com/search?n=100&ei=UTF-8&va_vt=any&vo_vt=any&ve_vt=any&vp_vt=any&vf=all&vc=it&vm=i&fl=0&p="openoffice"+%20comune.*.to.it&fr=yfp-t-909&&b=' + ( "%d" % (i) )
##    source = urllib.urlopen('https://search.yahoo.com/search?n=100&ei=UTF-8&va_vt=any&vo_vt=any&ve_vt=any&vp_vt=any&vf=all&vc=it&vm=i&fl=0&p=%22qgis%22&vs=..it')
    source = urllib.urlopen(url)
    ##page = source.read()
    page = source.readlines()
##   prkhrs = [] #{}

    parolachiave = 'comune'

    for line in page:
        if parolachiave in line:
            list_items = line.split('<div><span class=" fz-15px')
            if len(list_items)>0:
                for i in range(len(list_items)):
                    inizio = list_items[i].find(parolachiave)
                    fine = list_items[i].find('/',inizio)

                    s = list_items[i][inizio:fine].replace('<b>','').replace('<','')
                    prkhrs.append(s)

for x in list(OrderedDict.fromkeys(prkhrs)):
    print x
