# Bubblesort Algorithm
# link zur Funktion https://www.geeksforgeeks.org/python-program-for-bubble-sort/

def bubbleSort(arr):
    n = len(arr)
    # durch alle array elemente iterieren
    for i in range(n-1):
        # mit range(n) würde auch funktionieren
        # doch die äußere Schleife würde einmal mehr wiederholt werden als nötig

        # letztes i ELement ist schon bekannt
        swapped = False
        for j in range(0, n-i-1):
            
            # array von 0 bis n-i-1 durchlaufen
            # wenn arr[j] größer als arr[j+1] ist, dann tauschen
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # wenn kein einziger Tausch stattgefunden hat
            # kann die Schleife abgebrochen werden
            return arr # returned nur wenn kein Tausch stattgefunden hat
    return arr # ohne return kann ich die Funktion nicht in load_data.py verwenden

''' Function to test the bubbleSort function
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")'''

