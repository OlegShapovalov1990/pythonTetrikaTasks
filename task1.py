def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        for i, (arg, value) in enumerate(zip(annotations.keys(), args)):
            expected_type = annotations[arg]
            if not isinstance(value, expected_type):
                raise TypeError(f"Argument '{arg}' must be of type {expected_type}, but got {type(value)}")

        for key, value in kwargs.items():
            if key in annotations:
                expected_type = annotations[key]
                if not isinstance(value, expected_type):
                    raise TypeError(f"Argument '{key}' must be of type {expected_type}, but got {type(value)}")

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))
try:
    print(sum_two(1, 2.4))
except TypeError as e:
    print(e)
