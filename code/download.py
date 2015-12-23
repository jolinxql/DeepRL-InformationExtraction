''' download all relevant articles similar to original articles'''

#trainFile = '../data/tagged_data/whole_text_full_city/train.tag'

import sys, pickle, pdb
import query2 as query
from train import load_data

NUM_ENTITIES = 4

if __name__ == '__main__':


    trainFile = sys.argv[1]
    saveFile = sys.argv[2]
    
    #load data and process identifiers
    articles, identifiers = load_data(trainFile)
    identifiers_tmp = []  
    titles = []
    for e in identifiers:
        e = e.split(',')
        for i in range(NUM_ENTITIES):
            try:
                e[i] = int(e[i])
                e[i] = inflect_engine.number_to_words(e[i])
            except:
                pass
        identifiers_tmp.append(e[:NUM_ENTITIES])
        titles.append(','.join(e[NUM_ENTITIES:]))
    identifiers = identifiers_tmp

    #download related files
    downloaded_articles = []

    with open(saveFile, "wb" ) as f:
        for i in range(len(titles)):        
            tmp = query.download_articles_from_query(titles[i],' '.join(articles[i][0]),'bing')
            downloaded_articles.append(tmp)            
            pickle.dump([articles[i], titles[i], identifiers[i], downloaded_articles[i]], f)        
            print '\r',i,'/',len(titles)
        print
    #save to file
    
    print "Saved to file", saveFile