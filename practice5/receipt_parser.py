import re
with open('raw.txt', encoding='utf-8') as f:
    text=f.read()
print(text[:300])

prices_raw=re.findall(r'Стоимость\n([\d ]+,\d{2})',text)
print(prices_raw[:10])
prices=[]
for p in prices_raw:
    p=p.replace(" ",'').replace(',','.')
    prices.append(float(p))

total=sum(prices)
print("TOTAL:",total)
items=re.findall(r'\d+\.\n(.+)',text)
for item in items:
    print(item)

date=re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})',text)
datetime=date.group(1)
print(datetime)

pay=re.search(r'(Банковская карта|Наличные)',text)
if pay:
    pay_met=pay.group(1)
else:
    pay_met="Не найдено"
print(pay_met)

receipt={
    'items':items,
    'prices':prices,
    'total':total,
    'payment_method':pay_met,
    'datetime':datetime
}
print(receipt)
