#!/usr/bin/env python

from gdata import service
import gdata
import atom

def CreatePublicPost(title, content, link):
  BLOGSPOT_USER = 'zetakap.media@gmail.com'
  BLOGSPOT_PASS = 'skippable'
  BLOG_ID ='8539885967588588944'
  
  blogger_service = service.GDataService( BLOGSPOT_USER, BLOGSPOT_PASS)
  blogger_service.source = 'exampleCo-exampleApp-1.0'
  blogger_service.service = 'blogger'
  blogger_service.account_type = 'GOOGLE'
  blogger_service.server = 'www.blogger.com'
  blogger_service.ProgrammaticLogin()

  content = content + "... <a href='%s'>Read the rest at SeekingAlpha.com</a>" % link
  
  entry = gdata.GDataEntry()
  entry.title = atom.Title('xhtml', title)
  entry.content = atom.Content(content_type='html', text=content) 
  return blogger_service.Post(entry, '/feeds/%s/posts/default' % BLOG_ID)

