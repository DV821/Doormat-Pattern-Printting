#Printing doormat pattern with user defined rows and cols
#7*21
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
# ---------.|.---------


n = int(input("Enter rows : "))
m = int(input("Enter columns : "))
pattern=[('.|.'*(2*i+1)).center(m,'-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m,'-')]+ pattern[::-1]))