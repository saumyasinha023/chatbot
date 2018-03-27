import sys
import nltk.data
import nltk

def determineYN(reference, question):
    defAns = "no"
    questionString = ' '.join(question)
    questionString = questionString.lower()
    question = nltk.pos_tag(question)
    ans = "no"
    key = ""
    for (word,partofspeech) in question:
        if (partofspeech == 'NN' or partofspeech == 'NNS' or partofspeech == 'NNP' or partofspeech == 'NNPS'):
            key = word.lower()
            ans = "no"
    for sentence in reference:
        if ans == "yes":
            break
        s = nltk.word_tokenize(sentence.lower())
        if key in s:
            ans = "yes"
            for (word,partofspeech) in question:
                if ans == 'no':
                    break
                if (partofspeech != '.') and (word.lower() not in s) and (partofspeech != 'DT') and (word != 'does') and (word != 'do'):
                    ans = 'no'
                    if partofspeech[0] == 'V':
                        tWord = nltk.stem.wordnet.WordNetLemmatizer().lemmatize(word,'v')
                        for (w,p) in nltk.pos_tag(s):
                            if p[0] == 'V':
                                tWord2 = nltk.stem.wordnet.WordNetLemmatizer().lemmatize(w,'v')
                                if tWord == tWord2:
                                    ans = 'yes'
                    elif word in reference[0]:
                        ans = "yes"
                if defAns == "yes":
                    if (word == "no" or word =="not"):
                        ans = "no"
                if partofspeech[0] == 'V':
                    defAns = "yes"
                else:
                    defAns = "no"
    print (ans)
