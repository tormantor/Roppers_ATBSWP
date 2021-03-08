import re

text='The ADJECTIVE madman greeted NOUN and started VERB . A nearby NOUN was seriously traumatized witnessing the event.'
adjective=input('Enter an adjective: \n')
noun1=input('Enter a noun: \n')
verb=input('Enter a verb: \n')
noun2=input('Enter a noun: \n')
adjectiveRegex=re.compile('ADJECTIVE')
nounRegex=re.compile('NOUN')
verbRegex=re.compile('VERB')
text=adjectiveRegex.sub(adjective,text)
text=verbRegex.sub(verb,text)
text=nounRegex.sub(noun1,text,1)
text=nounRegex.sub(noun2,text)
print(text)
