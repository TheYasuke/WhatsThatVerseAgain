'''#scripture scraper from google- takes phrases  - select preferred bible version - first page of search
    -shows scriptures that relate

    1. inputs phrase ex- "But none shall perish"
       inputs version ex-   "KJV"
    2. Outputs scripture options ex  "1.  2 Peter 3:9 - The Lord is not slow to.....   "
    								 "2.  John 3:15 - That whosoever believeth...	"
    3. Click on scripture to get full view
    4. Optional? Re-search option to grab more results (may change search engine or grab from more than 1 page)
    5. if no results/not what your looking for "Try being broad with the phrase. "

    - from input phrase insert "scripture" after phrase for newphrase
    - put newphrase in search engine and search (for now) the first page.
    - scrape that pages titles for scriptures based on 66 books. Maybe search looking for : between numbers. Use regex 
    - when scriptures are identified, such as "2 Peter 3:9" on a google page, the number of occurences of scriptures found are counted. (This determines the order)
    - using the scriptures names found, use a bible site to get the full verse with the version that was input.
    - list scriptures which become the options to choose from
'''

'''
    Todo: remove multiple instances of same verse  "2 Peter 3:9 and 2 Pet. 3:9" (like if definition is same, take longer verse)
    Todo: seaching... dialog
    Todo: optomize speed
    Todo: add verse compare
    Todo: number results
    Todo: search history
    Todo: 
'''
import requests, re, itertools
from pprint import pprint
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

phrase = "then came john baptizing"
version = "nkjv"
aResults = 10
aPages = 0
bibleDict = {}
passageDict = {}


def main(phrase,version,aResults,aPages):
        
    try:
        webSearch(phrase, aResults, aPages, bibleDict)
    except:        
        return "No connection. Please check your connection."

    verzBool = bibleSearch(version) 
    
    if type(verzBool) is bool:
        return False
    
    return passageDict
    

def bibleSearch(myVersion):

    #1 Order items in dictionary by most occurences to least based on value
    searchDict = (dict(sorted(bibleDict.items(), key=lambda x: x[1], reverse=True)))
    #print (searchDict)
    #2 '''This and the "if not bibleDict" line below is added because it will not return False unless the version is first evaluated before the bibleDict. The only way to do this was to pretend that there was content, check to see if the version was bad, and then really check if there was content in the dictionary. shrewd tactic but it works til a better solution is found'''

    if not searchDict:   #the only reason i want this to continue is for the "if error" statement below
        searchDict["1"]= "2"
    
    for verse in searchDict:
        #3 take the verse and specified version and search for passage
        searchVerse = '+'.join(verse.split())
            
        URL="https://www.biblegateway.com/passage/?search=%s&version=%s" % (searchVerse, myVersion)
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        #4 if version specified results in error. break
        error = soup.find(class_="version-option")

        if error:
            print('Invalid Version')
            return False
           #break
        if not bibleDict:
            return
        #5 create object to capture passages
        results=soup.find(class_="version-%s result-text-style-normal text-html"%(myVersion.upper()))
        # print (results)
        results2= results.find_all("p")
        #6 take out footnotese of passages
        footnotes=results.find_all(class_=('footnote'))
        for feet in footnotes:
            feet.extract()
        #7 Take out cross references
        crossreference=results.find_all(class_=('crossreference'))
        for reference in crossreference:
            reference.extract()
        #8 for every verse place verse and passage in dictionary.
        for each in results2:
            #pprint (each.text)
            if verse not in passageDict:
                passageDict[verse] = each.text.replace(u'\xa0', u' ')
            else:
                passageDict[verse] += " "+each.text.replace(u'\xa0', u' ')


    #searches search engine for phrase + scripture
def webSearch(myPhrase,myResults, myPages,myDict):
    #1 Takes phrase adds it to google search query and makes bs4 object
    
    searchPhrase = '+'.join(myPhrase.split())
    URL="https://www.google.com/search?q=%s+scripture&num=%d" % (searchPhrase, myResults)
    URL2 ="https://www.ecosia.org/search?q=%s+scripture&p=%d" % (searchPhrase, myPages)
    
    page = requests.get(URL, headers=headers)
    page2= requests.get(URL2, headers=headers)
    page3=""
    #1.5 add each new ecosia page to results
    if myPages > 0:
        for each in range(myPages+1):
            page3+=requests.get("https://www.ecosia.org/search?q=%s+scripture&p=%d" % (searchPhrase, each), headers=headers).text
    
    soup = BeautifulSoup(page.text, 'html.parser')
    soup2 = BeautifulSoup(page2.text+page3, 'html.parser')

    #2 Searches google search for every title of search page.
    results=soup.find_all(class_="LC20lb")
    
    results2=soup2.find_all(class_="result-title js-result-title")
    #3 Open the file with bible books listed and reads from them
    bibleFile = open('BibleBooks.txt')
    content = bibleFile.readlines()
    

    #4 For every title found we do the following
    for title in itertools.zip_longest(results, results2):
        #5 For every book in the bible do the following for every title in the search
        for book in content:
            #6 regex pattern created to match bible ## book ##-##
            versePattern =r'(\d )*'+book.strip('\n') + " " +r'([0-1]?\d{1,2}:{1}[0-1]?\d{1,2}(-[0-1]?\d{1,2})?)'
            verseRegx = re.compile(versePattern)

            #7 search each title in google for matching verse of bible. If matching verse is found add to dictionary and add value of 1. If verse is already in dictionary increase value by 1            
            if hasattr(title[0],'text'):
                verse = verseRegx.search(title[0].text)
                if verse:
                    if verse.group() not in myDict: 
                        myDict[verse.group()]= 1
                    else:
                        myDict[verse.group()]+= 1
            if hasattr(title[1],'text'):
                verse2 = verseRegx.search(title[1].text)
                if verse2:
                    if verse2.group() not in myDict: 
                        myDict[verse2.group()]= 1
                    else:
                        myDict[verse2.group()]+= 1

    
    bibleFile.close()
     
#print(main(phrase,version,aResults,5))
