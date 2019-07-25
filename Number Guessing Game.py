maxi=int(input('The maximum is:'))
mini=int(input('The minimum is;'))

while maxi<=mini:
    print('Please enter a number lower than'+str(maxi))
    mini=int(input('The minimum is;'))

ans=int(input('The answer is(between '+str(mini)+' and '+str(maxi)+'):'))

while ans<mini or ans>maxi:
    print('Please enter the answer(between '+str(mini)+' and '+str(maxi)+'):')
    ans=int(input('The answer is(between '+str(mini)+' and '+str(maxi)+'):'))

gue=int(input('The guessing number is(between '+str(mini)+' and '+str(maxi)+'):'))

while gue<mini or gue>maxi:
    print('Please enter the guessing number(between '+str(mini)+' and '+str(maxi)+'):')
    gue=int(input('The guessing number is:'))

def sep(a,b,c,d):
    if d<b:
        print('The answer is between '+str(d)+' and'+str(c))
        a=d
        d=int(input('The guessing number is:'))
        return sep(a,b,c,d)
    elif d>b:
        print('The answer is between '+str(a)+' and'+str(d))
        c=d
        d=int(input('The guessing number is:'))
        return sep(a,b,c,d)
    else:
        print('You are RIGHT')
        print('The answer is '+str(d))

sep(mini,ans,maxi,gue)