import string
import keyword
alphas = string.ascii_letters + '_'
nums = string.digits
pykws = keyword.kwlist

print('Welcome to the Identifier Checker v1.0')
print('Testees must be at least 1 chars long.')
myInput = raw_input('Identifier to test? ')

if len(myInput) > 0:
    if myInput in pykws:
        print("invalid: symbol couldn't in python keyword list")
    else:
        if myInput[0] not in alphas:
            print('''invalid: First symbol must be
                alphabetic''')
        else:
            for otherChar in myInput[1:]:
                if otherChar not in alphas + nums:
                    print('''invalid: remaining
                    symbol must be alphanumeric''')
                    break
            else:
                print('okay as an identifier')
