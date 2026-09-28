#lab5:task5.1


counter = 0
def show_local():
    counter = 10
    print("Local counter:", counter)
show_local()
print("Global counter:", counter)


#output:
#Local counter: 10
#Global counter: 0
