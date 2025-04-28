num1=float(input("ingresa el primer numero: "))
num2=float(input("ingresa el segundo numero: "))
operacion=input("seleccione la operacion(+,-,*,/):")
if operacion =='+':
    resultado=num1+num2
    print(f"resultado:{resultado:.2f}")
elif operacion =='-':
    resultado=num1-num2
    print(f"resultado:{resultado:.2f}")
elif operacion =='*':
    resultado=num1*num2
    print(F"resultado:{resultado:.2f}")
elif operacion =='/':
    if num2 !=0:
        resultado=num1/num2
        print(f"resultado:{resultado:.2f}")
    else:
        print("error:no se puede dividir entre cero")
else:
    print("operacion no valida")