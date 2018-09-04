var winStyle = 'menubar,toolbar,location,status,scrollbars,resizable'

function getSequence(geneSymbol, seqtype) 
{
  winRef=window.open("GetSequence?geneSymbol="+geneSymbol+"&type="+seqtype, 'seq', 'width=700,height=350,resizable=yes,menubar=yes,scrollBars=yes')
  winRef.focus()
}

function tairGene(locus)
{
  window.location="http://www.arabidopsis.org/servlets/TairObject?type=locus&name="+locus;
}

function tairGermplasm(abrcStock)
{
window.location="http://www.arabidopsis.org/servlets/Search?type=general&action=detail&sub_type=germplasm&name="+abrcStock;
}

function tigrGeneIndex(id, species)
{
  var winRef;
  if (id.indexOf("NP") == 0)
    {	
      winRef=window.open("http://www.tigr.org/tigr-scripts/tgi/egad_report.pl?htnum="+id, 'tigr', winStyle);
    }
  else
    {		  
      var script;
      if (id.indexOf("TC") == 0)
	script = "tc_report.pl?tc="+id;
      else       
	script = "est_report.pl?EST="+id;
      if (species.indexOf("Ice Plant") >= 0)
	species = "ice_plant"
      else if (species.indexOf("Bird") >= 0)
	species = "L.japonicus"
      else if (species.indexOf("Model alga") >= 0)
	species = "c_reinhardtii"

	  winRef=window.open("http://www.tigr.org/tigr-scripts/tgi/"+script+"&species="+species, 'tigr', winStyle);
    }
  winRef.focus();
}

function nascArrays(locus, affyId)
{
  //winRef=window.open("http://ssbdjc2.nottingham.ac.uk/narrays/spothistory.pl?selection=no&searchfor=AGI&id="+locus, 'nasc')
  //winRef=window.open("http://128.243.111.177/narrays/spothistory.pl?searchfor=ATH1PS&id="+affyId, 'nasc');
  //winRef.focus()  
    window.location="http://128.243.111.177/narrays/spothistory.pl?searchfor=ATH1PS&id="+affyId
}

function showPic(image, width, height, title)
{
  winRef=window.open('', 'image', 'menubar=0,toolbar=0,status=0,scrollbars=1,resizable=1')
  winRef.resizeTo(width, height)
  winRef.document.writeln('<html><head><title>'+title+'</title></head>'
    +'<body style="margin: 0;" onLoad="self.focus()"><img src='+image+'></body></html>'  )
  winRef.document.close()
}
     
function popup(page, width, height)
{
  winRef=window.open(page,'', 'menubar=0,toolbar=0,status=0,scrollbars=1,resizable=1');
  winRef.resizeTo(width, height);
  winRef.focus();
}

