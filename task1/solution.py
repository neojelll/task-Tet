def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for i, arg in enumerate(args):
            expect_type = list(annotations.values())[0]
            if not isinstance(arg, expect_type):
                raise TypeError()          
        return func(*args, **kwargs)
    return wrapper
