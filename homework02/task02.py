"""     Если необходимо, исправьте данный код
    try {
       int d = 0;
       double catchedRes1 = intArray[8] / d;
       System.out.println("catchedRes1 = " + catchedRes1);
    } catch (ArithmeticException e) {
       System.out.println("Catching exception: " + e);
    }                                                  """

int_array = [3, 5, 6, 7, 8, 9, 10, 11, 12, 13]
try:
    d = 0
    result = int_array[8] / d
    print(f"result = {result}")
except ZeroDivisionError as z:
    print(f"Catching exception: {z}")
