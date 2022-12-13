#!/usr/bin/env python3
#title	Sorting lists of proteins in different ways

#lst{ProteintripleslistsortbyLength}
protein_triples = [('Q65209','African swine fever virus',141),
                   ('Q00020','Broad bean mottle virus',1164),
                   ('P03588','Brome mosaic virus',961),
                   ('Q83264','Cucumber mosaic virus',993)]

for protein in sorted(protein_triples,key=lambda p: p[2]):
  print('{}\t{}'.format(protein[1],protein[2]))
#lstend#

#lst{ProteinlistsortbyLength}
class Protein:
  def __init__(self, accession, name, length):
    self.accession = accession
    self.name = name
    self.length = length
  def __str__(self):
    return '{}\t{}'.format(self.name,self.length)

protein_list = [Protein('Q65209','African swine fever virus',141),
                Protein('Q00020','Broad bean mottle virus',1164),
                Protein('P03588','Brome mosaic virus',961),
                Protein('Q83264','Cucumber mosaic virus',993)]
for protein in sorted(protein_list,key=lambda p: p.name):
  print(protein)
#lstend#

#lst{ProteinlistsortItemAttrGetter}
from operator import itemgetter, attrgetter

for protein in sorted(protein_triples,key=itemgetter(2)):
  print('{}\t{}'.format(protein[1],protein[2]))

for protein in sorted(protein_list,key=attrgetter('length')):
  print(protein)
#lstend#
