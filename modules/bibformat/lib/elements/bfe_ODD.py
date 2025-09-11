# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011 CERN.
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
"""BibFormat element - ODD element
"""

__revision__ = "$Id$"

from invenio.bibformat_elements.bfe_report_numbers import \
     build_report_number_link

def format_element(bfo, limit, separator=" ", link='yes'):
    """
    Prints ODD image

    """
    ODDs = bfo.fields("092__a", repeatable_subfields_p=True)
    ODDB_img= ' '
    
    for ODD in ODDs:

       if ODD in ['D08.02', 'D04.02',  'D04.05']:
          ODDB_img = ODDB_img + ' <a href="/search?ln=fr&p=ODD01&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="No poverty"> <img  border="1" width="20" height="20" alt="No poverty" src="/img/SDG/web/E-WEB-Goal-01.png"></a>'
       if ODD in ['D04.05' ,'A05.06', 'A05.08' ]:  
          ODDB_img = ODDB_img + '  <a href="/search?ln=fr&p=ODD02&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Zero hunger" > <img  border="1" width="20" height="20" alt="Zero hunger" src="/img/SDG/web/E-WEB-Goal-02.png"></a>'

       if ODD in ODD in ['D04.05', 'A05.06', 'D08.05']: 
          ODDB_img = ODDB_img + '  <a href="/search?ln=fr&p=ODD03&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Good health and well-being"> <img  border="1" width="20" height="20"  alt="Good health and well-being" src="/img/SDG/web/E-WEB-Goal-03.png"></a>'


       if ODD in ['D06', 'D08.02']   or ODD[0:3] in ['D06', 'D08.02'] :  
          ODDB_img = ODDB_img + '  <a href="/search?ln=fr&p=ODD04&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Quality education"> <img  border="1" width="20" height="20" alt="Quality education" src="/img/SDG/web/E-WEB-Goal-04.png"></a>'

       if ODD in ['D08.01', 'D08.02', 'D02.01', 'D02.04' ] :  
          ODDB_img = ODDB_img + '  <a href="/search?ln=&p=ODD05&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb"title="Gender equality"> <img  border="1" width="20" height="20" alt="Gender equality" src="/img/SDG/web/E-WEB-Goal-05.png"></a>'
      

       if ODD in ['A04.07', 'D02.04' ,'B10'] or ODD[0:3] in ['A04.07', 'D02.04' ,'B10'] :  
          ODDB_img = ODDB_img + '  <a href="/search?ln=&p=ODD06&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Clean water and sanitation"> <img  border="1" width="20" height="20" alt="Clean water and sanitation" src="/img/SDG/web/E-WEB-Goal-06.png"></a>'

       if ODD in ['B05', 'D04.05', 'D02.04' ,'B10'] or ODD[0:3] in ['B05' ,'B10']:
          ODDB_img = ODDB_img + ' <a href="/search?ln=&p=ODD07&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb"title="Affordable and clean energy"> <img  border="1" width="20" height="20" alt="Affordable and clean energy" src="/img/SDG/web/E-WEB-Goal-07.png"></a> '

       if ODD  in ['D04.05', 'D04.02',  'D02.04',  'D02.02' ]:
          ODDB_img = ODDB_img + ' <a href="/search?ln=&p=ODD08&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Decent work and economic growth"> <img  border="1" width="20" height="20" alt="Decent work and economic growth" src="/img/SDG/web/E-WEB-Goal-08.png"></a>'


       if ODD  in  ['B04', 'B07', 'D04.05',  'B10' ] or ODD[0:3] in ['B04', 'B07', 'D04.05',  'B10' ]:
          ODDB_img = ODDB_img + '  <a href="/search?ln=&p=ODD09&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Industry, Innovation, Technology and Infrastructure"> <img  border="1" width="20" height="20" alt="Industry, Innovation, Technology and Infrastructure" src="/img/SDG/web/E-WEB-Goal-09.png"></a>'

       if ODD  in  [ 'D02.01',  'D02.04',  'D08.02', 'D04.05']:
          ODDB_img = ODDB_img + '  <a href="/search?ln=&p=ODD10&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Reduced inequality"> <img  border="1" width="20" height="20" alt="Reduced inequality" src="/img/SDG/web/E-WEB-Goal-10.png"></a>'


       if ODD  in ['B10' , 'B08' , 'CO2.03' ,'D04.05', 'B09'] or ODD[0:3] in ['B10' , 'B08' , 'CO2.03' ,'D04.05', 'B09']:
          ODDB_img = ODDB_img + '  <a href="/search?ln=&p=ODD11&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Industry, Innovation, Technology and Infrastructure"> <img  border="1" width="20" height="20" alt="Industry, Innovation, Technology and Infrastructure" src="/img/SDG/web/E-WEB-Goal-11.png"></a>'


       if ODD  in ['B05' ,'A05.04' ,'B10']  or ODD[0:3] in ['B05' ,'A05.04' ,'B10']:
          ODDB_img = ODDB_img + '  <a href="/search?ln=&p=ODD12&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Climate action"> <img  border="1" width="20" height="20" alt="Climate action" src="/img/SDG/web/E-WEB-Goal-12.png"></a>'

       if ODD  in ['B10', 'A05.04', 'C05.02'] or ODD[0:3] in ['B10', 'A05.04', 'C05.02']:
          ODDB_img = ODDB_img + '  <a href="/search?ln=&p=ODD13&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Responsible consumption and production"> <img  border="1" width="20" height="20" alt="Responsible consumption and production" src="/img/SDG/web/E-WEB-Goal-13.png"></a>'


       if ODD  in ['A04.08' ,'B10' ,'A05.04'] or ODD[0:3] in ['B10']:
          ODDB_img = ODDB_img + '  <a href="/search?ln=&p=ODD14&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Life below water""> <img  border="1" width="20" height="20" alt="Life below water" src="/img/SDG/web/E-WEB-Goal-14.png"></a>'

       if ODD  in ['B10', 'C05.02', 'A04.06', 'A05.04'] or ODD[0:3] in ['B10', 'C05.02', 'A04.06', 'A05.04']:
          ODDB_img = ODDB_img + '  <a href="/search?ln=&p=ODD15&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Zero hunger"> <img  border="1" width="20" height="20" alt="Life on land" src="/img/SDG/web/E-WEB-Goal-15.png"></a>'

       if ODD  in ['D04.05' ,'D08.02' ,'D02.04' ,'D03.01']:
          ODDB_img = ODDB_img + '  <a href="/search?ln=&p=ODD16&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Peace, justice and strong institutions"> <img  border="1" width="20" height="20" alt="Peace, justice and strong institutions" src="/img/SDG/web/E-WEB-Goal-16.png"></a>'

       if ODD  in ['D04.02' ,'D02.04' ,'D03.01' ,'D03.02']:
          ODDB_img = ODDB_img + '  <a href="/search?ln=&p=ODD17&f=ODD&action_search=Recherche&c=&c=&sf=&so=d&rm=&rg=10&sc=1&of=hb" title="Partnerships for the goals"> <img  border="1" width="20" height="20" alt="Partnerships for the goals" src="/img/SDG/web/E-WEB-Goal-17.png"></a>'

    '''
                escape(target, True),
                escape(_("This article on arXiv.org"), True),
                escape(arxiv_id))
if field['a'] in ['D08.02', 'D04.02',  'D04.05']:
                       phrases.append('ODD01')


                    elif field['a'] in ['D04.05' ,'A05.06', 'A05.08' ]:
                        phrases.append('ODD02')
                         
                    elif field['a'] in ['D04.05', 'A05.06', 'D08.05']:
                        phrases.append('ODD03')
                        phrases.append('ODD03')
                    elif field['a'] in ['D06', 'D08.02'] or field['a'][0:3] in ['D06', 'D08.02']:
                        phrases.append('ODD04')
                    elif field['a'] in ['D08.01', 'D08.02', 'D02.01', 'D02.04' ]:
                        phrases.append('ODD05')
                    elif field['a'] in ['A04.07', 'D02.04' ,'B10'] or field['a'][0:3] in ['A04.07', 'D02.04' ,'B10']:
                        phrases.append('ODD06')
                    elif field['a'] in [ 'B05', 'D04.05', 'D02.04', 'B10' ] or field['a'][0:3] in [ 'B05', 'D04.05', 'D02.04', 'B10' ]:
                        phrases.append('ODD07')
                    elif field['a'] in ['D04.05', 'D04.02',  'D02.04',  'D02.02' ]:
                        phrases.append('ODD08')
                    elif field['a'] in ['B04', 'B07', 'D04.05',  'B10' ] or field['a'][0:3] in ['B04', 'B07', 'D04.05',  'B10' ]:
                        phrases.append('ODD09')
                    elif field['a'] in [ 'D02.01',  'D02.04',  'D08.02', 'D04.05']:
                        phrases.append('ODD10')
                    elif field['a'] in ['B10' , 'B08' , 'CO2.03' ,'D04.05', 'B09'] or field['a'][0:3] in ['B10' , 'B08' , 'CO2.03' ,'D04.05', 'B09'] :
                        phrases.append('ODD11')
                    elif field['a'] in ['B05' ,'A05.04' ,'B10']  or field['a'][0:3] in ['B05' ,'A05.04' ,'B10']:
                        phrases.append('ODD12')                    
                    elif field['a'] in ['B10', 'A05.04', 'C05.02'] or field['a'][0:3] in ['B10', 'A05.04', 'C05.02']:
                        phrases.append('ODD13')
                    elif field['a'] in ['A04.08' ,'B10' ,'A05.04']:
                        phrases.append('ODD14')
                    elif field['a'] in ['B10', 'C05.02', 'A04.06', 'A05.04'] or field['a'][0:3] in ['B10', 'C05.02', 'A04.06', 'A05.04'] :
                    elif field['a'] in ['D04.05' ,'D08.02' ,'D02.04' ,'D03.01']:
                        phrases.append('ODD16')
                    elif field['a'] in ['D04.02' ,'D02.04' ,'D03.01' ,'D03.02']:
                        phrases.append('ODD17')                 '''
    


    return ODDB_img 

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
