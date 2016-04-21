import os, platform, logging

if platform.platform().startswith("Window"):
    logging_file = os.path.join(os.getenv("HOMEDRIVE"),os.getenv("HOMEPATH"),"test.log")
else:
    logging_file = os.path.join(os.getenv("HOME"),"test.log")

print("Logging to", l)