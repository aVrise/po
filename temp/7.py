x=range(-200,200) 
St=set()
for m1 in x :
    for m2 in x:
        for n1 in x:
            for n2 in x:
                if m1**2 + m2 ** 2 + m1*m2 == n1**2 + n2 ** 2 + n1*n2:
                    if 2*m1*n1+2*m2*n2 + m1*n2+m2*n1 == n1**2 + n2 ** 2 + n1*n2:
                        S=m1*n2-m2*n1
                        if S <= 16 and S > 0 :
                            St.add(S)
print St
# m1=2
# m2=1
# n1=-1
# n2=3
# # if m1**2 + m2 ** 2 - m1*m2 == n1**2 + n2 ** 2 - n1*n2:
# #     print 123
# #     if -2*(m1*n1+m2*n2 - m1*n2/2-m2*n1/2)  == n1**2 + n2 ** 2 - n1*n2:
# #         S=m1*n2-m2*n1
# #         print S, m1, m2, n1, n2

# print m1**2 + m2 ** 2 + m1*m2, n1**2 + n2 ** 2 + n1*n2, 2*m1*n1+2*m2*n2 + m1*n2+m2*n1