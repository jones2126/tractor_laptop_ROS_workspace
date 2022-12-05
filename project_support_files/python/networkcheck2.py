import urllib2
print 'accessing google'
def internet_on():
	try:
		urllib2.urlopen('http://172.217.15.110', timeout=1)
		print 'access sucessful'
		return True
	except urllib2.URLError as err: 
		print 'access failed'
		return False