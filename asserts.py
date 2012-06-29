#!/usr/bin/env python

import check_ticker_age

# successful returns
# expect False
age = check_ticker_age.get_ticker_article_age( 'BIP' )
assert( False == check_ticker_age.is_old_enough( age ) )
# expect True
age = check_ticker_age.get_ticker_article_age( 'AIZ' )
assert( check_ticker_age.is_old_enough( age ) )

# no articles # expect True
age = check_ticker_age.get_ticker_article_age( 'BTI' )
assert( check_ticker_age.is_old_enough( age ) )

# bad ticker
try:
    age = check_ticker_age.get_ticker_article_age( 'TURDS' )
except Exception as error:
    print "TICKER NOT FOUND!"
    assert( error.args[0] == "TICKER NOT FOUND!" )


