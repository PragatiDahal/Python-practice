def func1():
    try:
        l=[1,5,6,7]
        i=int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally: #it is exceuted irrespective of exceution of try and except
        print("I am always exceuted")

x=func1()
print(x)