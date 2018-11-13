

grocery_list = ["Juice", "Apples", "Potatoes"]
f = 1

for i in grocery_list:
    print( "Dont forget to buy " +  i + '!')

    ##Demo on how to look though characters in a string
for x in "diapers":
    print(x)

#Conditional loop with a if statment
desktop_app_list = ["OBS", "VMware", "Atom", "QR Generator", "Potatoe AI"]
for x in desktop_app_list:
    print(x)
    if x == "Atom":
        print("Ladies and Gents, we got it! \nThe rest of your desktop apps are:")




## function demo
def my_function():
    print("This text is coming from a function")

    #To call the fucntion just call the funchion with the parameters
my_function()

# fucntion with parameters Demo
def function_with_params(name):
    print("Hello, my name is " + name + " and I am a fucntion")

#Calling paramatized function
function_with_params("Bob")
