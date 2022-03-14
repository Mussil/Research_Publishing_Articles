#This file takes a source file and creates a destination file after sorting
#The sorting method is by passing on each year from 1936 and up in a loop
# and find all of the articles from this year

import lxml.etree as etree

allTags=['article','inproceedings','proceedings']

source_xml='../modifiedData/filteredDBLP.json'
dest_xml='../modifiedData/dblp.json'



def getelements():
    context = iter(etree.iterparse(source_xml, events=('start', 'end'),load_dtd=True))
    _, root = next(context) # get root element
    for event, elem in context:
        if event == 'end' and elem.tag in allTags:
            yield elem
            root.clear() # free memory



def keep(page,year):
    yearPage=page.find('year').text
    if str(year)==yearPage:
        return True
    return False



with open(dest_xml, 'wb') as file:
    # start root
    file.write(b'<?xml version="1.0" encoding="ISO-8859-1"?>\n')
    file.write(b'<!DOCTYPE dblp SYSTEM "dblp.dtd">\n')
    file.write(b'<dblp>\n')
    counter=0
    for year in range(1936,2022):
        print("year: " ,year)
        for page in getelements():
            if keep(page,year):
                file.write(etree.tostring(page, encoding='utf-8'))
                counter+=1
                print(counter)
    # close root
    file.write(b'</dblp>')


print(counter)
