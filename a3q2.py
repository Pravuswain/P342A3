#open all txt files 

with open('mat1q2.txt','r') as f:
	a =[[float(num) for num in line.split(',')] for line in f]
		
#print(a)

with open('mat2q2.txt','r') as f:
	b=[float(num) for num  in f]
		
#print(b)
n= len(b)
#print(n)

#function fforr partial pivoting
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

a,b=  pp(a,b)
#print(a)
#print(b)

#ffunction forr gauss-jordan method
def gj(a,b):
	#define pivot and loop over the firrrst list
	
	for i in range(0,n):

		pivot = a[i][i]

		#loop overr second list to trravvel ffforrr rrow operation
		for j in range(0,n):
			a[i][j] = a[i][j]/pivot
		b[i] = b[i]/pivot
		for k in range(0,n):
			factor = a[k][i]
			if k == i or factor== 0:
				pass
			
			else:
				
				for j in range(0,n):
					a[k][j] =a[k][j]-factor*a[i][j]
				b[k]=b[k]-factor*b[i]
			#else:
			#continue
					
	return b,a

X,A = gj(a,b)
print(f'soluion of linear equations : {X}')
print(f'transformed mattrix : {A}')

#OUTPUT
'''
soluion of linear equations : [-2.0, -2.0, 1.0]
transformed mattrix : [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

'''

