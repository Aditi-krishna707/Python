n1=int(input("Entre the value of n1 :"))
n2=int(input("Entre the value of n2 :"))

operator=input("Entre operator")

match operator:
    case "+":
        print(n1+n1)
    case "-":
        print(n1-n2)
    case "*":
        print(n1*n2) 
    case "/":
        print(int(n1/n2))       
    case "_":
        print("Entre value operator")
