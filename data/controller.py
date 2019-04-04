from data.models import Greeting

def add_greeting(name, greeting_str):
    '''
    Adds a Greeting to the database.
    Return None if there is an issue
    '''
    try:
        greeting = Greeting(
            name=name, 
            greeting=greeting_str[:-1],
            punctuation=greeting_str[-1],
        )
        greeting.save()
    except Exception as e:
        print(e)
        return None
    
    return greeting

def get_greeting(name):
    try:
        return Greeting.objects.get(name=name)
    except Exception as e:
        print(e)
        pass

    return None