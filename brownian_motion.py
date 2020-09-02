import numpy as np 

def brownian_displacement_simulation( k = 20, n = 1001, m = 2, d = 10.0, 
  t = 1.0): 
    
  dsq = np.zeros([k, n]) 
  for i in range(0,k): 
    x = brownian_motion_simulation(m,n,d,t)
    dsq[i,0:n] = np.sum(s[0:m, 0:n] ** 2, 0) 
    
    
  return dsq
  
def brownian_motion_simulation(m = 2, n = 1001, d = 10.0, t = 1.0): 
  dt = t/float(n-1) 
  x = np.zeros([m,n]) 
  
  for j in range(1,n): 
  
    s = np.sqrt(2.0 * m * d * dt) * np.random.randn(1)
    
    if(m==1): 
      dx = s*np.ones(1)
    else: 
      dx = np.random.randn(m) 
      norm_dx = np.sqrt(np.sum(dx**2)) 
      for i in range(0,m): 
        dx[i] = s * dx[i]/norm_dx
        
        
     x[0:m,j] = x[0:m,j-1] + dx[0:m] 
     
  return x 
  
  
  
    
