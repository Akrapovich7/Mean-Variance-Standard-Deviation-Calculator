import numpy as np
list=[0,1,2,3,4,5,6,7,8]

def calculate(list):
  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")

  list=np.array(list).reshape(3,3)

  #Mean
  axis1_mean=np.mean(list,axis=0).tolist()
  axis_2_mean=np.mean(list,axis=1).tolist()
  flattend_mean=np.mean(list).item()

  #Variance
  axis1_var=np.var(list,axis=0).tolist()
  axis2_var=np.var(list,axis=1).tolist()
  flattened_var=np.var(list).item()

  #Standard deviation
  axis1_std=np.std(list,axis=0).tolist()
  axis2_std=np.std(list,axis=1).tolist()
  flattened_std=np.std(list).item()

  #Max
  axis1_max=np.max(list,axis=0).tolist()
  axis2_max=np.max(list,axis=1).tolist()
  flattend_max=np.max(list).item()
  
  #Min
  axis1_min=np.min(list,axis=0).tolist()
  axis2_min=np.min(list,axis=1).tolist()
  flattened_min=np.min(list).item()

  #Sum
  axis1_sum=np.sum(list,axis=0).tolist()
  axis2_sum=np.sum(list,axis=1).tolist()
  flattened_sum=np.sum(list).item()



  calculations={
  'mean': [axis1_mean, axis_2_mean, flattend_mean],
  'variance': [axis1_var, axis2_var, flattened_var],
  'standard deviation': [axis1_std, axis2_std, flattened_std],
  'max': [axis1_max, axis2_max, flattend_max],
  'min': [axis1_min, axis2_min, flattened_min],
  'sum': [axis1_sum, axis2_sum, flattened_sum]
      
  }
  

  return calculations
calculate(list)
