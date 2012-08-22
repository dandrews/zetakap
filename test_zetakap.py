#!/usr/bin/env python

from screens import make_screen
from article import Article
import glob,os

pwd = os.path.dirname(__file__)
article_path = pwd + "/Articles"

article_prefix = "test_ignore_Article_"

num_articles = len(glob.glob( article_path + "/" + article_prefix + "*.txt"))
articles = []

# create a custom screen here
screen = ['','','','','','','']

while len( articles ) < 1:
    
    article = Article( screen )
    
    if int( article.num_companies ) < 3:
        continue

    if article.make_article() != False:
        articles.append( article )
        num_articles = num_articles + 1
        article_file = open( article_path + '/' + article_prefix + str(num_articles) + '.txt', 'w' )
        article_file.write( str( article.print_article() ) )
        article_file.close()
    
