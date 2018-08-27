import sys
import re

def replaceWeirdChars(submatch):
    sys.stderr.write("got submatch: %s\n"%submatch.group(1))
    #rtext = re.sub(r"\?|=|\+", "_", submatch.group(1))
    rtext = submatch.group(1).replace("?", "_")
    rtext = rtext.replace("&", "_")
    rtext = rtext.replace("+", "_")
    rtext = rtext.replace("=", "_")
    if rtext.endswith("enlarged_1"):
        rtext = rtext[:-2]
    return rtext

debug = 10
getref = re.compile("(?<=href='BlastResults)(.+?')")
filename = sys.argv[1]
F = open(filename)
for line in F:
    rep = re.sub(getref, replaceWeirdChars, line)
    if rep != line:
        print "Hah:\n%s\n%s\n"%(line, rep)
        if debug > 0:
            debug -= 1
            sys.exit(0)


'''
2010_Analysis_Forms.pdf
2010_Forms_Instructions.pdf
ABRC_Seed_Stock.html
Abstract.html
AccessPage.html
AllEmbryoPhenotypes.html
BlastResults?geneSymbol=ABP+1
BlastResults?geneSymbol=ACC+1
BlastResults?geneSymbol=ADL+1A
BlastResults?geneSymbol=AESP
SeedGeneProfile?allAlleles=Y&geneSymbol=ADL+1A
SeedGeneProfile?geneSymbol=ADL+1A
SeedGeneProfile?geneSymbol=ADL+1A&alleleSymbol=adl+1A-2
'''
