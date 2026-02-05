def whee(times):
    def wrapperWrapper(func):
        def wrapper():
            for _ in range(times):
                print("Something is happening before the function is called.")
                func()
                print("Something is happening after the function is called.")
        return wrapper
    return wrapperWrapper

@whee(3)
def say_whee():
   print("Whee!")
say_whee()