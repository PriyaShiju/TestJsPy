from collections.abc import Sequence

def use_sequence(seq: Sequence):
    print(f'Type of sequence is {type(seq)}')
    assert(issubclass(type(seq), Sequence))
    print(f'Len of Sequence is { len(seq)}' )
    print(f'Repr of sequence is {repr(seq)}')
    
    for item in seq:
        print(item)
        
    print('_' *20)
    return
    
rseq = range(0,20)  # range
lseq=[i for i in rseq] # list
sseq =  '-'.join(map(str,rseq))  # string
bseq = bytes(rseq)
baseq= bytearray(rseq)
mvseq = memoryview(bseq)
allseq =[rseq,lseq,sseq,bseq,baseq,mvseq]

for item in allseq:
    use_sequence(item)