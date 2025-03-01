is_tampan = input("Apakah kamu tampan? (y/n)")
is_kaya = input("Apakah kamu kaya? (y/n)")
is_pintar   = input("Apakah kamu pintar? (y/n)")
is_setia = input("Apakah kamu setia? (y/n)")
is_sholeh = input("Apakah kamu sholeh? (y/n)")
jumlahy =0

if (is_tampan == "y" or is_tampan == "y") :
    jumlahy += 1
    
if (is_kaya == "y" or is_kaya == "y") :
    jumlahy += 1
    
if (is_pintar == "y" or is_pintar == "y") :
    jumlahy += 1
    
if (is_setia == "y" or is_setia == "y") :
    jumlahy += 1
    
if (is_sholeh == "y" or is_sholeh == "y") :
    jumlahy += 1
    
if jumlahy >=3 :
    print ("anda lolos")
if jumlahy <= 2:
    print("kamu tidak")