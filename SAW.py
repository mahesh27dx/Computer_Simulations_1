import numpy as np
import matplotlib.pyplot as plt

def random_walk_3D(N):
    Nsteps = range(N)
    xp,yp,zp = [0],[0],[0]
    pos = [0,0,0]
    
    rand = np.random.uniform(0,1,N)
    
    for i in Nsteps:
        # depending on the random number go right
        # left, up or down
        if 0.00000 <= rand[i] < 1.0/6.0: pos[0] = pos[0]+1
        if 1.0/6.0 <= rand[i] < 2.0/6.0: pos[0] = pos[0]-1
        if 2.0/6.0 <= rand[i] < 3.0/6.0: pos[1] = pos[1]+1
        if 3.0/6.0 <= rand[i] < 4.0/6.0: pos[1] = pos[1]-1
        if 4.0/6.0 <= rand[i] < 5.0/6.0: pos[2] = pos[2]+1
        if 5.0/6.0 <= rand[i] < 6.0/6.0: pos[2] = pos[2]-1
            
        xp.append(pos[0])
        yp.append(pos[1])
        zp.append(pos[2])

    dist = (xp[N]**2 + yp[N]**2 + zp[N]**2)**0.5
    
    return xp,yp,zp,end_end_dist
    
%matplotlib inline
Nwalks = 100
Nsteps = range(1,100)
f=open("3D_walk.txt","w+")
dMean = []
# loop through step range
for i in Nsteps:
    d = []
    # loop through number of walks and steps per walk
    for j in range(Nwalks):
        xp,yp,zp,dist = random_walk_3D(i)
        d.append(dist)
    
    f.write(str(xp[i]) + "   " + str(yp[i]) + "   " + str(zp[i]) + "   " + "\n" )
        
    # get average displacement for N walks
    dAve = np.average(d)
    dMean.append(dAve)
#print("x","   y" )
#print(xp,end = ',''\n')
f.close()
# relation should be a power function so take log both sides
x = np.log(np.array(Nsteps))
y = np.log(np.array(dMean))

# calculate slope of log-log plot to get power coefficeint
rise = y[len(y)-1] - y[0]
run = x[len(x)-1] - x[0]
slope = round(rise/run,3)

# plot mean displacement vs N steps
plt.figure()
plt.subplot(211)
plt.plot(Nsteps,dMean,label = '$<d>$')
plt.xlabel('N Steps')
plt.ylabel('$<d>$')
plt.annotate('100 Walks',fontsize=14,xy=(0.15,0.77), xycoords='figure fraction')
plt.legend(loc=2)

# plot log-log of mean displacement vs N steps 
plt.subplot(212)
plt.plot(x,y,label='Log-Log $<d>$')
plt.xlabel('log N Steps')
plt.ylabel('log $<d>$')
plt.annotate('Slope '+str(slope),fontsize=14,xy=(0.15,0.33),xycoords='figure fraction')
plt.legend(loc=2)

# plot mean of the squared displacement vs N steps
plt.subplot(212)
plt.plot(Nsteps,MdispSq,'bo-',label='$<d^2>$')
plt.xlabel('N Steps')
plt.ylabel('Mean Squared Displacement')
plt.legend(loc=2)