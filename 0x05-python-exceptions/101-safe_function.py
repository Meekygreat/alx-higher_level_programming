#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        r = fct(*args)
        return r
    except Exception as error:
        import sys
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
