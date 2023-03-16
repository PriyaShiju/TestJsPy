import itertools

def averager():
    for i in itertools.starmap(lambda a,b:b/a , enumerate(itertools.accumulate([2,3,4,5,6]), 1)):
        print(f'-->{i}')
        
averager()

# python Averager.py