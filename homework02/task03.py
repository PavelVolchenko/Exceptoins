"""     Дан следующий код, исправьте его там, где требуется.
public static void main(String[] args) throws Exception {
   try {
       int a = 90;
       int b = 3;
       System.out.println(a / b);
       printSum(23, 234);
       int[] abc = { 1, 2 };
       abc[3] = 9;
   } catch (Throwable ex) {
       System.out.println("Что-то пошло не так...");
   } catch (NullPointerException ex) {
       System.out.println("Указатель не может указывать на null!");
   } catch (IndexOutOfBoundsException ex) {
       System.out.println("Массив выходит за пределы своего размера!");
   }
}
public static void printSum(Integer a, Integer b) throws FileNotFoundException {
   System.out.println(a + b);
}
        Программа должна выбрасывать Exception, когда пользователь вводит пустую строку.
        Пользователю должно показаться сообщение, что пустые строки вводить нельзя.             """

try:
    a = 90
    b = 3
    if input("Enter -> ") == "":
        raise ValueError
    print(a / b)
    print_sum(23, 234)
    abc = [1, 2]
    abc[3] = 9
except NameError as n:
    print(f"Функция {n.name} не найдена!")
except IndexError:
    print("Массив выходит за пределы своего размера!")
except ValueError:
    print("Пустые строки вводить нельзя!")
except Exception:
    print("Что-то пошло не так...")


