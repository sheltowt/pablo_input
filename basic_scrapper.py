import urllib2
from BeautifulSoup import BeautifulSoup

# using beautiful soup library and urllib2 to pull web page, and create beautiful soup object 
soup = BeautifulSoup(urllib2.urlopen('http://www.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0DNgxf_JK1wZTe2nEAxo_0oZfgXPsWuRSI8v-AvmK0rfcvUEzaLdkFmVIHgF9jKnZfPy_hDvcUU3bb6SF0J_Oljve9IBsU7KPv2doFMiaKDXShl67Q9zVMHyt1HGPtmCOFxHU5tRkJMdqrBsNOts0Mva-Zx4EiqAnFqrhLzdiZzd_o-Jiv5L9_peSN-tVdCbN9HtLgfeGuqU81yWAOu7LGuYgBxtG1iWlQ8uy1pf-e_v22Kgv951ypRvfvaS259SH9x9I5Eic2pYwLNZrsiiktg2QhHApKrb-di3BTjjyPGvqMkZ7Qe2JlImAm755k3l0G-YyPqde5igMLkw_V72cQD21vI2eYHmVEXkuPA_uUFHi5BdPon6u-kfdae1ccNmqBptfjJz_r4JGvOHwn-e0v9MFNxIiirrEx7sNxajlsNOC4QLl_cXnVubUrNBYU88qeeKOL16l6vtUMKQYnDbhoY7jT-hCXpbe_LLZNspDeOqzkldF0WFXzLPQDTuOiQ9V6iQWEk6QI4yYLDDfqR5GtZmBU2UjK7B0Y=&p=1&sk=&fvj=0&tk=1aqi0mv920k4i2h6&jsa=1586&oc=1&sal=0').read())


# instantiate empty list
output = []


# pull all li tags from html appending them to the output list
for li in soup.findAll('li'):
	output.append(li.string)


# pull all p tags from html appending them to the output list
for p in soup.findAll('p'):
	output.append(p.string)

# checking out output
print(output)

#opening text file
f = open('./tmp/scrape.txt','w')

#looping through our extracted text line by line
for line in output:
	#writing text to file line by line, adding a new line delimiter at the end of the line
	f.write(str(line)+'\n') 

#closing the text file
f.close() 

