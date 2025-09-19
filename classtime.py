x='Python'
def my():
    x='C'
    print("I like "+x)
my()
print('I like '+x)

x='Python'
def my():
    global x
    x='C'
    print("I like "+x)
my()
print('I like '+x)
c=0
for i in range(3):
    for j in range(2):
        for k in range(10):
            # print(i,j,k)
            c+=1
print(c)

evens=[]
for i in range(1,21):
    if i%2==0:
        evens.append(i)
print(evens)

# using list comprehension
evens=[n for n in range(1,21) if n%2==0]
print(evens)

import os

# Path to advisory modules
ADVISORY_DIR = "advisory_modules"

def list_modules():
    print("\nAvailable Advisory Modules:")
    for file in os.listdir(ADVISORY_DIR):
        if file.endswith(".txt"):
            print(f"- {file.replace('_', ' ').replace('.txt', '').title()}")

def load_advisory(module_name):
    file_path = os.path.join(ADVISORY_DIR, f"{module_name}.txt")
    if not os.path.exists(file_path):
        print("❌ Module not found. Please check the name and try again.")
        return
    with open(file_path, "r", encoding="utf-8") as f:
        print("\n📢 Advisory Content:\n")
        print(f.read())

def main():
    print("🌾 Welcome to Krishi Vani CLI Assistant 🌾")
    while True:
        print("\nWhat would you like to do?")
        print("1. List available modules")
        print("2. Load advisory")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            list_modules()
        elif choice == "2":
            module_name = input("Enter module name (e.g., wheat_advisory): ").strip()
            load_advisory(module_name)
        elif choice == "3":
            print("🙏 Thank you for using Krishi Vani. Stay empowered!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#using for loop
mylist=['any','am','ivy','airy','a']
newlist=[]
for i in mylist:
    if i.startswith('a') and i.endswith('y'):
        newlist.append(i)
print(newlist)

#list comprehension
mylist=['any','am','ivy','airy','a']
newlist=[x for x in mylist if x.startswith('a') and x.endswith('y')]
print(newlist) 
print(newlist)
mylist=['a','b','c','d']
print(mylist[-2:0:-1])
