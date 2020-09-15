import sys

argv = sys.argv

it = '-it' in argv
rm = '--rm' in argv

if not it:
    errorMsg = 'Usage: python script.py [-it]'
    if not rm: errorMsg += '{--rm}'
    print(errorMsg)
    sys.exit()

corMsg = 'You have used module correct. '
if not rm: corMsg += 'You could have used optional parameter {--rm}.'
print(corMsg)
