import numpy as np

# input data 
N=int(input('Please enter the number of datapoints: '))
D=int(input('Please enter the dimension of your datapoint (one integer only): '))
data=np.zeros((N,D))
for i in range(N):
    temp = [int(item) for item in input("Enter data point : ").split(' ')]
    data[i]=temp
# data=np.array([[-4,2],[-2,1],[-1,-1],[2,2],[1,-2]])
# n=len(data)
# labels=np.array([1,1,-1,-1,-1])
# theta=np.array([-4,2])
# theta_0=-3
print(data.shape)
