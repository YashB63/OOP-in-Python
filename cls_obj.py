# In Python, a class is a blueprint for creating objects.
#It defines a set of attributes and methods that an object of that class will have.

# An object, on the other hand, is an instance of a class. 
# It is created from a class and has all the attributes and methods defined by the class. 
# Each object created from a class can have its own unique set of attribute values,
# but it will still have the same methods and attributes as the class it was created from.



x = 63 #to test whether X is a object or not
print(type(x))#output aayega class int matlab x class int ka ek object hai



class compute:#class banaya
    
    def config(self):#usme function define kiya
        print("i7, 16GB, 1TB")#print karne ka kaam diya

comp1 = compute()#yaha hum bata rhae hai ki comp1 jo hai vo compute ka ek object hai
print(type(comp1))#object ka type test karne ke liye. Output aayega ki bhai ye main class ka object hai.


#------Ab class ke andar ke function ko kaise call kare ?-----------

compute.config(comp1)#yaha kiya kuch yu hai ki humne class ka naam likha then konse function ko call karna hia uska naam likha 
#uske baad quite simply jo class ka object banaya tha usko bracket mey daal diya. Is se proper output mil jaayega.

#--------------ab ek aur object banate hai--------------

comp2 = compute()#ek aur object bana diya class ka

#------------------Jo realtime mey tarika use hota hai class ke andar ke function ko call karne ka---
comp1.config()#object bana diya and fir uske through function call kar liya
comp2.config()#same as above




