from lxml import html
import requests
from decimal import Decimal
from math import inf as infinity
from sys import argv


strip = lambda price: Decimal(price.strip('\n\tÂ£+ postage'))

print('\n\nWorking...\n\n')

lowest, highest = infinity, 0
total, count = Decimal(0), Decimal(0)
for page_number in range(1, 11):

  page = requests.get(argv[1], params={'LH_Sold': 1, 'LH_Complete': 1, '_ipg': 200, '_pgn': page_number})
  tree = html.fromstring(page.content)
  lvprices = tree.find_class('lvprices')

  if page_number == 1: print(page.url, '\n');
  print ('Page %s of 10' % page_number)

  for elem in lvprices:
    subtotal = Decimal(0)
    # single price? continue
    try: subtotal += strip(elem.find_class('bidsold')[0].text)
    except: continue
    # postage fee? add to price
    try: subtotal += strip(elem.find_class('fee')[0].text)
    except: pass

    count += 1; total += subtotal
    if subtotal > highest: highest = subtotal
    if subtotal < lowest: lowest = subtotal

  print ('Average:',  (total / count))
  print('Highest:', highest, '     Lowest:', lowest)
  print()


#  count purchase frequency
#  date of earliest sale per page