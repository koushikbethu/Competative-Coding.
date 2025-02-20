class MinStack:
    def __init__(self,capacity):
        self.stack=[]
        self.min_stack=[]
        self.capacity=capacity
    
    def is_full(self):
        return len(self.stack) >= self.capacity
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self,value):
        if self.is_full():
            print("OverFlow : Stack is full")
            return
        self.stack.append(value)
    #not self.min_stack: If the min_stack is empty, we must push the value as the first minimum.
    #value <= self.min_stack[-1]: If the new value is less than or equal to the current minimum (min_stack[-1]), we push it onto min_stack. This ensures that the smallest values are always stored on top.
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        print(f"Pushed : {value}")
        
    def pop(self):
        if self.is_empty():
            print("Underflow : Stack is Empty")
            return None
        value=self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        print(f"Popped : {value}")
        
    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[-1]
    
    def get_min(self):
        if self.is_empty():
            print("Stack  is Empty")
            return None
        return self.min_stack[-1]
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        print("Stack Contents :",self.stack)
        
if __name__=="__main__":
    N=int(input("Enter the Capacity of the stack:"))
    min_stack=MinStack(N)
    
    while True:
        print("\n1.Push\n2.Pop\n3.Top\n4.Get Min\n5.Display\n6.Exit")
        choice = int(input("Enter Your Choice:"))
        
        if choice == 1:
            value = int(input("Enter the value to Push: "))
            min_stack.push(value)
        elif choice ==2:
            min_stack.pop()
        elif choice ==3:
            print("Top element is :",min_stack.top())
        elif choice ==4:
            print("Minimu element is :",min_stack.get_min())
        elif choice ==5:
            min_stack.display()
        elif choice ==6:
            break
        else:
            print("Invalid choice . Please try again....") 
