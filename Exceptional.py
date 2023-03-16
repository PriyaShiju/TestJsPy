from math import log
import sys

digit_map ={ 'zero':'0',
    'one':'1',
    'two':'2',
    'three' :'3',
    'four':'4',
    'five':'5',
    'six': '6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}

def convert(s):
    try :
        number=''
        for token in s:
            number += str(digit_map[token])
        x=int(number)
        print(f"success x={x}" )
    except (KeyError,TypeError) as e:
        print(f"Failed - {e!r}", file=sys.stderr)
        raise
    
     #   x=-1
    #return x

def string_log(s):
    v=convert(s)
    return(log(v))
