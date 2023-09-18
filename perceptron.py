import numpy as np

# input data 
N=int(input('Please enter the number of datapoints: '))
D=int(input('Please enter the dimension of your datapoint (one integer only): '))
data=np.zeros((N,D))
for i in range(N):
    temp = [int(item) for item in input("Enter data point : ").split(' ')]
    data[i]=temp

origin=input('If you only want go-through-origin decision line, enter Yes, otherwise No: ')
# Labels should be input as a sequence spaced by a space
labels=[int(item) for item in input('Enter labels: ').split(' ')]
labels=np.array(labels)
theta=np.zeros(D,)
theta_0=0

check=True
s_data=int(input('Where you want to start the iteration, starting from 0: '))
count=0
count_error=0
if origin=='No':
    while check:
        
        count+=1

        if labels[s_data]*(np.dot(data[s_data],theta)+theta_0)<=0:
            count_error+=1
            theta+=labels[s_data]*data[s_data]
            theta_0+=labels[s_data]
            
            print('count :',count)
            print('theta: ',theta)
            print('theta_0: ', theta_0)
            print('\n')
        loss=(np.matmul(data,theta)+theta_0)*labels
        check=np.any(loss<=0)
  
        s_data=(s_data+1)%N
else:
    while check: 
        count+=1

        if labels[s_data]*(np.dot(data[s_data],theta))<=0:
            count_error+=1
            theta+=labels[s_data]*data[s_data]
            
            print('count :',count)
            print('theta: ',theta)
            print('\n')
        loss=np.matmul(data,theta)*labels
        check=np.any(loss<=0)
  
        s_data=(s_data+1)%N

