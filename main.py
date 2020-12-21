import world
import vietnam
import finland
import uk

choice = int(input("1. World\n2. Vietnam\n3. Finland\n4. England\n\nYour choice: "))
print()
if choice == 1:
    world.world()
elif choice == 2:
    vietnam.vietnam()
elif choice == 3:
    finland.finland()
elif choice == 4:
    uk.uk()
else:
    print("Run the program again and choose from 1 to 3.")