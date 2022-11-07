


import pandas as pd

mtcars = pd.read_csv('mtcars.csv')
print(mtcars.sort_values(by=['mpg']).head(5)['car'])# -> 1. Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)
#print(mtcars[mtcars.cyl == 8].sort_values(by=['mpg']).tail(3))->2. Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
#print(mtcars[mtcars.cyl == 6].mpg.mean())->mtcars[mtcars.cyl == 8]
#print(mtcars[(mtcars.cyl == 4) & (mtcars.wt > 2.0) & (mtcars.wt < 2.2)].mpg.mean()) ->Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
#print(mtcars[mtcars.am == True].count().car)->Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
#print(mtcars[mtcars.am == False].count().car)
#print(mtcars[(mtcars.am == True) & (mtcars.hp>100)].count().car)->Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
#mtcars['kg']=mtcars['wt']*1000*0.453 -> Kolika je masa svakog automobila u kilogramima?



