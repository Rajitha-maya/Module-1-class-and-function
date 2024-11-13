class multifunction():
    def SubfieldsInAI():
        list=['Sub fields in AI are:','Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        for fields in list:
            print(fields)
            
    def oddeven(num):
    num=int(input("Enter the Number:"))
        if num%2==1:
            print(num,"is odd number")
        elif num%2==0:
            print(num,"is even number")
            
    def marriage():
        gender=input("Your gender:")
        age=int(input("your age:"))
        if(gender=="male" and age<21)or(gender=="female" and age<18):
            print("Not eligible")
        else:
            print("Eligible")
    

    def subjects():
        Subject1=int(input("Subject 1:"))
        Subject2=int(input("Subject 2:"))
        Subject3=int(input("Subject 3:"))
        Subject4=int(input("Subject 4:"))
        Subject5=int(input("Subject 5:"))
        total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        percentage = total / 500*100
        print("Total:",total)
        print("Percentage:",percentage)
    
    def areaoftriangle(Height,Breadth):
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        area=Height*Breadth/2
        print("Area of Triangle:",area)
        return area
    
    
    def perimeteroftriangle(Height1,Height2,Breadth):
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        perimeter=Height1+Height2+Breadth
        print("Perimeter of Triangle:",perimeter)
        return perimeter