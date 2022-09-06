def isPerfectSquare(n) :
 
    i = 1
    while(i * i<= n):
         
        
        if ((n % i == 0) and (n / i == i)):
            return True
             
        i = i + 1
    return False
 

if __name__ == "__main__" :
 
    n = 5
    if (isPerfectSquare(n)):
        print("Yes, it is a perfect square.")
    elif n == 0:
        print("Yes, it is a perfect square.")
    else :
        print("No, it is not a perfect square.")
 
