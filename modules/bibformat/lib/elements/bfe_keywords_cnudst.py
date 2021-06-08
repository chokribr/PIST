# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011 CERN.
# CNUDST Team : Chokri Copyright (C) 2021
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element - Prints keywords
   with language : CNUDST Dev
"""
__revision__ = "$Id$"

import cgi
from urllib import quote
from invenio.config import CFG_BASE_URL


def format_element(bfo, keyword_prefix, keyword_suffix,  print_lang='en,fr', separator=' ; ', link='yes'):
    """
    Display keywords of the record.

    @param keyword_prefix_fr: a prefix fr before each keyword
    @param keyword_suffix_en: a suffix fr after each keyword
    @param keyword_prefix_en: a prefix en before each keyword
    @param keyword_suffix_fr: a suffix en after each keyword
    @param print_lang: the comma-separated list of languages to print. Now restricted to 'en' and 'fr'
    @param separator: a separator between keywords
    @param link: links the keywords if 'yes' (HTML links)
    """
    if print_lang == 'auto':
        print_lang = bfo.lang
    languages = print_lang.split(',')
    champs = bfo.fields('653%_', repeatable_subfields_p=True)

    keywords_lang_agr = []  
    test_lang =''  
    for champ   in champs: 
        try:
          if champ['9'][0] <> test_lang and (champ['9'][0] not in  keywords_lang_agr) :
               test_lang = champ['9'][0]
               keywords_lang_agr.append(champ['9'][0])
        except:
             if ('' not in  keywords_lang_agr):
                 keywords_lang_agr.append('')

    out =''
    

    for keyword_lang_agr in keywords_lang_agr: 
       if keyword_lang_agr <>  '':
          out += '<div ><p style=" margin-left: 15%; width: 3%; color: #fff; center;  padding:2px; background-color:#356635;       border-width:2px;  border-style:solid; border-radius: 4px; border: 1px solid transparent;">' + keyword_lang_agr  +' </p></div>'
       #out +='<button type="button"  active" attr-lang="'+keyword_lang_agr+'">'+ keyword_lang_agr + '</button>'  
       #out += '<br><button type="button"  attr-lang="'+keyword_lang_agr+'">'+ keyword_lang_agr + '</button><br>'  
         
 
       if len(champs) > 0  :
            
            out += '<div style="margin-left: 15%; width: 70%;">' 
            if link == 'yes': 
               keywords= []
               for  champ in champs:
                       try:
                          if champ['9'][0]== keyword_lang_agr:
                             keywords.append('<a  href="' + CFG_BASE_URL + '/search?f=keyword&amp;p='+ quote('"' + champ['a'][0] + '"') + '&amp;ln='+ bfo.lang+  '">' + cgi.escape(champ['a'][0]) + '</a>')

                          #  keywords = ['<a  href="' + CFG_BASE_URL + '/search?f=keyword&amp;p='+ quote('"' + champ['a'][0] + '"') + '&amp;ln='+ bfo.lang+  '">' + cgi.escape(champ['a'][0]) + '</a>'
                                        #for  champ in champs if (champ['9'][0]== keyword_lang_agr ) ] 
                       except:
                             if keyword_lang_agr =='':
                                keywords.append('<a  href="' + CFG_BASE_URL + '/search?f=keyword&amp;p='+ quote('"' + champ['a'][0] + '"') + '&amp;ln='+ bfo.lang+  '">' + cgi.escape(champ['a'][0]) + '</a>')
            else:
                keywords =[cgi.escape(keyword) for champ in champs   ]
            keywords = [keyword_prefix + keyword + keyword_suffix
                     for keyword  in keywords]
            out += separator.join(keywords)
            out += '</div>'
    return out

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
