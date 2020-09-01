#open all txt files 

with open('mat1q1.txt','r') as f:
	a =[[float(num) for num in line.split(',')] for line in f]
		
#print(a)

with open('mat2q1.txt','r') as f:
	b=[float(num) for num  in f]
		
#print(b)
n = len(b)

def pp(a,b):
	for i in range(0,n-1):
		if abs(a[i][i]) == 0 :
			for j in range(i,n):
				if abs(a[j][i])>abs(a[i][i]) :
					a[i],a[j]=a[j],a[i]
					b[i],b[j]=b[j],b[i]
		else:
			pass			
	return a,b

A,X=  pp(a,b)



def gj(a,b):
	#define pivot and loop over the firrrst list
	for i in range(0,n):

		pivot = a[i][i]
		if pivot != 0:
		#loop overr second list to trravvel ffforrr rrow operation
			for j in range(i,n):
				a[i][j] = a[i][j]/pivot
			b[i]=b[i]/pivot
			for k in range(0,n):
				if k == i or a[k][i] == 0:
					continue
			
				else:
					factor = a[k][i]
					for j in range(i,n):
						a[k][j]=a[k][j]-factor*a[i][j]
					b[k]=b[k]-factor*b[i]
		else:
			continue			
	return b,a

X,A = gj(a,b)
print(f'soluion of linear equations : {X}')
print(f'transformed mattrix : {A}')

#OUTPUT
'''
soluion of linear equations : [3.0, 1.0, -2.0]
transformed mattrix : [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
'''