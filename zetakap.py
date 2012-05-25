#!/usr/bin/env python

from screens import make_screen
from article import Article
import glob

num_articles = len(glob.glob("Articles/Article_*.txt"))
articles = []

while len( articles ) < 10:
    
    article = Article( make_screen() )
    article.make_article()
    
    # check if there's enough stock tickers
    if int( article.title.split()[0] ) < 3:
        continue
    
    articles.append( article )
    num_articles = num_articles + 1
    article_file = open('Articles/Article_' + str(num_articles) + '.txt','w')
    article_file.write( str( article.print_article() ) )
    article_file.close()
    
