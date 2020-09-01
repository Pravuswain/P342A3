
with open('mat1q3.txt','r') as f:
	a =[[float(num) for num in line.split(',')] for line in f]
		
#print(a)
n= len(a)
#print(n)
I = [[1,0,0],[0,1,0],[0,0,1]]
#function fforr partial pivoting
def pp(a):
	for i in range(0,n-1):
		if abs(a[i][i]) == 0 :
			for j in range(i,n):
				if abs(a[j][i])>abs(a[i][i]) :
					a[i],a[j]=a[j],a[i]
					
		else:
			pass			
	return a

a=  pp(a)
#print(a)
#print(b)

#ffunction forr gauss-jordan method
#using same opeation on I as on A while reducing A to reduced row echlon form
def gj(a,I):
	#define pivot and loop over the firrrst list
	
	for i in range(0,n):

		pivot = a[i][i]

		#loop overr second list to trravvel forrr rrow operation
		for j in range(0,n):
			a[i][j] = a[i][j]/pivot
			I[i][j] = I[i][j]/pivot

		for k in range(0,n):
			factor = a[k][i]
			if k == i or factor== 0:
				pass
			
			else:
				
				for j in range(0,n):
					a[k][j] =a[k][j]-factor*a[i][j]
					I[k][j] =I[k][j]-factor*I[i][j]

			#else:
			#continue
					
	return I,a
B,A= gj(a,I)
print(f'Inverse of A : {B}')

#cross product
#calling back a for cross productt
with open('mat1q3.txt','r') as f:
	a =[[float(num) for num in line.split(',')] for line in f]
		

def cp(a,b)	:
	cross = [[0,0,0],[0,0,0],[0,0,0]]
	for i in range(0,n):
		for j in range(0,n):
			for k in range(0,n):
				
				cross[i][j] += a[i][k]*b[k][j]

	return cross
C = cp(a,B)

print(f"AxA^-1 :{C}")

#OUTPUT
'''
Inverse of A : [[-3.0, 3.0, -7.0], [1.0, 1.0, 0.0], [1.0, 0.0, 1.0]]
AxA^-1 :[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

'''


