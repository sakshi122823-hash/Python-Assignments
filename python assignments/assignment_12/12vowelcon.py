def check_vowel(str):
    if str == ( "a" , "e" , "i" ,"o","u" , "A" , "I" , "O", "U","E"):
        print("it is vowel")
    else:
        print("it is consonent")


alphabet=str(input("enter the alphabet  : "))
if __name__=="__main__":
    check_vowel(alphabet)