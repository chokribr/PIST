# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011 CERN.
## CNUDST Team: Chokri (C) Juin 2021
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element - Prints Multi language Abstract .
"""

__revision__ = "$Id$"

#import cgi
from invenio import bibformat_utils

def format_element(bfo, print_lang='en,fr',prefix_abstract="", escape="3",):
    """ A specific CNUDST Dev : Prints the abstract in Multi langauge of a record in HTML.

    Printed languages can be chosen with the 'print_lang' parameter.

    @param prefix_abstract: a prefix for  abstract 
       """
   

    if print_lang == 'auto':
        print_lang = bfo.lang
    languages = print_lang.split(',')

    try:
        escape_mode_int = int(escape)
    except ValueError, e:
        escape_mode_int = 0

    
    abstracts =  bfo.fields('520%%', repeatable_subfields_p=True)
    out = ''
    if len(abstracts) >0 :
        out += '<div class="row"> <div class="abstract">'
        out += '<table>'	
        out += '<tbody><tr><td valign="top">'

	
        out += '<div class="col-lang"><div class="btn-group-vertical btn-lang opacity">'
    
        first = False 
        for abstract in abstracts:
           if len(abstracts) == 1:
             out += '<div ><p style="   color: #fff; center;  padding:2px; background-color:#356635;       border-width:2px;  border-style:solid; border-radius: 4px; border: 1px solid transparent;">' + abstract['9'][0]  +' </p></div>' 
           else :
         
             out += '<button type="button"'
             if not first :
                out += 'class="btn-default active"'
             else :
                 out += 'class="btn-default "'
             out += 'attr-lang="' + abstract['9'][0] + '">' + abstract['9'][0] + '</button>'
             first = True

        out +='</div> </div> </td><td ><table><tr align="center">  <div class="col-md-11 col-content"  >'

        first = False 

        for abstract in abstracts:
       
            out += '<div class=content-' + abstract['9'][0] 
            if not first :
               out += '>'
            else :
               out += ' style=display:none;  >'  
        
            out += ' <div class=abstract-content><strong>' + prefix_abstract + '</strong> <small>' +  abstract['a'][0] + '</small></br></div></div>'
            first = True
        
        out +='</tr></table></td></div></tr></tbody></table></div></div>' 
       
    return out
            
        


    

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
