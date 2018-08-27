import sys
import re
from BeautifulSoup import BeautifulSoup

def replaceWeirdChars(original):
    sys.stderr.write("got submatch: %s\n"%original)
    #rtext = re.sub(r"\?|=|\+", "_", submatch.group(1))
    rtext = original.replace("?", "_")
    rtext = rtext.replace("&", "_")
    rtext = rtext.replace("+", "_")
    rtext = rtext.replace("=", "_")
    if rtext.endswith("enlarged_1"):
        rtext = rtext[:-2]
    return rtext

filename = sys.argv[1]
F = open(filename)
soup = BeautifulSoup(F.read())
F.close()
found = False
for a in soup.findAll('a'):
    if 'BlastResults' in a['href'] or 'SeedGeneProfile' in a['href'] or 'SearchMutants' in a['href'] or 'EmbryoPhenotype' in a['href'] or 'InsertBorder' in a['href'] or 'MutantList' in a['href'] or 'NomarskiImages' in a['href'] or 'TargetPDetails' in a['href']:
        a['href'] = replaceWeirdChars(a['href'])
        found = True

if found:
    F = open(sys.argv[1], 'w')
    F.write(str(soup))



'''
BlastResults?geneSymbol=ABP+1
BlastResults?geneSymbol=ACC+1
BlastResults?geneSymbol=ADL+1A
BlastResults?geneSymbol=AESP
SeedGeneProfile?allAlleles=Y&geneSymbol=ADL+1A
SeedGeneProfile?geneSymbol=ADL+1A
SeedGeneProfile?geneSymbol=ADL+1A&alleleSymbol=adl+1A-2

prefixes to fix:
BlastResults
EmbryoPhenotype
InsertBorder
MutantList
NomarskiImages
SearchMutants
SeedGeneProfile
TargetPDetails
'''
