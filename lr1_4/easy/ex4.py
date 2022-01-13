tvshow = ["Show 1", "Show 2", "Show 3", "Show 4"]

print("Here are our shows:")
for show in tvshow:
    print('-', show)

new_show = input("Enter new show: ")

correct_index = True
while correct_index:
    position = int(input("Enter position for the show: "))
    if position < 1 or position > len(tvshow)+1:
        print("You must enter position between 1 and", len(tvshow)+1)
    else:
        correct_index = False

tvshow.insert(position-1, new_show)
print("Here are our new shows:")
for show in tvshow:
    print('-', show)