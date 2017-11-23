import urllib3
import urllib3.request

# scrape pdf files on a web site

download_url_base = 'http://www.jossm.or.jp/series/flie/s'
download_url_ex = '.pdf'
download_url_num = 31;


for num in range(download_url_num):
	request_methods = urllib3.PoolManager()
	download_url = download_url_base+'%02d' % (num+1)+download_url_ex
	response = request_methods.request('GET', download_url)
	print(download_url)
	with open('src'+'%02d' % (num+1)+'.pdf', 'wb') as wfp:
	    wfp.write(response.data)

	# f = open('result.pdf', 'wb')
	# f.write(response.data)
	# f.close()


	# urllib3.request.urlretrieve(download_url, './') 

