import world
import vietnam
import finland

choice = int(input("1. World\n2. Vietnam\n3. Finland\n\n"))
print()
if choice == 1:
    world.world()
elif choice == 2:
    vietnam.vietnam()
elif choice == 3:
    finland.finland()
else:
    print("Run the program again and choose from 1 to 3.")