sur = ['sur', 'ova', 'cl', 'cla', 'ptd', 'ptc']
data=[]
# sur = ['sur']
ele = []
topl = 11
topmc = 0
layermc = 0

for i in range(len(sur)):

    # Read POSCAR
    temp = open('POSCAR_'+sur[i], 'r').readlines()
    temp = [[y for y in x.strip().split() if y != ' '] for x in temp]
    temp2 = []
    for ii in range(len(temp[5])):
        temp2 += int(temp[6][ii])*[temp[5][ii]]
    ele.append(temp2)

    # Read ACF
    temp = open('ACF_'+sur[i]+'.dat').readlines()
    temp = [[float(y) for y in x.strip().split() if y != ' '] for x in temp[2: 2+len(ele[i])]]
    top = []
    layer = []
    layerl = []
    for ii in temp:
        im = int(ii[0])
        if ii[3] > topl:
            top.append([im, ele[i][im-1], ii[1], ii[2], ii[3], ii[4]])
        elif layerl == []:
            layerl.append(ii[3])
            layer.append([])
        else:
            for iii, iij in enumerate(layerl):
                if abs(ii[3] - iij) < 0.5:
                    break
            else:
                layerl.append(ii[3])
                layer.append([])
                iii = len(layer) - 1
            layer[iii].append([im, ele[i][im-1], ii[1], ii[2], ii[3], ii[4]])
    topmc=max(topmc,len(top))
    for ii in layer:
        layermc = max(layermc,len(ii))
    layerl=sorted(zip(layerl,range(len(layerl))))
    layert=[]
    for ii in range(len(layerl)):
        layer[layerl[ii][1]].sort(key=lambda a:a[3])
        layert.append(sorted(layer[layerl[ii][1]], key=lambda a:a[2]))
    layert.append(sorted(top, key=lambda a: a[2]))
    data.append(layert)

output=[]
for i in range(len(sur)):
    if i == 0:
        for ii in data[0]:
            for iii in ii:
                output.append(iii[1:])

# for i in output:
#     print i


    # for ii in range(len(layert)-1):
    #     if layert[ii][0][4] >= layert[ii+1][0][4]:
    #         print layert[ii][0],layert[ii+1][0]
    #         print "error in ",ii," !!!"
    #         break
    #     for iii in range(len(layert[ii])-1):
    #         if layert[ii][iii][2] > layert[ii][iii+1][2]:
    #             print layert[ii][iii],layert[ii][iii+1]
    #             print "erroror in",ii,":",iii,"!!!" 
    #             break

    #         elif layert[ii][iii][2] == layert[ii][iii+1][2] and layert[ii][iii][3] >= layert[ii][iii+1][3]:
    #             print layert[ii][iii][3], layert[ii][iii+1][3]
    #             print "errororor in",ii,":",iii,"!!!!!"
    #             break
    # print layert






# print ele
