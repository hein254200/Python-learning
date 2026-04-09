nums =[2,3,5,8,9,1]
target = int(input("Enter the number you want to search:"))
found = False
for i in range(len(nums)):
   if nums[i] == target:
      print(f"Number {target} found at index {i}.")
      found = True
      break
if found == False:
    print("your number not fond.")
        
#ဒီမှာရေးထားတာ found = False ဆိုတာက မတွေ့သေးဘူးဆိုတာနဲ့စပေးလိုက်တယ်။
#for loop နဲ့ပတ်မယ် တခုချင်းတိုက်စစ်မယ်။ 
#တကယ်လို့တွေ့ခဲ့ရင် True ပေးပြီး break လိုက်မယ်
#တကယ်လို့ ္False ပေးလာရင် not found ထုတ်ပေးမယ်။
#သူကcondition နဲ့ဆုံးဖြတ်ခိုင်းရင်တခုချင်းစီလိုက်ပြီးprint နေမယ်
#ခုက True False နဲ့ဆုံးဖြတ်ပြီးတော့မှပဲprint ပေးလိုက်တယ်။