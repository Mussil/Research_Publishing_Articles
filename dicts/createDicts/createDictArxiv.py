'''
make a dictionary of analyzed data
----------------------------
the full dictionary format:
{
    <author name> :
    [
        { <year> :
            {
                <numArticle>: int,
                <numUniqueAuthors>: int,
                <newAuthors>: int,
                <numNewArticleAuthors>: int, ###this attr count the articles for author that he published with at least one new author
                <listAuthors> : [ ... <author name> ...] ###this is all the authors that co-publish in this year
            }
        } ,

        [ ... <author name> ...] ###this is all the authors that co-publish in all the year

    ]
}

----------------------------
the short dictionary format:
{
    <author name> :
    { <year> :
        {
            <numArticle>: int,
            <numUniqueAuthors>: int,
            <newAuthors>: int,
            <numNewArticleAuthors>: int
        }
    }
}
'''

import json

#global attr
data = {}
shortData = {}

def addToData(author,date,authors):
    '''
    :param author: the new author that will be added
    :param date:  the date the article published
    :param authors: the other authors that co-publish this article
    :return:
    '''
    insideData={}
    insideData['numArticle']=1
    lenAuthors=len(authors)
    if lenAuthors==0:
        lenAuthors=1
    insideData['numUniqueAuthors']=lenAuthors-1 ##all the authors exluded this one
    insideData['newAuthors']=lenAuthors-1 #number of authors for this article.
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
    TotalListAuthors.extend(authors) #all the authors that ever he workes with including himself

    yearsDict={}
    yearsDict[date]=insideData

    data[author]=(yearsDict,TotalListAuthors)


    #for the short dict
    insideDataShort={}
    insideDataShort['numArticle']=insideData['numArticle']
    insideDataShort['numUniqueAuthors']=insideData['numUniqueAuthors']
    insideDataShort['newAuthors']=insideData['newAuthors']
    insideDataShort['numNewArticleAuthors']=insideData['numNewArticleAuthors']
    yearsDictShort={}
    yearsDictShort[date]=insideDataShort
    shortData[author]=yearsDictShort


def updataData(author,date,authors):
    '''
    update data for author that exist
    :param author: author to change data on
    :param date: the date the article published
    :param authors: other authors that co-publish this article
    :return:
    '''
    yearsDict , TotalListAuthors= data.get(author)
    yearsDictShort=shortData.get(author) #addition for the short dict


    if yearsDict.get(date): #the author already published  this year
        insideData=yearsDict.get(date)
        insideDataShort=yearsDictShort.get(date)#addition for the short dict

        insideData['numArticle'] += 1
        insideDataShort['numArticle'] += 1 #addition for the short dict

        numNewArticleAuthors=0
        for other in authors:
            if other not in TotalListAuthors:
                TotalListAuthors.append(other)
                insideData['newAuthors'] += 1
                insideDataShort['newAuthors'] += 1 #addition for the short dict

                numNewArticleAuthors=1
            if other not in insideData['listAuthors']:
                insideData['listAuthors'].append(other)
                insideData['numUniqueAuthors']+=1
                insideDataShort['numUniqueAuthors']+=1  #addition for the short dict

        insideData['numNewArticleAuthors']+=numNewArticleAuthors
        insideDataShort['numNewArticleAuthors']+=numNewArticleAuthors  #addition for the short dict



    else: #it is a new year for the author
        insideData = {}
        insideDataShort = {}  #addition for the short dict

        insideData['numArticle'] = 1
        insideDataShort['numArticle'] = 1 #addition for the short dict

        lenAuthor=len(authors)
        if lenAuthor==0:
            lenAuthor=1
        insideData['numUniqueAuthors'] = lenAuthor-1
        insideDataShort['numUniqueAuthors'] = lenAuthor-1#addition for the short dict

        insideData['newAuthors']=0
        insideDataShort['newAuthors']=0  #addition for the short dict

        numNewArticleAuthors=0

        for other in authors:
            if other not in TotalListAuthors:
                TotalListAuthors.append(other)
                insideData['newAuthors']+=1
                insideDataShort['newAuthors']+=1 #addition for the short dict

                numNewArticleAuthors=1
        insideData['numNewArticleAuthors']=numNewArticleAuthors
        insideDataShort['numNewArticleAuthors']=numNewArticleAuthors #addition for the short dict

        listAuthors = []
        listAuthors.extend(authors) # all the authors that he workes with him this year
        insideData['listAuthors'] = listAuthors # including himself


    yearsDict[date] = insideData
    data[author]=(yearsDict,TotalListAuthors)

    #addition for the short dict
    yearsDictShort[date]=insideDataShort
    shortData[author]=yearsDictShort
    ##end add



if __name__=='__main__':
    path='../'
    source_json ='../../data/modifiedData/arxiv.json'
    dest_dict = path+'dictArxivFull.json'
    dest_dict_short = path+'dictArxivShort.json'

    moreThen10 = 0
    lessThen10 = 0



    with open(source_json, "r") as read_file:
        data_json = json.load(read_file)
        for dict in data_json:

            authors_temp = dict.get("authors_parsed")
            # Convert List of lists to list of Strings
            authors = [' '.join(ele[:2]) for ele in authors_temp] #take only the first 2 names of author

            if len(authors) > 10: #Skip articles written by more than 10 authors
                moreThen10 += 1
                continue
            lessThen10 += 1

            date = dict.get("versions")
            v1 = date[0]['created']
            _, date = v1.split(', ')

            day, month, year, time, gmt = date.split(' ')
            date = year #decide weather to choose by months or year. now it by years

            for author in authors:
                if author in data:
                    updataData(author, date, authors)

                else:  # new author
                    addToData(author, date, authors)

    print(f"articles written by more than 10 authors:{moreThen10}")
    print(f"articles written by less of equal to 10 authors:{lessThen10}")



    with open(dest_dict, 'w') as file:
        file.write(json.dumps(data)) # use `json.loads` to do the reverse

    # add
    with open(dest_dict_short, 'w') as file:
        file.write(json.dumps(shortData))  # use `json.loads` to do the reverse


