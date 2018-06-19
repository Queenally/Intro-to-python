print ("""Welcome to madlibs
you'll be asked for different nouns and verbs, try to keep them funny""")
plural_nouns = raw_input('please give me a plural noun: ')
nouns1 = raw_input('please give me a noun: ')
noun2 = raw_input('please give me a noun: ')
song = raw_input('please give me a song: ')
verb1 = raw_input('please give me a verb: ')
verb2 = raw_input('please give me a verb: ')
madlibs = (""" LEarning to drive is a tricy process. There are a few  steps :
1.keep two %s on the steering wheel at all times
2. step on the %s to speed up and the %s to slow down
3. your parents will just love it if you play %s on the radio
4. make sure to honk your horn when you see %s on a street sign
5. THis is very important, if you are at a stoplight %s.""")

print (madlibs %(plural_nouns,nouns1,noun2,song,verb1,verb2))