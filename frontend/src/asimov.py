#K = ['2ZEBRAS ']
#C = 'TRXMJZJONXHPSSRBX2IXRGAXOJB2VXHRMMVXE MCNOH2N'

K = ['CANDY24','JINGLE 98','TINSEL43','8 XMAS','STOCKING7','CLAUS','HOLIDAY 789','RUDOLPH','1 CHIMNEY','CAROLING3']
C = 'Z5VGFPEIMVFAVLHKKFNMV3WWVGFNHNFDMV5WWWVOKPMMDBVMGKFPNMVXWWVB7NKDMVFAVMFPGVOKFN V2WWWVYPCIKFGMVZWWWVLHEITVLHEDMVXVBHKYDVOFSVFAV7OPGKFADEVHEIVNFIHTMVGHGDK';

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789'

for k in K:
    m = k  
    for ch in alpha:
        if ch not in m:
            m += ch
    out = ''
    for ch in C:
        pos = m.index(ch)
        out += alpha[pos]
    print(out)

