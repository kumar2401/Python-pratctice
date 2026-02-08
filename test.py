class test(): 
  fruit_prices={
   
      "apple":1.2,
       "banana":0.5,
       "cherry":2.5
   

  }
  for key in fruit_prices.values():
    print("keys -",key)
d1={'a':10,'b':20}
d2={'b':30,'c':40}
for k in d2:
  if k in d1:
   d1[k]=d1[k]+d2[k]
   print(d1[k]) 
  else  :
   d1[k]=d2[k]
print(d1)  