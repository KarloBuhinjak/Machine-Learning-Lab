import urllib.request as ur
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris



# url koji sadrzi xml datoteku s mjerenjima:
url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=0&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017'

airQualityHR = ur.urlopen(url).read()
root = ET.fromstring(airQualityHR)

df = pd.DataFrame(columns=('mjerenje', 'vrijeme'))

i = 0
while True:

    try:
        obj = root[i]
    except:
        break

    row = dict(zip(['mjerenje', 'vrijeme'], [obj[0].text, obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = df.append(row_s)
    df.mjerenje[i] = float(df.mjerenje[i])
    i = i + 1

df.vrijeme = pd.to_datetime(df.vrijeme, utc=True)
#df.plot(y='mjerenje', x='vrijeme')
#plt.show()

# add date month and day designator
df['month'] = df['vrijeme'].dt.month
df['dayOfweek'] = df['vrijeme'].dt.dayofweek

#PRINTANJE PRVA TRI DATUMA KADA JE KONCENTRACIJA BILA NAJVEĆA
print(df.sort_values(['mjerenje']).tail(3))


#pd.set_option("display.max_rows", None, "display.max_columns", None)
#print(df)

#print(df.sort_values(['mjerenje']).tail(100))
#print(df.sort_values(by=['mjerenje']).head(3)['vrijeme'])


#print(df[df.mjerenje == 0])

#df = pd.DataFrame({'lab':df[df.mjerenje == 0].mjerenje, 'val':df["month"]})
#ax = df.plot.bar(x='val', y='lab')
#plt.show();



