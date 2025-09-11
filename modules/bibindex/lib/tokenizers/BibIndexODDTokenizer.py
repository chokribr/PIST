# -*- coding:utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2013 CERN.
# Copyright (C) 2025 CNUDST.
# Autor : Chokri Ben Romdhane
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
from invenio.bibindex_tokenizers.BibIndexFilteringTokenizerODD import BibIndexFilteringTokenizerODD


class BibIndexODDTokenizer(BibIndexFilteringTokenizerODD):
    """
        Filtering tokenizer which tokenizes ODD  based on tag (092_a) values
        
    """


    def __init__(self, stemming_language=None, remove_stopwords=False, remove_html_markup=False, remove_latex_markup=False):
        self.rules = (('092__a', 'a', '',''),)
 

    def get_tokenizing_function(self, wordtable_type):
        """Returns proper tokenizing function"""
        return self.tokenize

   

    def tokenize_via_recjson(self, recID):
        """
        Nonmarc version of tokenize function for DOI.
        Note: with nonmarc we don't need to filter anymore.
        We just need to take value from record because we
        use bibfield here.
        """
        rec = get_record(recID)
        values = rec.get('doi', [])
        return values
