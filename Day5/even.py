target = int(input())
if target>1000:
    print("Total too high")
else:
    total = 0
    for num in range(2,target+1,2):
        total+=num
    print(f"The total of even number from 0 to {target}: {total}")