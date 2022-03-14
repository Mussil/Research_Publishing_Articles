import json






population={'Above 1':(1,1000),'Alph':(1,3),'Beta':(4,6),'Gama':(7,9),'Delta':(10,12),'Above 13':(13,1000)}



def createDataByPop(source_dict,checkedYearInt):
    '''
    :param source_dict: the name of the file of the dict
    :param checkedYearInt: the year that been checked in integer
    :return: dict of the format:
    {
        <population name> :
            {
                <yearsArticle> : { <year> : [ ... int ... ] },
                <yearsUnique> : { <year> : [ ... int ... ] },
                <yearsNewAuthors> :  { <year> : [ ... int ... ] },
                <yearsNewArticleAuthors> : { <year> : [ ... int ... ] }
            }
    }


    '''
    checkedYear = str(checkedYearInt)

    dataOfAllPop = {}
    print("Started Reading JSON file")
    with open(source_dict, "r") as read_file:
        print("Converting JSON encoded data into Python dictionary mainDict")
        dictNew2 = json.load(read_file)

        for pop, amount in population.items():
            minimum, maximum = amount
            counter = 0
            data = {'yearsArticle': {}, 'yearsUnique': {}, 'yearsNewAuthors': {}, 'yearsNewArticleAuthors': {}}

            for year in range(checkedYearInt + 1, 2021):
                year = str(year)
                data['yearsArticle'][year] = []
                data['yearsUnique'][year] = []
                data['yearsNewAuthors'][year] = []
                data['yearsNewArticleAuthors'][year] = []

            for author, inside in dictNew2.items():
                # all2010= inside.get(checkedYear,0)
                articals2010 = 0
                all2010 = inside.get(checkedYear, 0)

                if not all2010:  # this author doesnt has anything in 2010
                    continue

                articals2010 = all2010.get('numArticle', 0)

                if minimum <= articals2010 <= maximum:
                    counter += 1
                    pass
                else:
                    continue

                for year in range(checkedYearInt + 1, 2021):
                    year = str(year)

                    if inside.get(year, 0):
                        value = inside[year]
                        data['yearsArticle'][year].append(value['numArticle'])
                        data['yearsUnique'][year].append(value['numUniqueAuthors'])
                        data['yearsNewAuthors'][year].append(value['newAuthors'])
                        data['yearsNewArticleAuthors'][year].append(value['numNewArticleAuthors'])
                    else:
                        data['yearsArticle'][year].append(0)
                        data['yearsUnique'][year].append(0)
                        data['yearsNewAuthors'][year].append(0)
                        data['yearsNewArticleAuthors'][year].append(0)

            dataOfAllPop[pop] = data

    return dataOfAllPop





if __name__=='__main__':
    source_dict = 'dicts/dictArxivShort.json'
    dict=createDataByPop(source_dict,checkedYearInt=2010)
    print(dict)
    # add
    with open('ArXivDataOfAllPopBycategoryByYear.json', 'w') as file:
        file.write(json.dumps(dict))  # use `json.loads` to do the reverse
