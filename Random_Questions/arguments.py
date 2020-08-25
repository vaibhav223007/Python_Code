def argument(name, message):
    print(f"Hello {name}, {message}")


argument("vaibhav", "good morning")

# default argumnet
def default_argument(name, message="good morning"):
    print(f"Hello {name}, {message}")


default_argument("vishal")
default_argument("vinit", "good night")

# keyword argument
def keyword_argumnet(**kwargs):
    if kwargs:
        print("Hello {0}, {1}".format(kwargs["name"], kwargs["message"]))
        print(f"Your favourite food is {kwargs['food']}")


keyword_argumnet(name="vaibhav", message="How are you?", food="chicken")

# arbitrary argument
def arbitrary_argument(*names):
    # takes argument in form of tuple
    print(names)
    for name in names:
        print(name)

arbitrary_argument("vaibhav", "vishal", "nikhil", "pramod")

