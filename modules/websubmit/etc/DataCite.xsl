<?xml version="1.0" encoding="UTF-8"?>
<!--
<name>DataCite</name>
<description>DataCite XML</description>
-->
<!--
This stylesheet transforms a MARCXML input into DataCite output.
-->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:marc="http://www.loc.gov/MARC21/slim" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dc="http://purl.org/dc/elements/1.1/" exclude-result-prefixes="marc dc ">
	<xsl:output method="xml" indent="yes" encoding="UTF-8" omit-xml-declaration="yes"/>
	<xsl:template match="/">
		
			<resource xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://datacite.org/schema/kernel-4" xsi:schemaLocation="http://datacite.org/schema/kernel-4 http://schema.datacite.org/meta/kernel-4/metadata.xsd">
				<xsl:apply-templates/>
			</resource>
	</xsl:template>



	<xsl:template match="record" xmlns="http://datacite.org/schema/kernel-4">
		<xsl:choose>
			<xsl:when test="datafield[@tag='024' and @identfierType='DOI']">
				<identifier identifierType="DOI"><xsl:value-of select="datafield[@tag='024']/subfield[@code='a']"/></identifier>
			</xsl:when>
			<xsl:otherwise>
				<identifier identifierType="DOI">10.80147/pist-<xsl:value-of select="controlfield[@tag=001]"/></identifier>
			</xsl:otherwise>
		</xsl:choose> 
		<!-- Auteurs-->
		<creators>
			<creator>
				<creatorName>
					<xsl:value-of select="datafield[@tag='100']/subfield[@code='a']"/>
				</creatorName>
				<xsl:if test="datafield[@tag='100']/subfield[@code='u']">
					<affiliation>
						<xsl:choose>
							<xsl:when test="datafield[@tag='024' and subfield[@code='2']='ROR']">
								<xsl:attribute name="affiliationIdentifier">
									<xsl:text>https://ror.org/</xsl:text>
									<xsl:value-of select="datafield[@tag='024']/subfield[@code='a']"/>
								</xsl:attribute>
								<xsl:attribute name="affiliationIdentifierScheme">ROR</xsl:attribute>
								<xsl:attribute name="schemeURI">https://ror.org</xsl:attribute>
							</xsl:when>
						</xsl:choose>
						<xsl:value-of select="datafield[@tag='100']/subfield[@code='u']"/>
					</affiliation>
				</xsl:if>
			</creator>
			<xsl:for-each select="datafield[@tag=700]">
				<creator>
					<creatorName>
						<xsl:value-of select="subfield[@code='a']"/>
					</creatorName>
					<xsl:if test="datafield[@tag='700']/subfield[@code='u']">
						<affiliation>
							<xsl:value-of select="datafield[@tag='700']/subfield[@code='u']"/>
						</affiliation>
					</xsl:if>
				</creator>
			</xsl:for-each>
		</creators>
		<!--Titre -->
		<titles>
			<title>
				<xsl:value-of select="datafield[@tag='245']/subfield[@code='a']"/>
				<xsl:if test="datafield[@tag='245']/subfield[@code='b']">
					<xsl:text>:</xsl:text>
					<xsl:value-of select="datafield[@tag='245']/subfield[@code='b']"/>
				</xsl:if>
			</title>
		</titles>
		<!--Langues-->
		<xsl:for-each select="datafield[@tag=041]">
			<language>
				<xsl:value-of select="subfield[@code='a']"/>
			</language>
		</xsl:for-each>
		<!-- Mots clés -->
		<subjects>
			<xsl:for-each select="datafield[@tag=653]">
				<subject>
					<xsl:value-of select="subfield[@code='a']"/>
				</subject>
			</xsl:for-each>
		</subjects>
		<!-- Editeur -->
		<xsl:choose>
			<xsl:when test="datafield[@tag=502]/subfield[@code='c']">
				<publisher>
					<xsl:choose>
						<xsl:when test="datafield[@tag='024' and subfield[@code='2']='ROR']">
							<xsl:attribute name="publisherIdentifier">
								<xsl:text>https://ror.org/</xsl:text>
								<xsl:value-of select="datafield[@tag='024']/subfield[@code='a']"/>
							</xsl:attribute>
							<xsl:attribute name="publisherIdentifierScheme">ROR</xsl:attribute>
							<xsl:attribute name="schemeURI">https://ror.org</xsl:attribute>
						</xsl:when>
					</xsl:choose>
					<xsl:value-of select="datafield[@tag=502]/subfield[@code='c']"/>
				</publisher>
				<xsl:if test="not(contains(datafield[@tag=502]/subfield[@code='d'], '[s.d.]'))">
					<publicationYear>
						<xsl:value-of select="datafield[@tag=502]/subfield[@code='d']"/>
					</publicationYear>
				</xsl:if>
			</xsl:when>
			<xsl:when test="datafield[@tag=773] and notdatafield[@tag=260]/subfield[@code='c']">
				<publisher>
					<xsl:choose>
						<!-- Si 773$d contient ': ' -->
						<xsl:when test="contains(datafield[@tag=773]/subfield[@code='d'], ': ')">
							<xsl:value-of select="substring-before(substring-after(datafield[@tag=773]/subfield[@code='d'], ': '), ',')"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:value-of select="../datafield[@tag=260]/subfield[@code='b']"/>
						</xsl:otherwise>
					</xsl:choose>
					<!-- Ajouter les attributs pour ROR si applicable -->
					<xsl:if test="datafield[@tag='024' and subfield[@code='2']='ROR']">
						<xsl:attribute name="publisherIdentifier">
							<xsl:text>https://ror.org/</xsl:text>
							<xsl:value-of select="datafield[@tag='024']/subfield[@code='a']"/>
						</xsl:attribute>
						<xsl:attribute name="publisherIdentifierScheme">ROR</xsl:attribute>
						<xsl:attribute name="schemeURI">https://ror.org</xsl:attribute>
					</xsl:if>
				</publisher>
				<publicationYear>
					<xsl:choose>
						<xsl:when test="not(contains(datafield[@tag=773]/subfield[@code='d'], '[s.d.]')) and contains(datafield[@tag=773]/subfield[@code='d'], ':')">
							<xsl:value-of select="substring-after(substring-after(datafield[@tag=773]/subfield[@code='d'], ':'), ', ')"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:value-of select="datafield[@tag=260]/subfield[@code='c']"/>
						</xsl:otherwise>
					</xsl:choose>
				</publicationYear>
			</xsl:when>
			<xsl:otherwise>
				<xsl:for-each select="datafield[@tag=260]">
					<publisher>
						<xsl:value-of select="subfield[@code='b']"/>
						<xsl:choose>
							<xsl:when test="datafield[@tag='024' and subfield[@code='2']='ROR']">
								<xsl:attribute name="publisherIdentifier">
									<xsl:text>https://ror.org/</xsl:text>
									<xsl:value-of select="datafield[@tag='024']/subfield[@code='a']"/>
								</xsl:attribute>
								<xsl:attribute name="publisherIdentifierScheme">ROR</xsl:attribute>
								<xsl:attribute name="schemeURI">https://ror.org</xsl:attribute>
							</xsl:when>
						</xsl:choose>
					</publisher>
					<publicationYear>
						<xsl:value-of select="subfield[@code='c']"/>
					</publicationYear>
				</xsl:for-each>	
			</xsl:otherwise>
		</xsl:choose>
		<xsl:if test="datafield[@tag='264'] and not(contains(datafield[@tag='264'][@ind2='1']/subfield[@code='c'], '[s.d.]'))">
			<publicationYear>
				<xsl:value-of select="datafield[@tag='264'][@ind2='1']/subfield[@code='c']"/>
			</publicationYear>
		</xsl:if>
		<!-- URL, ISBN , ISSN -->
		<alternateIdentifiers>
			<alternateIdentifier alternateIdentifierType="URL">http://monastir.pist.tn/record/<xsl:value-of select="controlfield[@tag=001]"/>
			</alternateIdentifier>
			<xsl:for-each select="datafield[@tag=020]">
				<alternateIdentifier alternateIdentifierType="ISBN">
					<xsl:value-of select="subfield[@code='a']"/>
				</alternateIdentifier>
			</xsl:for-each>
			<xsl:for-each select="datafield[@tag=022]">
				<alternateIdentifier alternateIdentifierType="ISSN">
					<xsl:value-of select="subfield[@code='a']"/>
				</alternateIdentifier>
			</xsl:for-each>
			<!-- xsl:for-each select="datafield[@tag=773]">
				<alternateIdentifier>
					<xsl:if test="datafield[@tag='245']/subfield[@code='k'] = '[Article de revue]'">
						<xsl:attribute name="alternateIdentifierType">ISSN</xsl:attribute>
					</xsl:if>
					<xsl:if test="datafield[@tag='245']/subfield[@code='k'] = '[Acte de colloque]'">
						<xsl:attribute name="alternateIdentifierType">ISBN</xsl:attribute>
					</xsl:if>
					<xsl:value-of select="subfield[@code='x']"/>
				</alternateIdentifier>
			</xsl:for-each -->
		</alternateIdentifiers>
		<!-- Abstract -->
		<descriptions>
			<xsl:for-each select="datafield[@tag=520]">
				<description descriptionType="Abstract">
					<xsl:attribute name="xml:lang">
						<xsl:value-of select="subfield[@code='9']"/>
					</xsl:attribute>
					<xsl:value-of select="subfield[@code='a']"/>
				</description>
			</xsl:for-each>
			<!-- voir autre note-->
			<xsl:for-each select="datafield[@tag=504]">
				<description descriptionType="Other">
					<xsl:value-of select="subfield[@code='a']"/>
				</description>
			</xsl:for-each>
		</descriptions>
		<!-- Collation -->
		<xsl:if test="datafield[@tag=300]">
			<sizes>
				<xsl:for-each select="datafield[@tag=300]">
					<size>
						<xsl:value-of select="subfield[@code='a']"/>
					</size>
				</xsl:for-each>
			</sizes>
		</xsl:if>
		<!-- Typologie -->
		<xsl:for-each select="datafield[@tag=980]">
			<xsl:choose>

				<xsl:when test="(contains(subfield[@code='a'], 'MASTERE'))">
					<resourceType>
						<xsl:attribute name="resourceTypeGeneral">Dissertation</xsl:attribute>
						MASTERE
					</resourceType>
				</xsl:when>
				<xsl:when test="(contains(subfield[@code='a'],'MEMOIRE'))">
					<resourceType>
						<xsl:attribute name="resourceTypeGeneral">Dissertation</xsl:attribute>
						MEMOIRE
					</resourceType>
				</xsl:when>
				<xsl:when test="(contains(subfield[@code='a'],'THESIS'))">
					<resourceType><xsl:attribute name="resourceTypeGeneral">Dissertation</xsl:attribute>THESIS</resourceType>
				</xsl:when>
				<xsl:when test="(contains(subfield[@code='a'],'RAPPORT'))">
					<resourceType>
						<xsl:attribute name="resourceTypeGeneral">Report</xsl:attribute>
						<!--<xsl:value-of select="substring-before(/datafield[@tag=502]/subfield[@code='a'], ' (')"/>-->
					</resourceType>
				</xsl:when>
				<xsl:when test="contains(subfield[@code='a'], 'ARTICLE')">
					<resourceType>
						<xsl:attribute name="resourceTypeGeneral">JournalArticle</xsl:attribute>
					</resourceType>
				</xsl:when>
				<xsl:when test="subfield[@code='a']='PRETIRAGE'">
					<resourceType>
						<xsl:attribute name="resourceTypeGeneral">Preprint</xsl:attribute>
						<xsl:value-of select="../datafield[@tag='245']/subfield[@code='k']"/>
					</resourceType>
				</xsl:when>
				<xsl:when test="subfield[@code='a']='LIVRE'">
					<resourceType>
						<xsl:attribute name="resourceTypeGeneral">Book</xsl:attribute>
						<xsl:value-of select="subfield[@code='a']"/>
					</resourceType>
				</xsl:when>
				<xsl:when test="subfield[@code='a']='Dataset'">
					<resourceType>
						<xsl:attribute name="resourceTypeGeneral">Dataset</xsl:attribute>
					</resourceType>
				</xsl:when>
			</xsl:choose>
		</xsl:for-each>
		<!-- Date DateType=Available, Accepted -->
		<dates>
			<xsl:choose>
				<xsl:when test="datafield[@tag=502]/subfield[@code='d']">
					<!-- date de soutenance pour les travaux universitaires -->
					<date dateType="Issued">
						<xsl:value-of select="datafield[@tag=502]/subfield[@code='d']"/>
					</date>
				</xsl:when>
				<xsl:otherwise>
					<!-- date de publicatoon pour le livre -->
					<xsl:for-each select="datafield[@tag=260]">
						<date dateType="Issued">
							<xsl:value-of select="subfield[@code='c']"/>
						</date>
					</xsl:for-each>
				</xsl:otherwise>
			</xsl:choose>
		</dates>
		<!-- copyright-->
		<xsl:for-each select="datafield[@tag=540]">
			<rightsList>
				<rights>
					<xsl:attribute name="rightsURI">
						<xsl:value-of select="subfield[@code='u']"/>
					</xsl:attribute>
					<xsl:value-of select="subfield[@code='a']"/>
				</rights>
			</rightsList>
		</xsl:for-each>
		<!-- relation -->
		<relatedItems>
			<xsl:if test="datafield[@tag=773]">
				<relatedItem relationType="IsPartOf">
					<xsl:if test="datafield[@tag='245']/subfield[@code='k'] = '[Article de revue]'">
						<xsl:attribute name="relatedItemType">Journal</xsl:attribute>
					</xsl:if>
					<xsl:if test="datafield[@tag='245']/subfield[@code='k'] = '[Acte de colloque]'">
						<xsl:attribute name="relatedItemType">ConferenceProceeding</xsl:attribute>
					</xsl:if>
					<xsl:if test="datafield[@tag=773]/subfield[@code='x']">
						<relatedItemIdentifier>
							<xsl:if test="datafield[@tag='245']/subfield[@code='k'] = '[Article de revue]'">
								<xsl:attribute name="relatedItemIdentifierType">ISSN</xsl:attribute>
							</xsl:if>
							<xsl:if test="datafield[@tag='245']/subfield[@code='k'] = '[Acte de colloque]'">
								<xsl:attribute name="relatedItemIdentifierType">ISBN</xsl:attribute>
							</xsl:if>
							<xsl:value-of select="datafield[@tag=773]/subfield[@code='x']"/>
						</relatedItemIdentifier>
					</xsl:if>
					<xsl:if test="datafield[@tag=773]/subfield[@code='t']">
						<titles>
							<title>
								<xsl:value-of select="datafield[@tag=773]/subfield[@code='t']"/>
							</title>
						</titles>
					</xsl:if>
					<xsl:if test="datafield[@tag=773]/subfield[@code='g']">
						<volume>
							<xsl:value-of select="substring-before(datafield[@tag=773]/subfield[@code='g'], ',')"/>
						</volume>
						<xsl:if test="substring-before(substring-after(datafield[@tag=773]/subfield[@code='g'], ','), ',')">
							<number>
								<xsl:value-of select="substring-before(substring-after(datafield[@tag=773]/subfield[@code='g'], ','), ',')"/>
							</number>
						</xsl:if>
						<!--issue>Iss 1</issue-->
					</xsl:if>
				</relatedItem>
			</xsl:if>
		</relatedItems>
	</xsl:template>
</xsl:stylesheet>
