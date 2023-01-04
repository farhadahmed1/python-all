greet_words = ['hi', 'hello']
bye_words = ['bye', 'tata']
bad_words = ["cat" , "dog"]


def listen():
    return input("Say Something: ")

def decide(commend):
    #print (commend)
    commend = commend.lower()
    broken_words = commend.split(" ")
    #print(broken_words)
    for word in broken_words:
        if word in greet_words: 
            talkback("Welcome man")
            break
        elif word in bye_words:
            talkback("okay bye dear.take care Man") 
            break   
        elif word in bad_words:
            talkback("Your are a bad guy . Behave yourself.")
            break

def talkback(response):
    print(response) 

user_commend = listen()
decide(user_commend)