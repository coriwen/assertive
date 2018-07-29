def qualifierFunc(keywords, corpus, advice):
    count = 0
    for i in keywords:
        corpus = corpus.lower()
        freq = corpus.count(i)
        count = count + freq
        
    if count > 1:
        return (advice %count)
    
qualifiers = ['just', 'actually', "anyway", "not sure", "not certain", "not an expert", 
              "no expert", "anyways", "not sure, but", "i think", "i feel"]

qualifiertext = """Qualifiers are words like 'just' and 'actually' and phrases like 'I'm not an expert, but...' that undermine what you're saying before you've even said it. You're using %d of them, oh my. Get rid of them - you know what you're talking about."""
