for i in range(99, 0, -1):
#حلقةالتكرار من الرقم 99 و 0 م بيتعد معانا و -1 علشان يعد تنازلى
    if i == 1:
        current_number = "1 bottle"
    else:
        current_number = f"{i} bottles"
 #هناحددت صيغة العددلو 1 يبقى bottle لو اكتر من 1 يبقى bottles       
    if i - 1 == 1:
        next_number = "1 bottle"
    elif i - 1 == 0:
        next_number = "no more bottles"
    else:
        next_number = f"{i - 1} bottles"
#هنا حددت صيغة العدد التالى لو 1 يبقى bottle لو 0 يبقى no more bottles لو اكتر من 1 يبقى bottles
    print(f"{current_number} of water on the wall, {current_number} of water.")
    print(f"Take one down and pass it around, {next_number} of water on the wall.\n")   
    print("No more bottles of water on the wall, no more bottles of water.")
print("Go to the store and buy some more, 99 bottles of water on the wall.") 

        
        
        

