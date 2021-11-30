# this is used to take multiple arguments
def funcprint(*args):  #args is just the name use can use other also ,it is basically your tuble containg the arguments and *for all arguments
    for item in args:
        print(args)
        return args

heroes=("iron_man","hulk","thor","captain_america")
funcprint(*heroes)
   # if u wnat to give normal arg you want tyo give it before *args
# basic formant -norman arg-*args-**kwargs

# kwargs is the dictionrt multiple argument
def funcprint(**kwargs):
    for key,value in kwargs.items():
        print(f"real name of {key} is {value}")
kr={"iron_man":"tony","captain america":"steve rogers"}
funcprint(**kr)
