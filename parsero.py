import re
import csv

#initialization of variables
files = {'Food': 'food.txt', 'Clothes': 'clothes.txt', 'T-Shirts': 'shirts.txt'}
number = int(input('Enter number catalog number: '))
f1 = open("check.html", "w")

#Class for items
class ShopItem:
	amount = '"5"'
	es='""'
	weight ='"0.100"'
	cat1 =''
	m = []
	dflag = 1
	cat = ''

	def __init__(self,n):
		global number
		self.number=n

	def saveitem(self):
		self.dflag=1 
		htmlstr = str(self.number)+' '+'<b>'+self.m[0]+'</b> <font color="blue">Price: '+self.m[1]+'</font><br>'
		if self.m[2] != '':
			htmlstr +='<i>'+self.m[2]+'</i><br>'
		f1.write(htmlstr+ '<br>\n')
		writer.writerow(
			('"XTSOL"', '"'+str(self.number)+'"', self.amount, '"0"', '"1"', '"default"', 
			self.es, '"0"', '"'+self.m[1]+'"', self.es, self.es, self.es, '"0"', '"1"', self.weight, self.es,
			'"0.00"', '"default"', '"0"', '"1"', '"0"', self.es,self.es,self.es,self.es, '"'+self.m[0]+'"',
			'"'+self.m[2]+'"', '"'+self.m[2]+'"', self.es, self.es, self.es, self.es, self.es, '"'+self.m[0]+'"', 
			'"'+self.m[2]+'"', '"'+self.m[2]+'"', self.es, self.es, self.es, 
			self.es, self.es, '"'+self.cat+'"', '"'+self.cat1+'"', self.es, self.es, self.es, self.es)
			)
		self.number += 1

	def additem(self, line):
		m1 = re.search('\d+,\d+', line)
		try:
			self.m=line.split(' '+m1.group(0))
			self.m[0] += self.m[1]
			self.m[1] = (m1.group(0)).replace(',','.')
			self.dflag=0
		except Exception:
			f1.write('<b><font color="red"> Something is wrong with "'+line+'" </font></b><br><br>\n')

	def adddescription(self, line):
		if re.match('^\(.',line):
			line=(line.replace('(','')).replace(')','')
			self.m.append(line)
			self.dflag=2
		else:
			self.m.append('')
			self.saveitem()

	def getline(self, line):
		for ch in (chr(160), chr(172), chr(224), chr(128)): line=line.replace(ch,' ') 
		line=line.replace('"','&#34;')
		line=' '.join(line.split())
		if self.dflag == 0:
			self.adddescription(line) 
		if self.dflag == 1:
			self.additem(line)		
		if self.dflag == 2:
			self.saveitem()


#making headers in files
f1.write('<html><h1><font color="red">New items in shop</font></h1> \n')
writer = csv.writer(open('stocks.csv', 'w',  newline=''), delimiter ='\t', quotechar=None)
writer.writerow(
	('"XTSOL"', '"p_model"', '"p_stock"', '"p_sorting"', '"p_shipping"', '"p_tpl"', 
	'"p_manufacturer"', '"p_fsk18"', '"p_priceNoTax"', '"p_priceNoTax.1"', 
	'"p_priceNoTax.2"', '"p_priceNoTax.3"', '"p_tax"', '"p_status"', '"p_weight"', 
	'"p_ean"', '"p_disc"', '"p_opttpl"', '"p_vpe"', '"p_vpe_status"', '"p_vpe_value"', 
	'"p_image.1"', '"p_image.2"', '"p_image.3"', '"p_image"', '"p_name.de"', 
	'"p_desc.de"', '"p_shortdesc.de"', '"p_meta_title.de"', '"p_meta_desc.de"', 
	'"p_meta_key.de"', '"p_keywords.de"', '"p_url.de"', '"p_name.en"', 
	'"p_desc.en"', '"p_shortdesc.en"', '"p_meta_title.en"', '"p_meta_desc.en"',
	'"p_meta_key.en"', '"p_keywords.en"', '"p_url.en"', '"p_cat.0"', '"p_cat.1"', 
	'"p_cat.2"', '"p_cat.3"', '"p_cat.4"', '"p_cat.5"')
	)

#parsing items
item=ShopItem(number)
for cat, current_file in files.items():
	f1.write('<h1>'+cat+': </h1>\n')
	f = open(current_file, "r", encoding="latin-1")
	item.cat=cat
	for line in f:
		item.getline(line)	
	item.dflag=1
	f.close

f1.write('</html>\n')
f1.close