import re
import csv

#initialization of variables
dflag = 1
amount = '"5"'
es='""'
weight ='"0.100"'
files = {'Food': 'food.txt', 'Clothes': 'clothes.txt', 'T-Shirts': 'shirts.txt'}
cat1 =''
number = int(input('Enter number catalog number: '))
f1 = open("check.html", "w")

#function for saving item 
def saveitem():
	global dflag 
	global number
	dflag=1 
	htmlstr = str(number)+' '+'<b>'+m[0]+'</b> <font color="blue">Price: '+m[1]+'</font><br>'
	if m[2] != '':
		htmlstr +='<i>'+m[2]+'</i><br>'
	f1.write(htmlstr+ '<br>\n')
	writer.writerow(
		('"XTSOL"', '"'+str(number)+'"', amount, '"0"', '"1"', '"default"', 
		es, '"0"', '"'+m[1]+'"', es, es, es, '"0"', '"1"', weight, es,
		'"0.00"', '"default"', '"0"', '"1"', '"0"', es,es,es,es, '"'+m[0]+'"',
		'"'+m[2]+'"', '"'+m[2]+'"', es, es, es, es, es, '"'+m[0]+'"', 
		'"'+m[2]+'"', '"'+m[2]+'"', es, es, es, 
		es, es, '"'+cat+'"', '"'+cat1+'"', es, es, es, es)
		)
	number += 1

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
for cat, current_file in files.items():
	f1.write('<h1>'+cat+': </h1>\n')
	f = open(current_file, "r", encoding="latin-1")

	for line in f:
		for ch in (chr(160), chr(172), chr(224), chr(128)): line=line.replace(ch,' ') 
		line=line.replace('"','&#34;')
		line=' '.join(line.split())
		if dflag == 0:
			if re.match('^\(.',line):
				line=(line.replace('(','')).replace(')','')
				m.append(line)
				dflag=2
			else:
				m.append('')
				saveitem()
 
		if dflag == 1:
			m1 = re.search('\d+,\d+', line)
			try:
				m=line.split(' '+m1.group(0))
				m[0] += m[1]
				m[1] = (m1.group(0)).replace(',','.')
				dflag=0
			except Exception:
				f1.write('<b><font color="red"> Something is wrong with "'+line+'" </font></b><br><br>\n')
		
		if dflag == 2:
			saveitem()

	dflag=1
	f.close

f1.write('</html>\n')
f1.close