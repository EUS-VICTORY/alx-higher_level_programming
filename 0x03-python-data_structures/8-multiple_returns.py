#!/usr/bin/python3
def multiple_returns(sentence):
    if len sentence == 0:
        sentence[0] = None
        return None
    else:
        return len(sentence), sentence[0]
