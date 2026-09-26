import os
from datetime import datetime

# this function just makes sure user enters a number
def get_int(text):
    while True:
        n = input(text)
        if n.isdigit():
            return int(n)
        else:
            print("Enter proper number please")

# same for float
def get_float(text):
    while True:
        try:
            x = float(input(text))
            if x >= 0:
                return x
            else:
                print("Amount can't be negative")
        except:
            print("Invalid amount")

# main program starts here
def main():

    print("====== SHOP BILLING ======")

    item_count = get_int("How many items? : ")

    if item_count == 0:
        print("Nothing to bill.")
        return

    names = []
    qty = []
    price = []
    totals = []

    # taking item details
    for i in range(item_count):
        print("\nItem", i+1)
        n = input("Name: ").strip()
        if n == "":
            n = "Item_" + str(i+1)

        q = get_int("Qty: ")
        p = get_float("Price: ")

        names.append(n)
        qty.append(q)
        price.append(p)
        totals.append(q * p)

    # printing bill
    print("\n------- BILL -------")
    print("Name            Qty   Price   Total")

    grand = 0

    for i in range(item_count):
        print(names[i].ljust(15), qty[i], "  ", price[i], "   ", totals[i])
        grand += totals[i]

    print("--------------------")
    print("Grand Total =", grand)
    print("--------------------")

    # saving bill
    folder = "bills"
    os.makedirs(folder, exist_ok=True)

    filename = "bill_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    fullpath = os.path.join(folder, filename)

    f = open(fullpath, "w", encoding="utf-8")
    f.write("BILL RECEIPT\n")
    f.write("Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
    f.write("Name            Qty   Price   Total\n")

    for i in range(item_count):
        f.write(names[i].ljust(15) + str(qty[i]) + "   " +
                str(price[i]) + "   " + str(totals[i]) + "\n")

    f.write("\nGrand Total = " + str(grand))
    f.close()

    print("Bill saved:", filename)

if __name__ == "__main__":
    main()
