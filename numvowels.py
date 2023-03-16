def numvowels(text:str) -> int:
    return sum(1 if c.lower() in 'aeiou' else 0
               for c in text)
    
    """
    >>> import inspect
>>> sig = inspect.signature(numvowels)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>     
NameError: name 'numvowels' is not defined
>>> from numvowels import numvowels
>>> sig = inspect.signature(numvowels)
>>> sig.parameters()                  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'mappingproxy' object is not callable
>>> sig.parameters  
mappingproxy(OrderedDict([('text', <Parameter "text: str">)]))
>>> str(sig.parameters)
'OrderedDict([(\'text\', <Parameter "text: str">)])'
>>> sig.parameters['text'].annotation
<class 'str'>

    
    """