# Research Publishing Articles

## ArXiv:

Skipped articles written by more than 10 authors<br>
Sorted the data by the `versions` `version` :`v1` `created` field
 
* Amount of articles written by more than 10 authors: 65344
* Amount of articles written by less or equal to 10 authors: 1860365

### Preprocessing:
1. Make sure databases are in the `data/originalData` folder
2. Run the script `data/prepareData/sortModifyArxiv.py` which sort the arXiv dataBase by date
3. Run the script `dicts/createDicts/createDictArxiv.py` to create the dictionary which contain only the necessary information after analyze.
<br> This will result two dictionary:
   1. `dicts/dictArxivFull.json` : which contain all the information for the analyzing
   2. `dicts/dictArxivShort.json` : which contain only the information needed for the analysis
4. Run the script `base.py` which will result the file `ArXivDataOfAllPopBycategoryByYear.json`

----------------------------
### The short dictionary format:
```
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
```
**Meaning:**
* **numArticle** : number of articles written by this author this year
* **numUniqueAuthors** : number of co-writers this year for this author
    <br>*Unique* - indicates that if the co-author has participated in several articles he is counted once
* **newAuthors** : number of authors for this year who wrote an article together with this author for the first time
* **numNewArticleAuthors** : number of articles for this author for this year in which there are new writers

----------------------------
### Division into populations:
* Above 1 : 1 to 1000 (included)
* Above 13 : 13 and up
* Alph : 1 to 3 (included)
* Beta : 4 to 6 (included)
* Gama : 7 to 9 (included)
* Delta : 10 to 12 (included)

### Data based on population:
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


## DBLP:


