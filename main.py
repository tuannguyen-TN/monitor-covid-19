import world
import vietnam
import finland
import uk
import swiss

if __name__ == "__main__":
    choice = int(input("1. World\n2. Vietnam\n3. Finland\n4. UK\n5. Switzerland\n6. All\n\nYour choice: "))
    print()
    if choice == 1:
        world.world()
    elif choice == 2:
        vietnam.vietnam()
    elif choice == 3:
        finland.finland()
    elif choice == 4:
        uk.uk()
    elif choice == 5:
        swiss.swiss()
    elif choice == 6:
        print("World:")
        world.world()
        print()
        print("Vietnam:")
        vietnam.vietnam()
        print()
        print("Finland:")
        finland.finland()
        print()
        print("UK:")
        uk.uk()
        print()
        print("Switzerland:")
        swiss.swiss()
        print()
    else:
        print("Run the program again and choose from 1 to 3.")