def username_generator(first,last):
  if len(first)<3 or len(last)<4:
    return(first+last)
  else:
    return(first[:3]+last[:4])

def password_generator(username):
  password=""
  #Shifting right
  '''password=username[-1]+username[:-1]
  return password;'''
  '''OR'''
  #loop used for shift
  for i in range(len(username)):
    password+=username[i-1]   
  return(password)

