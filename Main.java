import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine(); // введенная строка
        int n = sc.nextInt(); // введенная степень
        int len = str.length(); // длина строки
        int index1 = 1; // индекс 1-ой переменной
        int index2; // индекс 2-ой переменной

        // для комплексных чисел
        String complex = "i";

        for (int p = 0; p < len - 3; p++) { // нахождение индекса 1-ой переменной

            boolean letter = Character.isLetter(str.charAt(p));
            if (letter) {
                index1 = p;
            }
        }

        for (int p = index1 + 4; p < len - 1; p++) { // нахождение индекса 2-ой переменной

            boolean letter = Character.isLetter(str.charAt(p)); // проверка на букву

            if (letter) {

                index2 = p; // индекс 2-ой переменной

                boolean letter1 = Character.isLetter(str.charAt(len - 2));
                boolean letter2 = Character.isLetter(str.charAt(len - 3));

                if (letter1 && letter2) { // если следующий за 2-ой переменной символ тоже буква

                    if (str.substring(index2, index2 + 1).equals(complex)) { // если "i" - буква перед 2-ой переменной, то число комплексное

                        String x = str.substring(1, index1);
                        String y = str.substring(index1 + 4, index2);
                        String a = str.substring(index1, index1 + 1);
                        String w = str.substring(index2, index2 + 1); // i
                        String b = str.substring(index2 + 1, index2 + 2);

                        // если коэффициенты единицы
                        if (x.isEmpty()) {
                            x = "1";
                        }
                        if (y.isEmpty()) {
                            y = "1";
                        }

                        // перевод строки в число (коэффициенты перед переменными)
                        double f = Double.parseDouble(x);
                        double l = Double.parseDouble(y);

                        // если одинаковые переменные
                        if (a.equals(b)) {
                            System.out.println(Math.pow((f + l), n) + w + a.repeat(n));
                        }

                        int res1 = 1, i; // факториал n
                        for (i = 2; i <= n; i++)
                            res1 *= i;

                        for (int k = 0; k <= n; k++) {

                            int t = n-k; // счетчик степени a (k - cчетчик степени b)
                            double t1 = n-k; // для возведения в степень

                            double r = Math.pow(f, t1); // коэффициент перед a
                            double s = Math.pow(l, k); // коэффициент перед b

                            int res2 = 1, i1;// факториал k
                            int res3 = 1, i2;// факториал n-k

                            for (i1 = 2; i1 <= k; i1++)
                                res2 *= i1;
                            for (i2 = 2; i2 <= (n-k); i2++)
                                res3 *= i2;
                            int c =  res1/(res2 * res3); // вектор

                            if (k != n) { // для всех членов бинома, кроме последнего
                                if (k != 0) { // для всех элементов бинома, кроме первого
                                if (k % 2 != 0) { // b в нечетной степени
                                    System.out.print(c*r*s + w + a.repeat(t) + b.repeat(k) + " - ");
                                }
                                else { // b в четной степени
                                System.out.print(c*r*s + a.repeat(t) + b.repeat(k) + " + ");
                            }}
                                else { // для первого элемента бинома
                                    System.out.print(c*r*s + a.repeat(t) + " + ");
                                }
                                }
                            else { // для последнего элемента бинома
                                if (k % 2 != 0) { // если степень b нечетная
                                    System.out.print(c*r*s + w + b.repeat(k));
                                }
                                else { // если степень b четная
                                    System.out.print(c*r*s + b.repeat(k));
                                }
                            }
                        }
                    }
                }
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                else { // если число не комплексное

                    String x = str.substring(1, index1);
                    String y = str.substring(index1 + 4, index2);
                    String a = str.substring(index1, index1 + 1);
                    String b = str.substring(index2, index2 + 1);


                    if (x.isEmpty()) {
                        x = "1";
                    }
                    if (y.isEmpty()) {
                        y = "1";
                    }

                    double f = Double.parseDouble(x);
                    double l = Double.parseDouble(y);

                    // если одинаковые переменные
                    if (a.equals(b)) {
                        System.out.println(Math.pow((f + l), n) + a.repeat(n));
                    }

                    int res1 = 1, i; // факториал n
                    for (i = 2; i <= n; i++)
                        res1 *= i;

                    for (int k = 0; k <= n; k++) {

                        int t = n-k; // счетчик степени a (k - cчетчик степени b)
                        double t1 = n-k;

                        double r = Math.pow(f, t1); // коэффициент перед a
                        double s = Math.pow(l, k); // коэффициент перед b

                        int res2 = 1, i1;// факториал k
                        int res3 = 1, i2;// факториал n-k

                        for (i1 = 2; i1 <= k; i1++)
                            res2 *= i1;
                        for (i2 = 2; i2 <= (n-k); i2++)
                            res3 *= i2;

                        int c =  res1/(res2 * res3); // вектор

                        if (k != n) { // для всех элементов бинома, кроме последнего
                            System.out.print(c*r*s + a.repeat(t) + b.repeat(k) + " + ");
                        }
                        else { // для последнего элемента бинома
                            System.out.print(c*r*s + a.repeat(t) + b.repeat(k));
                        }
                    }
                }
            }
        }
    }
}
