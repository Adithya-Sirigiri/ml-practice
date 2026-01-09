alphabet="abcdefghijklmnopqrstuvwxyz"
result=""
initial_mess=input("Please enter \"encrypt\" for encryption and \" decrypt\" for decryption of the message:")
if(initial_mess=="encrypt"):
    info=input("Type your message to be encrypted:")
    num=int(input("How many characters you want to shift:"))
    infos=info.lower()
    for i in infos:
        if i in alphabet:
            new=alphabet.index(i)
            final=(new+num)%26
            result+=alphabet[final]
        else:
            result+=i
    print("The encrypted message is:",result)
    nor=input("Type yes if you want to decrypt the message:")
    if(nor=="yes"):
        for i in infos:
         if i in alphabet:
            new=alphabet.index(i)
            final_1=(new-num)%26
            if(final_1<=0):
               final_1+=26
               result+=alphabet[final_1]
            else:
               result+=alphabet[final_1]
         else:
            result+=i
        else:
           print("The dencrypted message is:",result)
   