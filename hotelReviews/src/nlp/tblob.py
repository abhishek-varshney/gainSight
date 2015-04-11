from textblob import TextBlob

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''
text2= '''
My stay at the hotel was such a wonderful experience. The staff was very courteous and very helpful. My dining experience was beyond believe. I not only look for a good meal, but presentation is very important to me, and the Bellagio had them all. I have been going to Las Vegas for the past 25 years, and I must say the Bellagio filled my every expectation. I will be back next year, and will stay at the Bellagio. Your pool was great I truly enjoyed it. The price was a little bit expensive. 
'''
blob = TextBlob(text2)
print blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

print blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
# 0.060
# -0.341

#blob.translate(to="es") 
