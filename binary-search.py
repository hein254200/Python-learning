nums=[2,4,6,8,10,12,14,16,18,20]
target=int(input("Enter the number you want to seaarch:"))
left = 0
right = len(nums)-1
found = False
while left<=right:
    mid = (left+right)//2
    if nums[mid]<target:
        left = mid+1
    elif nums[mid]>target:
        right=mid-1
    else:
        found = True
        print(f"found number {target} at index {mid}")
        break
if not found:
    print("the number not found!")

#binary search မှာ list တခုလုံးကို အလည်ကနေခွဲရှာတယ်။
#ရှာချင်တဲ့number က mid ထက်ကြီလား၊ကြီးရင် mid point ရွှေ့( left = mid+1)
#ငယ်လားငယ်လဲရွှေ့(right=mid-1)
#ဒီလို့နဲ့တွေ့တဲ့ထိရှာမယ်။
