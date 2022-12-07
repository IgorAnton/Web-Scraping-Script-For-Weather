import requests
from bs4 import BeautifulSoup

import tkinter as tk

from tkinter import ttk


window = tk.Tk()
window.title("Vremenska Prognoza")
window.resizable(False,False)
text = tk.Text(window, height=40, width = 40)
text.grid(row=0, column=0, sticky=tk.EW)

scrollbar = ttk.Scrollbar(window, orient='vertical', command=text.yview)
scrollbar.grid(row=0, column=1, sticky=tk.NS)
text['yscrollcommand'] = scrollbar.set


URL = "https://naslovi.net/vremenska-prognoza/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(class_="box")


curr = results.find(class_="w-curr-data")


dataTemp = curr.find(class_="w-curr-temp")

dataOther = curr.find_all(class_="w-curr-row")

print("DANAS: ")
print(dataTemp.text.strip())


for dO in dataOther :
    print(dO.text.strip())

print("----------------------------------------\n")

todayM = "DANAS: \n" + dataTemp.text.strip() +"\n"

for d in dataOther:
    todayM = todayM + d.text.strip() + "\n"

todayM = todayM + "----------------------------------------\n"

allDaysAhead = results.find_all(class_="w-row")




i = 0






for nextDay in reversed(allDaysAhead) :
    dayName = nextDay.find(class_="w-col-day").text.strip()
    dateN   = nextDay.find(class_="w-col-date-date").text.strip()
    minTemp = nextDay.find(class_="w-col-min").text.strip()
    maxTemp = nextDay.find(class_= "w-col-max").text.strip()
    percipType = nextDay.find(class_= "w-col-summary").text.strip()
    precip  = nextDay.find(class_ = "w-col-precip").text.strip()
    wind    = nextDay.find(class_ = "w-col-wind").text.strip()


    poruka = "DAN: " + dayName + "\n" + "DATUM: " + dateN + "\n" + "Min Temp: " + minTemp+ "\n" + "Max Temp: " + maxTemp+ "\n" +  "Padavine: " + precip + "\n" +"Tip padavine: " + percipType + "\n" + "Vetar: " + wind + "\n"
    poruka = poruka + "----------------------------------------\n"

    position = f'{-i}.0'
    text.insert( position , poruka)
    i = i+1

    print (poruka)


pos = f'{-1}.0'
text.insert('1.0',todayM)

window.mainloop()


