import scipy.io as scio
import numpy
datafile = 'usvmodel.mat'
data = scio.loadmat(datafile)
print type(data)
linearx = [ ]
for i in range(150):
    linearx.append(round(data['Trajectory'][2][i][3],2))
print linearx
numpy.save('linearx3.npy',linearx)


# # agent_number(0,1,2--1,2,3agent,0 is leader agent), step(0-maxstep),

# #print data['Trajectory'][agent_number][step]  #the state of agent

# # # agent 2 linearspeed and angular speed
# # for i in range(150):
# #     print data['Trajectory'][1][i][3:6]
# #     linearx = data['Trajectory'][1][i][3]
# #     lineary = data['Trajectory'][1][i][4]
# #     angularz = data['Trajectory'][1][i][5]
# # print type(data['Trajectory'][1][1][3])
# # print type(float(data['Trajectory'][1][1][4]))
# linearx = [ ]
# for i in range(150):
#     # linearx.extend((data['Trajectory'][1][i][3])
# # numpy.save('linearx1.npy',linearx)
# # print dat
# print (data)

# # data = numpy.load('linearx.npy')
# # print type(data[0])
# # for i in range(10):
# #     print data[i]
