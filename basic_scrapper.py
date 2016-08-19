import urllib2
from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://www.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0DNgxf_JK1wZTe2nEAxo_0oZfgXPsWuRSI8v-AvmK0rfcvUEzaLdkFmVIHgF9jKnZfPy_hDvcUU3bb6SF0J_Oljve9IBsU7KPv2doFMiaKDXShl67Q9zVMHyt1HGPtmCOFxHU5tRkJMdqrBsNOts0Mva-Zx4EiqAnFqrhLzdiZzd_o-Jiv5L9_peSN-tVdCbN9HtLgfeGuqU81yWAOu7LGuYgBxtG1iWlQ8uy1pf-e_v22Kgv951ypRvfvaS259SH9x9I5Eic2pYwLNZrsiiktg2QhHApKrb-di3BTjjyPGvqMkZ7Qe2JlImAm755k3l0G-YyPqde5igMLkw_V72cQD21vI2eYHmVEXkuPA_uUFHi5BdPon6u-kfdae1ccNmqBptfjJz_r4JGvOHwn-e0v9MFNxIiirrEx7sNxajlsNOC4QLl_cXnVubUrNBYU88qeeKOL16l6vtUMKQYnDbhoY7jT-hCXpbe_LLZNspDeOqzkldF0WFXzLPQDTuOiQ9V6iQWEk6QI4yYLDDfqR5GtZmBU2UjK7B0Y=&p=1&sk=&fvj=0&tk=1aqi0mv920k4i2h6&jsa=1586&oc=1&sal=0').read())

output = []

for li in soup.findAll('li'):
	output.append(li.string)

for p in soup.findAll('p'):
	output.append(p.string)

print(output)

f = open('./tmp/scrape.txt','w')
for line in output:
	f.write(str(line)+'\n') 
f.close() 

# for row in soup('table', {'class': 'spad'})[0].tbody('tr'):
#     tds = row('td')
#     print tds[0].string, tds[1].string