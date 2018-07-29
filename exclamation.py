def exclamationFunc(keywords, corpus, advice):
    count = 0
    for i in keywords:
        corpus = corpus.lower()
        freq = corpus.count(i)
        count = count + freq
        
    if count > 1:
        return (advice %count)
    
punct = ["!"]

puncttext = "You've used %d exclamation marks. Did you know that exclamation marks are often only used to appear friendlier? Unless you are genuinely excited, please delete some."
