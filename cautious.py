def cautiousFunc(keywords, corpus, advice):
    count = 0
    for i in keywords:
        corpus = corpus.lower()
        freq = corpus.count(i)
        count = count + freq
        
    if count > 1:
        return (advice %count)

cautious =  ["would you mind", "do you think", "would it be possible", "if it’s no bother", "no worries", "if it’s okay", 
            "if you don’t mind", "too inconvenient", "don't worry if not"]

cautioustext = """You seem pretty hesistant in your email - you've used %d phrases that indicate you're worried to inconvenience the recipient. Just ask Thomas for that report he owes you, he's three days late already!"""
