from nltk.tokenize import word_tokenize
from collections import Counter
from math import log
from random import randint
from pyswip import Prolog
prolog = Prolog()
prolog.consult("paraphrase.pl")

def paraphrase(sent):
    sent = " ".join(sent)
    query = list(prolog.query("paraphrase(\"%s\",R)"%sent))
    if len(query) == 0:
        return sent
    choice = query[randint(0,len(query)-1)]['R']
    return choice

def summarize(paragraph):
    sents = [word_tokenize(x) for x in paragraph.split(". ")]
    flat_sents = [y for x in sents for y in x]
    n = len(sents)
    sents_count= Counter(flat_sents)

    sent_weights = []
    for sent in sents:
        weights = []
        n_sent = len(sent)
        sent_count = Counter(sent)
        for token, count in sent_count.items():
            weights.append((count/n_sent)*log(n/sents_count[token]))
        sent_weights.append(sum(weights)/n_sent)

    summary = []
    c = 0
    while c < n/2:
        max_i = -1
        max_w = -1
        for i,entry in enumerate(sent_weights):
            if entry is not None and entry > max_w:
                max_w = entry
                max_i = i
        sent_weights[max_i] = None
        summary.append((max_i,paraphrase(sents[max_i])))
        c += 1

    summary = sorted(summary, key = lambda x: x[0])
    summary = [v[1] for v in summary]
    return summary

examples = ["You don't understand. Johnny Fontane never gets that movie. That part is perfect for him. It'll make him a big star. I'm gonna run him out of the movies. And let me tell you why. Johnny Fontane ruined one of Woltz International's most valuable proteges. For three years we had her under contract, singing lessons, dancing lessons, acting lessons. I spent hundreds of thousands of dollars. I was gonna make her a big star. And let me be even more frank, just to show you that I'm not a hard-hearted man, that it's not all dollars and cents. She was beautiful! She was young, she was innocent. She was the greatest piece of ass I've ever had, and I've had 'em all over the world. And then Johnny Fontaine comes along with his olive oil voice and guinea charm and she runs off. She threw it all away just to make me look ridiculous. And a man in my position can't afford to be made to look ridiculous. Now you get the hell out of here! And if that goomba tries any rough stuff, you tell him I ain't no bandleader. Yeah, I heard that story. [Hagen has been calmly eating his meal throughout Woltz's tirade]",
        'I believe in America. America has made my fortune. And I raised my daughter in the American fashion. I gave her freedom but I taught her never to dishonor her family. She found a "boy friend," not an Italian. She went to the movies with him. She stayed out late. I didn\'t protest. Two months ago he took her for a drive, with another boy friend. They made her drink whiskey and then they tried to take advantage of her. She resisted. She kept her honor. So they beat her. Like an animal. When I went to the hospital her nose was broken. Her jaw was shattered, held together by wire. She couldn\'t even weep because of the pain. But I wept. Why did I weep? She was the light of my life. A beautiful girl. Now she will never be beautiful again. [He breaks down at this point, and the Don gestures to his son to get him a drink]Sorry... [He regains his composure and carries on] I went to the police, like a good American. These two boys were brought to trial. The judge sentenced them to three years in prison, and suspended the sentence. Suspended sentence! They went free that very day! I stood in the courtroom like a fool, and those two bastards, they smiled at me. Then I said to my wife, "For justice, we must go to Don Corleone."', 
        "Well, when Johnny was first starting out, he was signed to a personal services contract with this big-band leader. And as his career got better and better, he wanted to get out of it. But the band leader wouldn't let him. Now, Johnny is my father's godson. So my father went to see this bandleader and offered him $10,000 to let Johnny go, but the bandleader said no. So the next day, my father went back, only this time with Luca Brasi. Within an hour, he had a signed release for a certified check of $1000.",
        'The rules of the Hunger Games are simple. In punishment for the uprising, each of the twelve districts must provide one girl and one boy, called tributes, to participate. The twenty-four tributes will be imprisoned in a vast outdoor arena that could hold anything from a burning desert to a frozen wasteland. Over a period of several weeks, the competitors must fight to the death. The last tribute standing wins.']

for example in examples:
    summary = summarize(example)

    print("=============Example=============")
    print("Original:", example)

    print("----")
    print("Summarized:")
    output = ". ".join([x for x in summary])
    print(output)

while True:
    text = input("Enter new paragraph to summarize, or press [Enter] to quit.\n")
    if text == "":
        break
    else:
        summary = summarize(text)

        print("Summarized:")
        output = ". ".join([x for x in summary])
        print(output)
