def iterations(type: str = None):
    
    match type:
        case 'for':
            print('Iteration with for:')
            for i in range(10):
                print(i)
        case 'while':
            i = 1
            print('Iteration with while:')
            while i <= 10:
                print(i)
                i += 1
        case _:
            print('Iteration with count:')
            count()

def count(i=1):
    if i <= 10:
        print(i)
        count(i + 1)    

iterations('for')
iterations('while')
iterations()