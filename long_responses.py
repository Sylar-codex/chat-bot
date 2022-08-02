import random

R_job = "I am a bot so I don't have a job. Because I won't be able spend the money I make."

def unknown():
    response = ['could you please re-phrase that?',
                '...',
                'sounds okay',
                'what do you mean?'] [random.randrange(4)]
    
    return response