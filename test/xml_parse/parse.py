import xml.etree.ElementTree as ET
tree = ET.parse('abc')
for n in tree.findall('country'):

	print n.attrib['name']
	
	for c in n.getchildren():
		print "\t",
		print c.tag, c.text,
		if c.attrib :
		#or print c.attribute anyway
			print "attributes : ",c.attrib
		else : 
			print ''
