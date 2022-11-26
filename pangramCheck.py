"""pangram"""
def pangramCheck(s):
    # Write your code here
    
    processed = [i for i in range(97,122)]
    inputstr = set(s.lower())
    for i,letter in enumerate(inputstr):
        if ord(letter) in processed:
            processed.remove(ord(letter))
            # processed.append(letter)
    if len(processed)>0:
        return 'not pangram'
    return 'pangram' 
