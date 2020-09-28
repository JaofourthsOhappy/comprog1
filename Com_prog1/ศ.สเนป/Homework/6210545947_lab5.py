#No.1
def change_second_char(string,char):
    """
    >>> change_second_char('bald',"o")
    'bold'
    >>> change_second_char('paruj',"e")
    'peruj'
    >>> change_second_char('iphone',"a")
    'iahone'
    """
    string = string[0:1] + str(char) + string[2:]
    return str(string)

#No.2
def change_index_char(string,char,index):
    """
    >>> change_index_char("paruj","o",2)
    'paouj'
    >>> change_index_char("paruj","k",-2)
    'parkj'
    >>> change_index_char("paruj","l",7)
    'Error:index out of range'
    """
    if index >= len(string):
        return "Error:index out of range"
    else: 
        string = string[0:int(index)]+ str(char)+ string[int(index+1):]
        return str(string)

#No.3
def fix_start(s):
    """
    >>> fix_start('pparujjj')
    p*arujjj
    >>> fix_start('maemeungmaitai')
    mae*eung*aitai
    >>> fix_start('electrotelethermometer')
    el*ctrot*l*th*rmom*t*r
    """
    print(s[0],end = '')
    for i in s[1:]:
        if i == s[0]  :
            print('*',end = '')
        else :
            print(i,end = '')
#No.4
def count_vowels(word):
    """
    >>> count_vowels('aeiou')
    5
    >>> count_vowels('aaaaaa')
    6
    >>> count_vowels('paruj')
    2
    """
    sum = 0
    for i in word:
        if i == 'a' or i =='e' or i =='i' or i== 'o' or i == 'u':
            sum += 1
    return (sum)

#No.5
def both_ends(s):
    """
    >>> both_ends('kaopun')
    'kaun'
    >>> both_ends('kuy')
    ' '
    >>> both_ends('paruj')
    'pauj'
    """
    if len(s)<4 :
        return ' '
    else:
        s = s[0:2] + s[-2] + s[-1]
        return str(s)
#No.6
def mix_up(a,b):
    """
    >>> mix_up('mix','pod')
    'pox mid'
    >>> mix_up('kao','pun')
    'puo kan'
    >>> mix_up('iq','low')
    'error'
    """
    if len(a) <3 or len(b) <3 :
        return "error"
    else:
        s = b[0:2]+a[-1] +' ' + a[0:2]+b[-1]
        return s
#No.7
def verbings (s):
    """
    >>> verbings('mix')
    'mixing'
    >>> verbings('suck')
    'sucking'
    >>> verbings('io')
    'io'
    """
    if len(s) >= 3:
        if s[-1] == 'i' and s[-2] == 'n' and s[-3] == 'g':
            s = s+ 'ly'
        else:
            s = s + 'ing'
    return str(s)

#No.8
def not_bad (s):
    """
    >>> not_bad("This subject is not so bad")
    'This subject is good'
    >>> not_bad("You're not bad")
    "You're not bad"
    >>> not_bad("Your score is not that bad")
    'Your score is good'
    """
    x = s.find("not bad")
    if x == -1:
        b = s.find('not')
        c = s.find('bad')
        s = s[0:b]+'good'+s[c+3:]
    return str(s)


#No.9
def front_back(a,b):
    """
    >>> front_back('abcde','xyz')
    'abcxydez'
    >>> front_back('qwerty','kaopun')
    'qwekaortypun'
    >>> front_back('computer','program')
    'compproguterram'
    """
    if len(a)%2 == 0 :
        half_a = int(len(a)/2)
        a1 = a[0:half_a]
        a2 = a[half_a:]
    else :
        half_a = int(len(a)/2)
        a1 = a[0:half_a+1]
        a2 = a[half_a+1:]
    if len(b)%2 == 0:
        half_b = int(len(b)/2)
        b1 = b[0:half_b]
        b2 = b[half_b:]
    else :
        half_b = int(len(b)/2)
        b1 = b[0:half_b+1]
        b2 = b[half_b+1:]
    string = a1+b1+a2+b2
    return string        
        
    
