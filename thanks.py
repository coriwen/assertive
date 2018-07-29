def thanksFunc(keywords, corpus, advice):
    count = 0
    for i in keywords:
        corpus = corpus.lower()
        freq = corpus.count(i)
        count = count + freq
        
    if count > 1:
        return (advice %count)

thanks = ["thank", "really appreciate it", "grateful"]

thankstext = """Did someone save your life at great personal expense? You decided to thank the recipient of this email %d times. One thank you is usually enough - can you pick your favourite and remove the others?"""
