# Research_Publishing_Articles

**ArXiv**:

Skip articles written by more than 10 authors
sort the data by the 'versions' 'version' :'v1' 'created' field

articles written by more than 10 authors:65344

articles written by less of equal to 10 authors:1860365

----------------------------
the short dictionary format:
{
    `<author name>` :
    { `<year>` :
        {
            `<numArticle>`: int,
            `<numUniqueAuthors>`: int,
            `<newAuthors>`: int,
            `<numNewArticleAuthors>`: int
        }
    }
}
'''