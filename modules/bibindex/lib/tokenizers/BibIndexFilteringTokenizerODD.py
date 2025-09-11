# -*- coding:utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2013, 2014 CERN.
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


from invenio.search_engine import get_record
from invenio.bibrecord import record_get_field_instances
from invenio.bibindex_tokenizers.BibIndexMultiFieldTokenizer import BibIndexMultiFieldTokenizer

class BibIndexFilteringTokenizerODD(BibIndexMultiFieldTokenizer):
    """
         Filtering tokenizer which tokenizes ODD  based on tag (092_a) values
    """

    def __init__(self, stemming_language=None, remove_stopwords=False, remove_html_markup=False, remove_latex_markup=False):
        self.rules = ()


    def tokenize(self, recID):
        phrases = []


        try:
            rec = get_record(recID)

            for rule in self.rules:
                tag_to_index, necessary_tag, necessary_value, in_substring = rule
                core_tag = tag_to_index[0:3]
                ind = tag_to_index[3:5]
                sub_tag = tag_to_index[5]

                fields = [dict(instance[0]) for instance in record_get_field_instances(rec, core_tag, ind[0], ind[1])]
                for field in fields:
                    tag_condition = necessary_tag and field.has_key(necessary_tag) or necessary_tag == ''
                    value_condition = necessary_value and field.get(necessary_tag, '') == necessary_value or \
                                      necessary_value == ''
#                    if tag_condition and field.has_key(sub_tag) and value_condition:

                    if field['a'] in ['D08.02', 'D04.02',  'D04.05']:
                       phrases.append('ODD01') 
                       phrases.append('SDG01') 
                       phrases.append('No poverty')
                       phrases.append('poverty')
                       phrases.append('Pas de pauvreté')
                       phrases.append('pauvreté')
                       phrases.append('القضاء على الفقر')
                       phrases.append('الفقر')
                       phrases.append('القضاء')
                       phrases.append('على')
                    if field['a'] in ['D04.05' ,'A05.06', 'A05.08' ]:
                        phrases.append('ODD02')
                        phrases.append('SDG02')
                        phrases.append('Zero hunger')
                        phrases.append('hunger')
                        phrases.append('Zero')
                        phrases.append('Lutte contre la faim')
                        phrases.append('faim')
                        phrases.append('Lutte')
                        phrases.append('القضاء التام على الجوع')
                        phrases.append('الجوع')
                        phrases.append('القضاء')
                        phrases.append('التام')

                         
                    if field['a'] in ['D04.05', 'A05.06', 'D08.05']:
                        phrases.append('ODD03')
                        phrases.append('SDG03')

                        phrases.append('Good health and well-being')
                        phrases.append('Good')
                        phrases.append('health')
                        phrases.append('well-being')


                        phrases.append('Bonne santé et bien-être')
                        phrases.append('Bonne')

                        phrases.append('bien-être')
                        phrases.append('santé')
                        phrases.append('الصحة الجيدة والرفاه')
                        phrases.append('الصحه')
                        phrases.append('الجيدة')
                        phrases.append('الرفاه')

                    if field['a'] in ['D06', 'D08.02'] or field['a'][0:3] in ['D06', 'D08.02']:

                        phrases.append('ODD04')
                        phrases.append('SDG04')
                        phrases.append('Quality education')
                        phrases.append('Quality')
                        phrases.append('education')
                        phrases.append('Accès à une éducation de qualité')
                        phrases.append('Accès')
                        phrases.append('éducation')
                        phrases.append('qualité')
                        phrases.append('التعليم الجيد')
                        phrases.append('الجيد')
                        phrases.append('التعليم')


                    if field['a'] in ['D08.01', 'D08.02', 'D02.01', 'D02.04' ]:

                        phrases.append('ODD05')
                        phrases.append('SDG05')
                        phrases.append('Gender equality')
                        phrases.append('Gender')
                        phrases.append('equality')
                        phrases.append('Égalité entre les sexes')
                        phrases.append('Égalité ')
                        phrases.append('sexes')
                        phrases.append('المساواة بين الجنسين')
                        phrases.append('الجنسين')
                        phrases.append('المساواة')

                    if field['a'] in ['A04.07', 'D02.04' ,'B10'] or field['a'][0:3] in ['A04.07', 'D02.04' ,'B10']:
                        phrases.append('ODD06')
                        phrases.append('SDG06')
                        phrases.append('Clean water and sanitation')
                        phrases.append('Clean')
                        phrases.append('water')
                        phrases.append('sanitation')
                        phrases.append('Accès à l''eau salubre et à l''assainissement')
                        phrases.append('Accès')
                        phrases.append('eau')
                        phrases.append('salubre')
                        phrases.append('assainissement')
                        phrases.append('المياه النظيفة والنظافة الصحية')
                        phrases.append('المياه')
                        phrases.append('النظيفة')
                        phrases.append('النظافة')
                        phrases.append('الصحية')

                    if field['a'] in [ 'B05', 'D04.05', 'D02.04', 'B10' ] or field['a'][0:3] in [ 'B05', 'D04.05', 'D02.04', 'B10' ]:
                        phrases.append('ODD07')
                        phrases.append('SDG07')
                        phrases.append('Affordable and clean energy')
                        phrases.append('Affordable')
                        phrases.append('clean')
                        phrases.append('energy')


                        phrases.append('Énergie propre et d''un coût abordable')
                        phrases.append('Énergie')
                        phrases.append('propre')
                        phrases.append('coût')
                        phrases.append('abordable')
                        phrases.append('طاقة نظيفة وبأسعار معقولة')
                        phrases.append('طاقة')
                        phrases.append('نظيفة')
                        phrases.append('أسعار')
                        phrases.append('معقولة')


                    if field['a'] in ['D04.05', 'D04.02',  'D02.04',  'D02.02' ]:
                        phrases.append('ODD08')
                        phrases.append('SDG08')
                        phrases.append('Decent work and economic growth')
                        phrases.append('Decent')
                        phrases.append('work')
                        phrases.append('economic')
                        phrases.append('growth')

                        phrases.append('Accès à des emplois décents')
                        phrases.append('Accès')
                        phrases.append('emplois')
                        phrases.append('décents')

                        phrases.append('العمل اللائق ونمو الاقتصاد')
                        phrases.append('العمل')
                        phrases.append('اللائق')
                        phrases.append('نمو')
                        phrases.append('الاقتصاد')

                    if field['a'] in ['B04', 'B07', 'D04.05',  'B10' ] or field['a'][0:3] in ['B04', 'B07', 'D04.05',  'B10' ]:
                        phrases.append('ODD09')
                        phrases.append('SDG09')
                        phrases.append('Industry, Innovation, Technology and Infrastructure')
                        phrases.append('Industry')
                        phrases.append('Innovation')
                        phrases.append('Technology')
                        phrases.append('Infrastructure')

                        phrases.append('Industrie, innovation et infrastructure')
                        phrases.append('Industrie')
                        phrases.append('innovation')
                        phrases.append('infrastructure')

                        phrases.append('الصناعة والابتكار والبنية التحتية')
                        phrases.append('الصناعة')
                        phrases.append('الابتكار')
                        phrases.append('البنية')
                        phrases.append('التحتية')

                    if field['a'] in [ 'D02.01',  'D02.04',  'D08.02', 'D04.05']:
                        phrases.append('ODD10')
                        phrases.append('SDG10')
                        phrases.append('Reduced inequality')
                        phrases.append('Reduced')
                        phrases.append('inequality')

                        phrases.append('Réduction des inégalités')
                        phrases.append('inégalités')
                        phrases.append('Réduction')

                        phrases.append('الحد من أوجه عدم المساواة')
                        phrases.append('الحد')
                        phrases.append('أوجه')
                        phrases.append('عدم')
                        phrases.append('المساواة')

                    if field['a'] in ['B10' , 'B08' , 'CO2.03' ,'D04.05', 'B09'] or field['a'][0:3] in ['B10' , 'B08' , 'CO2.03' ,'D04.05', 'B09'] :
                        phrases.append('ODD11')
                        phrases.append('SDG11')

                        phrases.append('Sustainable cities and communities')
                        phrases.append('Sustainable')
                        phrases.append('cities')
                        phrases.append('communities')

                        phrases.append('Villes et communautés durables')
                        phrases.append('Villes')
                        phrases.append('communautés')
                        phrases.append('durables')

                        phrases.append('مدن ومجتمعات محلية مستدامة')
                        phrases.append('مدن')
                        phrases.append('مجتمعات')
                        phrases.append('محلية')
                        phrases.append('مستدامة')


                    if field['a'] in ['B05' ,'A05.04' ,'B10']  or field['a'][0:3] in ['B05' ,'A05.04' ,'B10']:
                        phrases.append('ODD12') 
                        phrases.append('SDG12') 
                        phrases.append('Responsible consumption and production')
                        phrases.append('Responsible')
                        phrases.append('consumption')
                        phrases.append('production')
                        phrases.append('Consommation et production responsables')
                        phrases.append('Consommation')
                        phrases.append('production')
                        phrases.append('responsables')

                        phrases.append('الاستهلاك والإنتاج المسؤولان')
                        phrases.append('الاستهلاك')
                        phrases.append('الإنتاج')
                        phrases.append('المسؤولان')
                  
                    if field['a'] in ['B10', 'A05.04', 'C05.02'] or field['a'][0:3] in ['B10', 'A05.04', 'C05.02']:
                        phrases.append('ODD13')
                        phrases.append('SDG13')
                        phrases.append('Climate action')
                        phrases.append('Climate')
                        phrases.append('action')
                        phrases.append('Lutte contre les changements climatiques')
                        phrases.append('Lutte')
                        phrases.append('contre')
                        phrases.append('changements')
                        phrases.append('climatiques')
                        phrases.append('العمل المناخي')
                        phrases.append('المناخي')
                        phrases.append('العمل')

                    if field['a'] in ['A04.08' ,'B10' ,'A05.04']:
                        phrases.append('ODD14')
                        phrases.append('SDG14')
                        phrases.append('Life below water')
                        phrases.append('Life')
                        phrases.append('below')
                        phrases.append('water')

                        phrases.append('Vie aquatique')
                        phrases.append('Vie')
                        phrases.append('aquatique')
                        phrases.append('الحياة تحت الماء')
                        phrases.append('الحياة')
                        phrases.append('تحت')

                    if field['a'] in ['B10', 'C05.02', 'A04.06', 'A05.04'] or field['a'][0:3] in ['B10', 'C05.02', 'A04.06', 'A05.04'] :
                        phrases.append('ODD15')
                        phrases.append('SDG15')
                        phrases.append('Life on land')
                        phrases.append('Life')
                        phrases.append('land')
                        phrases.append('Vie terrestre')
                        phrases.append('Vie')
                        phrases.append('terrestre')
                        phrases.append('الحياة في البرّ')
                        phrases.append('البرّ')
                        phrases.append('الحياة')

                    if field['a'] in ['D04.05' ,'D08.02' ,'D02.04' ,'D03.01']:
                        phrases.append('ODD16')
                        phrases.append('SDG16')

                        phrases.append('Peace, justice and strong institutions')
                        phrases.append('Peace')
                        phrases.append('justice')
                        phrases.append('strong')
                        phrases.append('institutions')

                        phrases.append('Paix, justice et institutions efficaces')
                        phrases.append('Paix')
                        phrases.append('justice')
                        phrases.append('institutions')
                        phrases.append('efficaces')
                        phrases.append('السلام والعدالة والمؤسسات القوية')
                        phrases.append('السلام')
                        phrases.append('العدالة')
                        phrases.append('المؤسسات')
                        phrases.append('القوية')


                    if field['a'] in ['D04.02' ,'D02.04' ,'D03.01' ,'D03.02']:
                        phrases.append('ODD17')
                        phrases.append('SDG17')

                        phrases.append('Partnerships for the goals')
                        phrases.append('Partnerships')
                        phrases.append('goals')
                        phrases.append('Partenariats pour la réalisation des objectifs')
                        phrases.append('Partenariats')
                        phrases.append('réalisation')
                        phrases.append('objectifs')
                        phrases.append('عقد الشراكة لتحقيق الأهداف')
                        phrases.append('عقد')
                        phrases.append('الشراكة')
                        phrases.append('لتحقيق')
                        phrases.append('الأهداف')

            return phrases
        except KeyError:
            return []
        return phrases

    def tokenize_via_recjson(self, recID):
        """
        TODO: implementation needs to be introduced
        in order to work with non-marc standards.
        """
        return []
