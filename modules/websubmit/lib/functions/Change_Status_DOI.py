# This file is part of Invenio.
# Copyright (C) 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011 CERN.
# Copyright (C) 2024 CNUDST
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

__revision__ = "$Id$"

   ## Description:   Change  DOI Stae from Draft to Findable 
   ##                This function creates DOI using Datacite API 
   ##             by  bibConverting  and the configuration files passed as
   ##             parameters
   ##
   ## Author: Chokri Ben Romdhane
   ##

import os

from invenio.textutils import wash_for_xml
from invenio.config import \
     CFG_BINDIR, \
     CFG_WEBSUBMIT_BIBCONVERTCONFIGDIR,\
     CFG_DATACITE_USERNAME,\
     CFG_DATACITE_PASSWORD,\
     CFG_DATACITE_PREFIX 
from invenio.websubmit_config import InvenioWebSubmitFunctionError
import requests
import json
from os import access, rename, F_OK, R_OK


def Change_Status_DOI( parameters, curdir, form, user_info=None):


    """
    This function creates the record file formatted for a direct
    insertion in the documents database. It uses the BibConvert tool.  The
    main difference between all the Make_..._Record functions are the
    parameters.

    As its name does not say :), this particular function should be
    used for the submission of a document.

    """
    sysno = ""
    if access("%s/SN" % curdir, F_OK|R_OK):
        ## SN exists and should contain the recid; get it from there.
        try:
            fptr = open("%s/SN" % curdir, "r")
        except IOError:
            ## Unable to read the SN file's contents
            msg = """Unable to correctly read the current submission's recid"""
            raise InvenioWebSubmitFunctionError(msg)
        else:
            ## read in the submission details:
            sysno = fptr.read().strip()
            fptr.close()

    DOI = CFG_DATACITE_PREFIX  + "/pist-" + sysno 
    #URL_Record = "http://monastir.pist.tn/record/" + sysno
    Data = {
    "data": {
        "type": "dois",
        "attributes": {
            "event": "publish",

        }
    }
}
    
    url_api = "https://api.test.datacite.org/dois/"+ DOI
    headers = {'Content-Type': 'application/vnd.api+json'}
    
    try:
       response = requests.request("GET", url_api, auth=(CFG_DATACITE_USERNAME, CFG_DATACITE_PASSWORD),headers=headers)
       code_response = str(response.headers['Status'])

       if (code_response [0:3] == '200') :
                 response_PUT = requests.request("PUT", url_api,  auth=(CFG_DATACITE_USERNAME, CFG_DATACITE_PASSWORD), json = Data, headers=headers )
                 code_response_PUT = str(response_PUT.headers['Status'])
                 
           
                 if (code_response_PUT[0:3] != '200'):
                     raise InvenioWebSubmitFunctionError(" DOI Not updated!" + code_response_PUT ) 
       
       else: 
                 raise InvenioWebSubmitFunctionError(" DOI Not FOUND !" )
       
     
    except:

      raise InvenioWebSubmitFunctionError(" DOI Problem !" )
    return ""


