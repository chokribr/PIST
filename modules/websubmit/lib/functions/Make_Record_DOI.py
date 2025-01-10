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

   ## Description:   test DOI Inseert function 
   ##                This function creates DOI using Datacite API 
   ##             by  bibConverting  and the configuration files passed as
   ##             parameters
   ##
   ## AUthor: Chokri Ben Romdhane
   ##
   ## PARAMETERS:    sourceSubmit: source description file
   ##                mysqlInsert: template description file

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
import base64
import json
from os import access, rename, F_OK, R_OK
#parameters, , form, user_info=None
def Make_Record_DOI( parameters, curdir , form, user_info=None):
    """
    This function creates the record file formatted for a direct
    insertion in the documents database. It uses the BibConvert tool.  The
    main difference between all the Make_..._Record functions are the
    parameters.

    As its name does not say :), this particular function should be
    used for the submission of a document.

       * createTemplate: Name of bibconvert's configuration file used
                         for creating the mysql record.

       * sourceTemplate: Name of bibconvert's source file.
    """
    sysno=""
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
    # Get rid of "invisible" white spaces
    #source = parameters['sourceTemplate'].replace(" ","")
    #create = parameters['createTemplate'].replace(" ","")
    # We use bibconvert to create the xml record
    call_uploader_txt = "%s/bibconvert -l1   -c'%s' <%s/recmysql  > %s/recmysql_DOI" % (CFG_BINDIR,'DataCite.xsl',curdir ,curdir)
#(CFG_BINDIR,curdir,CFG_WEBSUBMIT_BIBCONVERTCONFIGDIR,source,CFG_WEBSUBMIT_BIBCONVERTCONFIGDIR,create,curdir)
    os.system(call_uploader_txt)
    # Then we have to format this record (turn & into &amp; and < into &lt;
    # After all we know nothing about the text entered by the users at submission time
    if os.path.exists("%s/recmysql_DOI" % curdir):
        fp = open("%s/recmysql_DOI" % curdir,"r")
        rectext = fp.read()
        fp.close()
    else:
        raise InvenioWebSubmitFunctionError("Cannot create database record DOI")

    if not rectext:
        raise InvenioWebSubmitFunctionError("Empty record DOI!")


    XML_64 = base64.encodestring(rectext)
    #print XML_64
    
    DOI = CFG_DATACITE_PREFIX  +"/pist-"+ sysno
    #print DOI
    URL_Record = "http://monastir.pist.tn/record/" + sysno
    Data = {
    "data": {
        "type": "dois",
        "attributes": {
            "event": "",
            "prefix": "10.80147" ,
            "doi": DOI,            
            "xml": XML_64,
            "url": URL_Record

        }
    }
}

    url_api = "https://api.test.datacite.org/dois/"
    headers = {'Content-Type': 'application/vnd.api+json'}
    try:
       response = requests.request("POST", url_api,  auth=(CFG_DATACITE_USERNAME, CFG_DATACITE_PASSWORD), json = Data, headers=headers )
      
       code_response = str(response.headers['Status'])
       if  (code_response [0:3] != '201'):
             raise   InvenioWebSubmitFunctionError(code_response)

    except:
       raise InvenioWebSubmitFunctionError("Erreur API Datacite")

    return ""


