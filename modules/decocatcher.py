from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            if func.__name__=="add_contact" and not isinstance(int(args[0][2]), int) or not isinstance(args[0][1], str):
                raise ValueError
            if func.__name__=="change_contact" and not isinstance(int(args[0][2]), int) or not isinstance(args[0][1], str):
                raise ValueError
            return func(*args, **kwargs)
        except ValueError:
            return "Wrong data type"
        except IndexError:
            return "Give me name and phone please."
        except KeyError:
            return "Unknown name"

    return inner
