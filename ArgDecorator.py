def check_nonnegative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError('Argument{} must be nonnegative'.format(index))
            return f(*args)
        return wrap
    return validator

@check_nonnegative(1)
def create_list(value,size):
    return [value]*size



