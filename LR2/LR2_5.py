class my_range():
    
    STEP = 1
    
    def __init__(self, first, last = 0, step = STEP):
        if last == 0:
            self.last = first
            self.first = 0
            self.step = step 
        else:
            self.first = first
            self.last = last
            self.step = step 
            
        
    def new_range(self, func = 1):
        a = []
        f = self.first
        while f < self.last:
            a.append(f)
            f += self.step
        if func != 1:
            b = []
            for elem in a:
                if func(elem):
                    b.append(elem)
        else:
            b = a
        return b
        
        
def even_q(num):
    if num % 2 == 0:
        return True
    else:
        return False
    

if __name__ == '__main__':
    test = my_range(15, 30)
    print(test.new_range(even_q))

