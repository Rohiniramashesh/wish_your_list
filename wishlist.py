import pickle
import os

if os.path.exists("flipcart.dat"):
     f=open("flipcart.dat","rb" )
     cart=dict(pickle.load(f))
else:
   cart=dict()
while True:
    print("1.ADD TO CART")
    print("2.LIST CART")
    print("3.MODIFY QTY")
    print("4.REMOVE FROM CART")
    print("5.EXIT")
    
    ch=int(input())
    if ch==1:
        print("enter itemcoder,descr,qty,cost")
        code=int(input())
        descr=input()
        qty=int(input())
        cost=int(input())
        L=[descr,qty,cost]
        cart[code]=L
        
        
    elif ch==2:
        if len(cart)==0:
            print("cart empty")
            
        else:    
           print("item in cart")
           for e in cart.keys():
              print(cart.get(e))
            
            
    elif ch==3:
        print("enter item code")
        itemcode=int(input())
        if cart.get(itemcode)==None:
            print("item not found")
        else:
            v=cart.get(itemcode)
            print("+ or -")
            choice=input()
            if choice=="+" :
                v[1]+=1
            elif choice=="-"and v[1]>1:
                v[1]-=1
                
                
    elif ch==4:
         print("enter code")
         itemcode=int(input())
         if cart.get(itemcode)==None:
             print(" item not found")
         else:
             cart.pop(itemcode)
                
                
    elif ch==5:
          f = open("flipcart.dat","wb")
          pickle.dump(cart,f)
          f.close()
          break         