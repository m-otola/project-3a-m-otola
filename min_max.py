# Omotola Anibaba
# October 13 2020
# Write a program that asks the user how many integers they would like to enter; min and max values from integers.
mini_maxi = int(input("How many integers would you like to enter?"))
print("Please enter", mini_maxi, "integers.")
small_num = 9999999999999
large_num = -99999999999
for nums in range(0, mini_maxi):
    looks = int(input())
    if looks < small_num:
        small_num = looks
    if looks > large_num:
        large_num = looks
print("min:", small_num)
print("max:", large_num)
