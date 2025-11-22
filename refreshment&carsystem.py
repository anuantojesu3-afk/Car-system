import time
print("Welcome to our website of BMW's Pros & Cons")
time.sleep(1.5)
print("BMW Models In Stock = M8,i7,X4,X3 M,i4")
a=(input("Enter a BMW Car "))
if(a=="M8"):
 print("2025 Model M8, Price = $138,000")
if(a=="i7"):
 print("2025 Model i7, Price = $105,700")
if(a=="X4"):
 print("2025 Model X4, Price = $55,300")
if(a=="X3 M"):
 print("2024 Model X3 M, Price = $75,500")
if(a=="i4"):
 print("2024 Model i4, Price = $57,300")
b=(input("Choose Payment Option [Credit Card,Cash,Loan] "))
if(b!="Loan"):
 print(b + " Chosen, Initializing...")
 time.sleep(1.5)
 print("Bill: "
+a + " Vehicle "
+b +" Payment")
if(b=="Loan"):
 print(b + " Chosen, Initializing...")
 Info=(input("Duration Of Loan "))
 print(Info + " Inputed, Initializing...")
 time.sleep(1.5)
 print("Loan Bill: "
+a + " Vehicle ")
InfoSecond=(input("Enter Address , Name , Phone Number "))
Refreshment=(input("Enter Refreshments[Drinks] "))
if(Refreshment!=""):
 print(Refreshment + " , Arriving In 5 Minutes...")
 time.sleep(1.5)
if(a!="" and b!="" and Refreshment!=""):
 print("Final Bill, Initalising...")
 time.sleep(1.5)
 print("Final Bill:")
 print(a)
 print(b)
 print(InfoSecond)
 print(Refreshment)