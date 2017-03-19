#you can eveb create by process
words = ['this','is','just','a','test']
capatalized_words=[x.capitalize() for x in words]

print("words:" , words)
print("Capatalized words:" , capatalized_words)

#an use it for filtering the list items as well

words=['hello','worlds','foo','bar','test','python','is','awesome']
short_words=[x for x in words if len(x)<=3]
other_words=[x for x in words if x not in short_words]
words_with_e=[x for x in words if x.count('e') >= 1]

print("words:" , words)
print("short words:",short_words)
print("thers:",other_words)
print("words with e",words_with_e)



