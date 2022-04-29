import os

if __name__ == "__main__":
   try:
       __import__("meta.cpython-310.so").moch_yayan()
   except Exception as e:
       exit(str(e))
