with open("example.txt", 'w') as f:
    f.write("python is easy")
with open("example.txt", 'r') as f:  
    print(len(f.read().split()))

def count_words(filename):
    try:
        with open("example.txt", 'r') as f:
            return len(f.read().split())
    except FileNotFoundError:
        return "File doesnt exist"
print(f"count: {count_words('example.txt')}")  

with open("example.txt", 'r') as f:  
    data = f.read().upper()
with  open("example.txt", 'w') as f1: 
    f1.write(data)   
#OR     
with open("example.txt", 'r') as f, open("example.txt", 'w') as f1: 
    data = f.read().upper()   
    f1.write(data) 
with open ("test.txt", 'w')  as source:
    source.write("alice, 85\n Bob, 50\n charlie, 60")  
     