import os

if __name__ == "__main__":
   try:
       __import__("krek").moch_yayan()
   except Exception as e:
       exit(str(e))
