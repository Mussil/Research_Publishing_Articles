#Creates a data structure that summarizes the data
#general example:
#{ name of author:
# [{year:  {'numArticle': , 'numUniqueAuthors': , 'newAuthors': , 'listAuthors': [List of co-authors throughout this year only] } ,
# [List of co-authors throughout the years] ]
# }

import json
import lxml.etree as etree

allTags=['article','inproceedings','proceedings']
source_xml='../../data/modifiedData/dblp.json'
path = '../'
dest_dict = path + 'dictDBLPFull.json'
dest_dict_short = path + 'dictDBLPShort.json'


def getelements():
    context = iter(etree.iterparse(source_xml, events=('start', 'end'),load_dtd=True))
    _, root = next(context) # get root element
    for event, elem in context:
        if event == 'end' and elem.tag in allTags:
            yield elem
            root.clear() # free memory


data={}
shortData={}


def addToData(author,year,authors):
    insideData={}
    insideData['numArticle']=1
    lenAuthor=len(authors)
    if lenAuthor==0:
        lenAuthor=1
    insideData['numUniqueAuthors']=lenAuthor-1
    insideData['newAuthors']=lenAuthor-1 #number of authors for this article.
    # it is a new author this is why all the other are new to him


    ######addition
    if len(authors)>1: #more authors for this article
        insideData['numNewArticleAuthors']=1
    else: # the author wrote an article by himself
        insideData['numNewArticleAuthors']=0




    listAuthors=[]
    listAuthors.extend(authors) #all the authors that he workes with this year
    insideData['listAuthors']=listAuthors #including himself

    TotalListAuthors=[]
    TotalListAuthors.extend(authors) #all the authors that ever he workes with #including himself

    yearsDict={}
    yearsDict[year]=insideData

    data[author]=(yearsDict,TotalListAuthors)


    ##add
    insideDataShort={}
    insideDataShort['numArticle']=insideData['numArticle']
    insideDataShort['numUniqueAuthors']=insideData['numUniqueAuthors']
    insideDataShort['newAuthors']=insideData['newAuthors']
    insideDataShort['numNewArticleAuthors']=insideData['numNewArticleAuthors']
    yearsDictShort={}
    yearsDictShort[year]=insideDataShort
    shortData[author]=yearsDictShort
    ##end add


def updataData(author,year,authors): #update data for author that exist
    yearsDict , TotalListAuthors= data.get(author)
    yearsDictShort=shortData.get(author) #add 8

    if yearsDict.get(year): #the author already advertised in this year
        insideData=yearsDict.get(year)
        insideDataShort=yearsDictShort.get(year) #add 8


        insideData['numArticle'] += 1
        insideDataShort['numArticle'] += 1 #add 8

        numNewArticleAuthors=0
        for other in authors:
            if other not in TotalListAuthors:
                TotalListAuthors.append(other)
                insideData['newAuthors'] += 1
                insideDataShort['newAuthors'] += 1 #add 8

                numNewArticleAuthors=1
            if other not in insideData['listAuthors']:
                insideData['listAuthors'].append(other)
                insideData['numUniqueAuthors']+=1
                insideDataShort['numUniqueAuthors']+=1  #add 8


        insideData['numNewArticleAuthors']+=numNewArticleAuthors
        insideDataShort['numNewArticleAuthors']+=numNewArticleAuthors  #add 8



    else: #it is a new year for the author
        insideData = {}
        insideDataShort = {}  #add 8

        insideData['numArticle'] = 1
        insideDataShort['numArticle'] = 1 #add 8

        lenAuthor=len(authors)
        if lenAuthor==0:
            lenAuthor=1
        insideData['numUniqueAuthors'] = lenAuthor-1
        insideDataShort['numUniqueAuthors'] = lenAuthor-1 #add 8

        insideData['newAuthors']=0
        insideDataShort['newAuthors']=0  #add 8


        numNewArticleAuthors=0

        for other in authors:
            if other not in TotalListAuthors:
                TotalListAuthors.append(other)
                insideData['newAuthors']+=1
                insideDataShort['newAuthors']+=1 #add 8

                numNewArticleAuthors=1
        insideData['numNewArticleAuthors']=numNewArticleAuthors
        insideDataShort['numNewArticleAuthors']=numNewArticleAuthors #add 8

        listAuthors = []
        listAuthors.extend(authors) # all the authors that he workes with this year
        insideData['listAuthors'] = listAuthors # including himself


    yearsDict[year] = insideData
    data[author]=(yearsDict,TotalListAuthors)

    ##add
    yearsDictShort[year]=insideDataShort
    shortData[author]=yearsDictShort
    ##end add


counter=0
moreThen10=0
lessThen10=0

for page in getelements():
    year=page.find('year').text
    authors=page.findall('author')
    authors = list(map(lambda x: x.text, authors))

    if len(authors) > 10:
        moreThen10 += 1
        continue
    lessThen10 += 1


    # print(authors)
    for author in authors:
        if author in data:
            updataData(author,year,authors)

        else : #new author
            addToData(author,year,authors)

# print(data)
print("more"+str(moreThen10))
print("less"+str(lessThen10))


with open(dest_dict, 'w') as file:
    file.write(json.dumps(data)) # use `json.loads` to do the reverse


#add
with open(dest_dict_short, 'w') as file:
    file.write(json.dumps(shortData)) # use `json.loads` to do the reverse