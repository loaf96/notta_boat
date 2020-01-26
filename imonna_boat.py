from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

# setup base url and replace chrome with webdriver of one's chosing

web = 'https://www.getmyboat.com/boat-rental/'
browser = Browser('chrome')

# open and visit url 
browser.visit(web)

# use to scrape the site

gt_u = []
igt_u = []
for x in range (0,301):
    html = browser.url
    site = requests.get(html)
    soup = BeautifulSoup(site.text, 'lxml')
    dat_data = soup.find_all('div', attrs={'class': '_16Y5Y'})
    lky_data = soup.find_all('div', attrs={'class': '_3hhau'})
    lkat_dat = soup.find_all('a', attrs={'class': 'Shx4x'})
    dat_all = [dat_data, lkat_dat, lky_data]
    gt_u.append(dat_all)
    try:
        browser.find_by_text('Next').first.click()
    except:
        'WebDriverException'
        print('Expected to be seen at end of page grouping....\nIf seen before'\
             'hand you may have not collected all the data')

# lists created to hold the data that will be transformed into a dictionary

info = {'time_incr':[], 'rate':[], 'descrp':[], 'num_guests':[]}

# used to put all of the categories form each page into one dictionary
# that will be used to make the csv file

for x in gt_u:
    for y in x[0]:
        gttm = y.text
        spltter = gttm.split('$')
        info['rate'].append(spltter[1])
        info['time_incr'].append(spltter[0])
    for z in x[1]:
        info['descrp'].append(z.text)
    for w in x[2]:
        info['num_guests'].append(w.text)

# puts it into a csv file

dat_frame = pd.DataFrame(info)
dat_frame.to_csv('scrprman.csv', index=False)
pd.read_csv('scrprman.csv').head()