
# define function for all
def autonomous_copy_machine() :

    print("Welcome to Our Service : Autonomous Copy Machine")

    # 01. given input "Amout of copy"
    n_copy = int(input("please input amout of copy : ")  )
    

    # 02. check condition for amout of copy
    if (n_copy >= 1) and (n_copy <10) :
        price = 3 * n_copy

    elif n_copy <100 :
        price = 2 * n_copy

    elif n_copy >= 100 :
        price = 1 * n_copy

    else : 
        print("Incorrect input please try again")

    # 03. input amout of paid
    customer_paid =  int(input("please input money paid : ")  )

    # 04. Give a change in a banknote & coins 
    change = customer_paid - price

    # formula for change

    ## banknote : 500 THB / 100 THB
    ## coin : 10 THB / 5 THB / 1 THB

    n_note_500 = change // 500  # ได้เงินทอนเป็นแบ๊ง 500 กี่ใบ
    change_below_500 = change % 500  # เงินทอนส่วนที่เหลือจากแบ๊ง 500 มีกี่บาท

    n_note_100 = change_below_500 // 100 # ได้เงินทอนเป็นแบ๊ง 100 กี่ใบ
    change_below_100 = change_below_500  % 100   # เงินทอนส่วนที่เหลือจากแบ๊ง 100 มีกี่บาท

    n_coin_10 = change_below_100 // 10  # ได้เงินทอนเป็นเหรียญ 10 กี่เหรียญ
    change_below_10 =  change_below_100 % 10  # เงินทอนส่วนที่เหลือจากเหรียญ 10 มีกี่บาท

    n_coin_05 = change_below_10 // 5  # ได้เงินทอนเป็นเหรียญ 5 กี่เหรียญ
    change_below_05 =  change_below_10 % 5  # เงินทอนส่วนที่เหลือจากเหรียญ 5 มีกี่บาท

    n_coin_01 = change_below_05 // 1  # ได้เงินทอนเป็นเหรียญ 1 กี่เหรียญ
    change_below_01 =  change_below_05 % 1  # เงินทอนส่วนที่เหลือจากเหรียญ 1 มีกี่บาท

    if change < 0 :
        print(f"Insufficient payment / please pay more   {  abs(change) } THB ")

    elif change == 0 :
        print("Thank you very much , see you next time")

    else :
        print("******************************************")
        print(f"your total amount will be : {price} THB ")
        print(f"your Payment is           : {customer_paid} THB")
        print("******************************************")
        print(f"you will be given a change for {change} THB as detail below")
        print("-------------------------------------------")
        print(f"Bank note - 500 THB  :  {n_note_500} Notes")
        print(f"Bank note - 100 THB  :  {n_note_100} Notes")
        print(f"Coin      -  10 THB  :  {n_coin_10} coins")
        print(f"Coin      -   5 THB  :  {n_coin_05} coins")
        print(f"Coin      -   1 THB  :  {n_coin_01} coins")
        print("-------------------------------------------")
        print("Thank you very much , see you next time")
        print("-------------------------------------------")


# try to call function we've just created

autonomous_copy_machine()
   