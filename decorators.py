def handle_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("===== Printing Exception(s) =====")
            print(e)

    return wrapper