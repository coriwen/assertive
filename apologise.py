apologies = ["sorry", "apologise", "apologies", "hope it's not too late"]

apologytext = """Wow, you must be really sorry! You apologised an entire %d times in your email. Unless you accidentally ran over your supervisor's puppy, that's really not necessary."""

def apologiseFunc(keywords, corpus, advice):
    count = 0
    for i in keywords:
        corpus = corpus.lower()
        freq = corpus.count(i)
        count = count + freq
        
    if count > 1:
        return (advice %count)
