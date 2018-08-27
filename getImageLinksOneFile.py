from BeautifulSoup import BeautifulSoup
import urllib2
import re
import sys
import os
import os.path

debug = 10
images = set()
#html_page = urllib2.urlopen("http://imgur.com")
htmlFile = sys.argv[1]
if os.path.isfile(htmlFile):
    if debug > 0:
        print "file "+htmlFile
        debug -= 1
    F = open(htmlFile)
    soup = BeautifulSoup(F)
    for img in soup.findAll('img'):
        images.add(img.get('src'))

#print(images)
#outfile = open("all_images_list.txt", 'w')
for i in sorted(images):
    sys.stdout.write(i+"\n")
