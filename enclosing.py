message ='global'
def enclosing():
    message='enclosing'
    def local():
        nonlocal message
        message ='nonlocal'
        print('nonlocal -'+ message)

    print('enclosing 1 -'+ message)
    local()
    print('enclosing 2 -'+ message)
print('global 1 -'+ message)
enclosing()
print('global 2-'+ message)
        