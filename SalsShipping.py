def groundship_cost(weight):
  if(weight<=2):
    cost=1.5*weight+20
  elif(weight<=6):
    cost=3*weight+20
  elif(weight<=10):
    cost=4*weight+20
  else:
    cost=4.75*weight+20
  return cost;
print(groundship_cost(8.4))

premium_groundship_cost=125.0

def droneship_cost(weight):
  #drone shipping = 0 Flat charge + 3*weight per pound
  #So, droneshippingcost=3x(groundshippingcost-flat) 
  cost = (groundship_cost(weight)-20)*3
  return cost;
print(droneship_cost(1.5))

def bestshippingmethod(weight):
  #Lowest Cost among the 3 Methods DRONE, GROUND and PREMIUM GROUND
  cheapest=0
  g=groundship_cost(weight)
  p=premium_groundship_cost
  d=droneship_cost(weight)
  if(g<=p):
    if(g<=d): #g<p
      cheapest=g  #g<p and g<d 
    else:
      cheapest=d #d<g and g<p  
  else:     #p<g
    if(p<=d):
      cheapest=p #p<g and p<d
    else:       #d<p and p<g  
      cheapest=d
  if(cheapest==g):
    return("Ground Shipping")
  elif(cheapest==p):
    return("Premium Ground Shipping")
  else:
    return("Drone shipping")
  return(cheapest)
print(bestshippingmethod(4.8))
