import itertools
import re
def solve(formula):
    return filter(valid, letter_replacements(formula))
def letter_replacements(formula):
    formula = formula.replace(' = ', ' == ') # Allow = or ==
    letters = cat(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        yield formula.translate(str.maketrans(letters, cat(digits)))
def valid(exp):
    try:
        return not leading_zero(exp) and eval(exp) is True
    except ArithmeticError:
        return False
cat = ''.join
leading_zero = re.compile(r'\b0[0-9]').search
str1=input("Enter first string: ")
str2=input("Enter second string: ")
str3=input("Enter third string: ")
str4=str1+' + '+str2+' = '+str3
print("Input string is '",str4,"'")
next(solve(str4))