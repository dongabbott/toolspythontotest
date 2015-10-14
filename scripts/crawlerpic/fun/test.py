import settings
import os


if os.path.exists('./tmp/images'):
    print 'aaaaaaaa'
else:
    os.makedirs('./tmp/images')