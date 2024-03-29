#!/usr/bin/env python

from screens import make_screen
from article import Article
import glob,os

pwd = os.path.dirname(__file__)
article_path = pwd + "/Articles"
article_prefix = "a"
num_articles = len(glob.glob( article_path + "/" + article_prefix + "*.txt"))
articles = []

while len( articles ) < 10:
    
    article = Article( make_screen() )
    
    # check if there's enough stock tickers
    if int( article.num_companies ) < 3:
        continue

    if article.make_article() != False:
        articles.append( article )
        article.tickerlist.update_pending_tickers()
        num_articles = num_articles + 1
        article_file = open( article_path + '/' + article_prefix + str(num_articles) + "___" + article.title.replace(' ','_') + '.txt', 'w' )        
        article_file.write( str( article.print_article() ) )
        article_file.close()
    
