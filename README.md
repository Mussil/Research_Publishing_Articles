# Research - publishing articles
The basic data files are too large and therefore have not been uploaded to Githab, it can be downloaded from its site

## ArXiv:
[Download](https://www.kaggle.com/Cornell-University/arxiv)
* Skipped articles written by more than 10 authors<br>
* Amount of articles written by more than 10 authors: 65344
* Amount of articles written by less or equal to 10 authors: 1860365
* Sorted the data by the `versions` `version` :`v1` `created` field


### Preprocessing:
1. Make sure databases are in the `data/originalData` folder
    1. The `arxiv-metadata-oai-snapshot.json`
2. Run the script `data/prepareData/sortModifyArxiv.py` which sort the arXiv dataBase by date
3. Run the script `dicts/createDicts/createDictArxiv.py` to create the dictionary which contain only the necessary information after analyze.
<br> This will result two dictionary:
   1. `dicts/dictArxivFull.json` : which contain all the information for the analyzing
   2. `dicts/dictArxivShort.json` : which contain only the information needed for the analysis
4. Run the script `base.py` which will result the file `ArXivDataOfAllPopBycategoryByYear.json`
   <br>make sure the source and dest are: 
   ```
    source_dict = 'dicts/dictArxivShort.json'
    dest='ArXivDataOfAllPopBycategoryByYear.json'
   ```
----------------------------
## DBLP:
[Download dblp.xml and dblp.dtd](https://dblp.org/xml/)
<br>[What do I find in dblp.xml?](https://dblp.org/faq/16154937.html)
* Skipped articles written by more than 10 authors<br>
* Amount of articles written by more than 10 authors: 32142
* Amount of articles written by less or equal to 10 authors: 5487920

### Preprocessing:
1. Make sure databases are in the `data/originalData` folder
    1. The `dblp.xml`
    2. And the `dblp.dtd` (*Very important*)
2. Run the script `data/prepareData/filterDBLP.py` which filter the DBLP dataBase from certain labels
   keep only:  (5520291 articles left)
   1. article - label journals
   2. inproceedings 
   3. proceedings.
3. Run the script `data/prepareData/sortDBLP.py` which sort the DBLP by year and month
   If the dataBase of DBLP is updated to be after 2021, the range in this field should be changed
4. Run the script `dicts/createDicts/createDictDBLP.py` to create the dictionary which contain only the necessary information after analyze.
<br> This will result two dictionary:
   1. `dicts/dictDBLPFull.json` : which contain all the information for the analyzing
   2. `dicts/dictDBLPShort.json` : which contain only the information needed for the analysis
5. Run the script `base.py` which will result the file `DBLPDataOfAllPopBycategoryByYear.json`
   <br>make sure the source and dest are: 
   ```
    source_dict = 'dicts/dictDBLPShort.json'
    dest='DBLPDataOfAllPopBycategoryByYear.json'
   ```

## Auxiliary
**Meaning:**
* **numArticle** : number of articles written by this author this year
* **numUniqueAuthors** : number of co-writers this year for this author
    <br>*Unique* - indicates that if the co-author has participated in several articles he is counted once
* **newAuthors** : number of authors for this year who wrote an article together with this author for the first time
* **numNewArticleAuthors** : number of articles for this author for this year in which there are new writers

### The full dictionary format:
The purpose of the full dictionary is to keep all the data required for the short dictionary
```
{ 
   <author name> :
      [
         {<year> : 
            {
               'numArticle': int, 
               'numUniqueAuthors'>': int,
               'newAuthors': int,
               'numNewArticleAuthors': int
               'listAuthors': 
                  [List of names of co-authors throughout this year only] 
            }
         } ,
      [List of co-authors from all the years] ]
}
```
### The short dictionary format:
```
{
    <author name> :
    { <year> :
        {
            'numArticle': int,
            'numUniqueAuthors': int,
            'newAuthors': int,
            'numNewArticleAuthors': int
        }
    }
}
```


### Division into populations:
* Above 1 : 1 to 1000 (included)
* Above 13 : 13 and up
* Alph : 1 to 3 (included)
* Beta : 4 to 6 (included)
* Gama : 7 to 9 (included)
* Delta : 10 to 12 (included)

### Data based on population:
The files:<br>
* `ArXivDataOfAllPopBycategoryByYear.json`  
* `DBLP DataOfAllPopBycategoryByYear.json` 
<br>in the foramt of:
```
    {
        <population name> :
            {
                <yearsArticle> : { <year> : [ ... int ... ] },
                <yearsUnique> : { <year> : [ ... int ... ] },
                <yearsNewAuthors> :  { <year> : [ ... int ... ] },
                <yearsNewArticleAuthors> : { <year> : [ ... int ... ] }
            }
    }
```



