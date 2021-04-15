import os
from locallibs.relocatablizer import codesign, relocatablize, analyze
print(os.getenv('APP_SIGN_ID'))
# codesign("./Python.framework")