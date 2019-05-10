
def dship(weight):
    if weight >= 10:
      return weight * 14.25
    elif (weight >= 6 ) or (weight = 10):
      return weight * 12.00
    elif (weight >= 2) or (weight = 6):
      return weight * 9.00
    else:
      return weight * 4.50

def dship(weight):
    if weight >= 10:
      return weight * 14.25
    elif (weight >= 6 ) or (weight == 10):
      return weight * 12.00
    elif (weight >= 2) or (weight == 6):
      return weight * 9.00
    else:
      return weight * 4.50

print(dship(50))


prm_grd_sh = 125
def grd_sh(weight):
  if weight > 10:
    return (4.75 * weight) + 20.00
  elif (weight > 6) or (weight == 10):
    return (4.00 * weight) + 20.00
  elif (weight >= 2) or (weight == 6):
    return (3.00 * weight) + 20.00
  else:
    return (1.50 * weight) + 20.00
    
    

def dship(weight):
    if weight >= 10:
      return weight * 14.25
    elif (weight >= 6 ) or (weight == 10):
      return weight * 12.00
    elif (weight >= 2) or (weight == 6):
      return weight * 9.00
    else:
      return weight * 4.50
    
def prm_grd(weight):
  return prm_grd_sh

def fin_cost(weight):
  if ((grd_sh(weight)) < (dship(weight))) and ((grd_sh(weight)) < (prm_grd(weight))):
    return "With a price of, $" + str(grd_sh(weight)) + ", Ground shipping is cheaper than drone and premium ground shipping"
  elif ((prm_grd(weight)) < (dship(weight))) and ((prm_grd(weight)) < (grd_sh(weight))):
    return "With a price of, $" + str(prm_grd(weight)) + ", premium ground shipping is cheaper than drone and ground shipping"
  else:
    return "With a price of, $" + str(dship(weight)) + ", drone shipping is cheaper than ground and premium ground shipping"

print("To find the cheapest method of shipping type print(fin_cost(weight)) and insert the weight of your package in the corresponding parenthesis"



def grd_sh(weight):
  if weight > 10:
    return (4.75 * weight) + 20.00
  elif (weight > 6) or (weight == 10):
    return (4.00 * weight) + 20.00
  elif (weight >= 2) or (weight == 6):
    return (3.00 * weight) + 20.00
  else:
    return (1.50 * weight) + 20.00
    
    

def dship(weight):
    if weight >= 10:
      return weight * 14.25
    elif (weight >= 6 ) or (weight == 10):
      return weight * 12.00
    elif (weight >= 2) or (weight == 6):
      return weight * 9.00
    else:
      return weight * 4.50
    
def prm_grd(weight):
  return prm_grd_sh

def fin_cost(weight):
  if ((grd_sh(weight)) < (dship(weight))) and ((grd_sh(weight)) < (prm_grd(weight))):
    return "With a price of, $" + str(grd_sh(weight)) + ", Ground shipping is cheaper than drone and premium ground shipping"
  elif ((prm_grd(weight)) < (dship(weight))) and ((prm_grd(weight)) < (grd_sh(weight))):
    return "With a price of, $" + str(prm_grd(weight)) + ", premium ground shipping is cheaper than drone and ground shipping"
  else:
    return "With a price of, $" + str(dship(weight)) + ", drone shipping is cheaper than ground and premium ground shipping"

print("To find the cheapest method of shipping type print(fin_cost(weight)) and insert the weight of your package in the corresponding parenthesis"


