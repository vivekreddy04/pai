import math
def minmax(curdepth,nodeindex,maxturn,scores,target):
    if curdepth==target:
        return(scores[nodeindex])
    if maxturn:
        return max(minmax(curdepth+1,nodeindex*2,False,scores,target),minmax(curdepth+1,nodeindex*2+1,False,scores,target))
    else:
        return min(minmax(curdepth+1,nodeindex*2,True,scores,target),
        minmax(curdepth+1,nodeindex*2,maxturn,scores,target)
        )
scores=[3, 5, 2, 9, 12, 5, 23, 23]
treedepth=math.log(len(scores),2)
print("optimal value",end='')
print(minmax(0,0,True,scores,treedepth))
