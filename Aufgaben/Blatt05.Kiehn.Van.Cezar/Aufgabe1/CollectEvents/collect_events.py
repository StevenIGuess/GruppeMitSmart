#!/usr/bin/env python3

import sys, re

if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} <inputfile>\n'
                    .format(sys.argv[0]))
  exit(1)

month_list = ['Januar',
              'Februar',
              'März',
              'April',
              'Mai',
              'Juni',
              'Juli',
              'August',
              'September',
              'Oktober',
              'November',
              'Dezember']

'''FRAGE 1 (0.5 Punkte): Warum ist es sinnvoll, den folgenden String zu
definieren und wozu dient dabei das Zeichen |? Hinweis: verwenden Sie diesen
String in zwei der vier regul"aren Ausdr"ucke.
ANTWORT:
'''

re_month = '|'.join(month_list)

'''Definiere die Elemente einer Liste res_for_date
(Abk"urzung f"ur regular expressions for date).
Diese Liste muss vier regul"are Ausdr"ucke enthalten, die auf die
verschiedenen Formate der Datumsangaben in der Datei events.txt
passen. Jeder der Ausdr"ucke wird als String-Literal, also begrenzt
mit einfachen Anf"uhrungszeichen notiert. Die Datumsangaben, die durch
die regularen Ausdr"ucke erfasst werden, m"ussen immer eine Jahreszahl
enthalten. Die meisten enthalten auch eine Monatsangabe und die
Angabe des Tags. In wenigen F"allen fehlen eine oder beide Angaben.
Es ist wichtig, die regul"aren Ausdr"ucke zu verankern.
Entwickeln Sie nacheinander die einzelnen regul"aren
Ausdr"ucke, priorisiert nach der H"aufigkeit mit der sie in den
Testdaten passen. Testen Sie den entwickelten Ausdruck. Die
.tsv Dateien spezifizieren die Zielwerte.
'''
res_for_date=[f"^[0-3]?\d\.\s({re_month})\s(\-?\d+)\s",
               "([0-3]?\d\.[01]?\d?)\.(\-?\d+)\)$",
               "[\s\(](im\sJahr)\s(\-?\d+)\)$",
              f"^({re_month})\s(\-?\d+)\s"]
filename = sys.argv[1]
try:
  stream = open(filename)
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

'''FRAGE 2 (1 Punkt): Wozu dient die folgende Variable
res_for_date_matches und was bedeutet der Ausdruck,
mit dem sie intialisiert wird?
ANTWORT:
'''

res_for_date_matches = [0] * len(res_for_date)

'''FRAGE 3 (0.5 Punkte) Wozu dient die Variable found?
ANTWORT:
'''

'''FRAGE 4 (1 Punkt): Wieviele Gruppen m"ussen in jedem der regul"aren
Ausdr"ucken definiert sein, damit das folgende Programmst"uck funktioniert und
welche Bedingungen muss der String erf"ullen, der durch die letzte Gruppe
gematcht wird? Begr"unden Sie Ihre Antwort.
ANTWORT:
'''

'''FRAGE 5 (0.5 Puntkte): Wozu dient die Variable idx in der inneren
for-Schleife?
ANTWORT:
'''

'''FRAGE 6 (0.5 Punkte): Wozu dient die Variable no_match_lines?
ANTWORT:
'''

no_match_lines = list()
for line in stream:
  line = line.rstrip()
  found = False
  for idx, this_re in enumerate(res_for_date):
    mo = re.search(r'{}'.format(this_re),line)
    if mo:
      found = True
      res_for_date_matches[idx] += 1
      try:
        year = int(mo.group(2))
      except ValueError as err:
        sys.stderr.write('{}: cannot parse integer from {}\n'
                         .format(sys.argv[0],mo.group(2)))
        exit(1)
  if not found:
    no_match_lines.append(line)
stream.close()

if no_match_lines:
  sys.stderr.write(('{}: die folgenden Zeilen in der Datei {} enthalten keine '
                    'Zeitangabe mit Jahreszahl\n').format(sys.argv[0],filename))
  for line in no_match_lines:
    sys.stderr.write('{}\n'.format(line))

print('# Treffer Statistik')
for idx in range(len(res_for_date_matches)):
  print('Anzahl der Zeilen mit Zeitangaben, die auf RE {} passen\t{}'
        .format(idx,res_for_date_matches[idx]))
print('Anzahl der Zeilen ohne Treffer eines RE\t{}'
      .format(len(no_match_lines)))
