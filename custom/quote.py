#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import urllib2

progname = 'quote'
version = 'v0.0.1'


def get_quote():
    response = urllib2.urlopen('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
    response_text = response.read().decode('utf-8').replace("\\'", "'")
    quote = json.loads(response_text)
    print u'{0}\n- {1}'.format(quote['quoteText'], quote['quoteAuthor'])


def main():
    """The Entry Point."""
    for i in range(5):
        try:
            get_quote()
            return
        except:
            pass
    print u'Talk doesn\'t cook rice.\n- Chinese Proverb'
    return


if __name__ == '__main__':
    main()

