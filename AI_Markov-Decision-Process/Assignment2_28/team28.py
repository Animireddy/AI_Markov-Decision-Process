n,m = input().split(' ')
n = int(n)
m = int(m)
arr=[]
for x in range(0,n):
	arr.append(input().split(' '))
for x in range(0,n):
	for y in range(0,m):
		arr[x][y] = float(arr[x][y])

e,w = input().split(' ')
e = int(e)
w = int(w)
end_states = []
wall = []
for x in range(0,e):
	end_states.append(input().split(' '))
for x in range(0,e):
	for y in range(0,2):
		end_states[x][y] = int(end_states[x][y])
for x in range(0,w):
	wall.append(input().split(' '))
for x in range(0,w):
	for y in range(0,2):
		wall[x][y] = int(wall[x][y])
start = []
start.append(input().split(' '))
start[0][0] = int(start[0][0])
start[0][1] = int(start[0][1])
unit_step_rew = input()
unit_step_rew = float(unit_step_rew)
original = [[float(0) for x in range(0,m)] for y in range(0,n)];
origin = [[float(0) for x in range(0,m)] for y in range(0,n)];
for x in range(n):
	for y in range(m):
		origin[x][y] = arr[x][y];
sym = [["-" for x in range(0,m)] for y in range(0,n)];
policy = [];

def validity(x,y):
	for l in range(w):
		if(x==wall[l][0] and y==wall[l][1]):
			return 0;
	if(x<n and y<m and x>=0 and y>=0):
		return 1
	else:
		return 0;
def check_in():
	for i in range(0,n):
		for j in  range(0,m):
			if(abs(original[i][j]-arr[i][j])>0.001):
				return 0;
	return 1;
visted = [[0 for x in range(0,n+1)] for y in range(0,m+1)];
def find_policy(x,y):
	if(x==3 and y==3):
		return;
	maxi = -1000;

	stri = '';
	q4=validity(x-1,y);
	q1=validity(x+1,y);
	q2=validity(x,y-1);
	q3=validity(x,y+1);
	if(q4 and maxi<arr[x-1][y] and not visted[x-1][y]):
		stri = 'Up';
		maxi = arr[x-1][y];

	if(q1 and maxi<arr[x+1][y] and not visted[x+1][y]):
		stri = 'Down';
		maxi = arr[x+1][y];
	if(q2 and maxi<arr[x][y-1] and not visted[x][y-1]):
		stri = 'Left';
		maxi = arr[x][y-1];
	if(q3 and maxi<arr[x][y+1] and not visted[x][y+1]):
		stri = 'Right';
		maxi = arr[x][y+1];
	#print(stri);
	#
	if(stri=='Up'):
		policy.append(stri);
		visted[x-1][y] = 1;
		find_policy(x-1,y);
	elif(stri=='Down'):
		policy.append(stri);
		visted[x+1][y] = 1;
		find_policy(x+1,y);
	elif(stri=='Right'):
		policy.append(stri);
		visted[x][y+1] = 1;
		find_policy(x,y+1);
	elif(stri=='Left'):
		policy.append(stri);
		visted[x][y-1]=1;
		find_policy(x,y-1);

cnt=0;
while 1:
	print("Iteration",cnt);
	cnt = cnt+1;

	flag = 0;
	for i in range(0,n):
		for j in range(0,m):
			original[i][j] = arr[i][j];

	for x in range(0,n):
		for y in range(0,m):
			print("%.3f" %(arr[x][y]),end=' ')
		print("\n")

	for x in range(0,n):
		for y in range(0,m):
			print(sym[x][y],end=' ')
		print("\n")

	visted = [[0 for x in range(0,n+1)] for y in range(0,m+1)];
	visted[3][0] = 1;
	#policy path start = (m-1,0) compare with (m-1,0+1)
	policy = [];
	print("Policy:")
	find_policy(m-1,0);
	for x in range(0,len(policy)):
		print(policy[x]);
	print("\n");

	for i in range(0,n):
		for j in range(0,m):
			val = 0;
			maxi = -10000000;
			for k in range(0,e):
				if(i==end_states[k][0] and j==end_states[k][1]):
					flag = 1;
					break;
			for k in range(0,w):
				if(i==wall[k][0] and j==wall[k][1]):
					flag = 2;
					break;
			if(flag==1 or flag==2):
				flag = 0;
				continue;
			else:
				pst1 = validity(i-1,j);
				pst2 = validity(i+1,j);
				pst3 = validity(i,j-1);
				pst4 = validity(i,j+1);
				if(pst1):
					val+=0.8*arr[i-1][j];
				else:
					val+=0.8*arr[i][j];
				if(pst3):
					val+=0.1*arr[i][j-1];
				else:
					val+=0.1*arr[i][j];
				if(pst4):
					val+=0.1*arr[i][j+1];
				else:
					val+=0.1*arr[i][j];
				maxi = max(val,maxi);
				if(maxi == val):
					sym[i][j] = "^";
				val=0;
				
				if(pst2):
					val+=0.8*arr[i+1][j];
				else:
					val+=0.8*arr[i][j];
				if(pst3):
					val+=0.1*arr[i][j-1];
				else:
					val+=0.1*arr[i][j];
				if(pst4):
					val+=0.1*arr[i][j+1];
				
				else:
					val+=0.1*arr[i][j];
				

				maxi = max(val,maxi);
				if(maxi == val):
					sym[i][j] = "v";
				val=0;

				if(pst1):
					val+=0.1*arr[i-1][j];
				else:
					val+=0.1*arr[i][j];
				if(pst2):
					val+=0.1*arr[i+1][j];
				else:
					val+=0.1*arr[i][j];
				if(pst3):
					val+=0.8*arr[i][j-1];
				else:
					val+=0.8*arr[i][j];
				maxi = max(val,maxi);
				if(maxi == val):
					sym[i][j] = "<";
				val=0;
				if(pst1):
					val+=0.1*arr[i-1][j];
				else:
					val+=0.1*arr[i][j];
				if(pst2):
					val+=0.1*arr[i+1][j];
				else:
					val+=0.1*arr[i][j];
				
				if(pst4):
					val+=0.8*arr[i][j+1];
				else:
					val+=0.8*arr[i][j];
				maxi = max(val,maxi);
				if(maxi == val):
					sym[i][j] = ">";
				arr[i][j] = unit_step_rew + maxi + origin[i][j]; 
				
	
	if(check_in()):
		break;
print("Final Output:")
for x in range(0,n):
	for y in range(0,m):
		print("%.3f" %(arr[x][y]),end=' ')
	print("\n")



