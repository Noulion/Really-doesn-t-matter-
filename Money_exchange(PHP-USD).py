import time

print("dollars to pesos 🤑🤑🔥 \n") # just title 🤑

while True:
    #input if you only have dollars 💰 💰 
    usa = input("dollars: ")
    pesos = 'pesos: '

    if usa == '' :
        print("\n")
        continue 
        

    if usa == usa:
        
        peso = 58.6995 #this value changes cuz of inflation or deflation 
        total = peso * float(usa) #ez math and float is nicer than int(). Cuz in int(), it gives long numbers 
    
        print(f'calculating how much is {usa}$ in pesos🤑 ')
        time.sleep(1.2)
        
        print(pesos, total, '₱', '\n')
        
        #if u got no money then get the fuck outta here
        if total <= 0:
            print("persona: bankrupt🏦👎")
            print('broke ass shit, no more loop for u')
            time.sleep(0.4)
            break
        
        #if u got money then give me 1000php = 20 dollars    
        elif total >= 1000:
            print("persona: rich🤑🚽")
            print("continue your loop rich man! \n")
