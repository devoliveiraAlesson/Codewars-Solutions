def solution(text, ending):
    return ending in text and text[-1] == ending[-1]
    
    # sim eu sei que tem função nativa
    #return text.endswith(ending)