# -*- coding: latin-1 -*-
from BeautifulSoup import BeautifulSoup
import urllib2
import re
import sys
import os
import os.path

debug = 10
images = set()
#html_page = urllib2.urlopen("http://imgur.com")
#htmlFile = open(sys.argv[1])
for htmlFile in os.listdir("."):
    if os.path.isfile(htmlFile):
        if debug > 0:
            print "file "+htmlFile
            debug -= 1
        try:
            soup = BeautifulSoup(open(htmlFile).read())
            for img in soup.findAll('img'):
                images.add(img.get('src'))
        except:
            pass

print("Number of images = %d\n"%len(images))
#print(images)
outfile = open("all_images_list.txt", 'w')
for i in sorted(images):
    outfile.write(i+"\n")
