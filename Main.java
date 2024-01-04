import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // Ввод количества функций+проверяем, что число положительное(защита от дурака)
        System.out.println("Введите количество булевых функций:");
        Scanner sc = new Scanner(System.in);
        int n = 0;
        while (true) {
            try {
                n = Integer.parseInt(sc.nextLine());
                if (n > 0) {
                    break;
                }
            } catch (NumberFormatException e) {
                System.out.println("Введите положительное число!");
            }
        }

        // Ввод функций
        System.out.println("Введите функции в виде таблиц истинности:");
        String[] c = new String[n];
        int[] d = new int[n];
        for (int i = 0; i < n; i++) {
            c[i] = sc.nextLine();
            d[i] = c[i].length();
        }

        // Проверка принадлежности к классу самодвойственности
        boolean[] Sam = new boolean[n];
        for (int i = 0; i < n; i++) {
            Sam[i] = checkSam(c[i]);
        }

        // Проверка принадлежности к классу T0
        boolean[] T0 = new boolean[n];
        for (int i = 0; i < n; i++) {
            T0[i] = c[i].charAt(0) == '0';
        }

        // Проверка принадлежности к классу T1
        boolean[] T1 = new boolean[n];
        for (int i = 0; i < n; i++) {
            T1[i] = c[i].charAt(d[i] - 1) == '0';
        }

        // Проверка монотонности
        boolean[] M = new boolean[n];
        for (int i = 0; i < n; i++) {
            M[i] = checkMonoton(c[i], d[i]);
        }

        // Проверка линейности
        boolean[] L = new boolean[n];
        for (int i = 0; i < n; i++) {
            L[i] = checkLin(c[i], d[i]);
        }

        // Вывод результатов
        for (int i = 0; i < n; i++) {
            System.out.println("S - " + Sam[i]);
            System.out.println("T0 - " + T0[i]);
            System.out.println("T1 - " + T1[i]);
            System.out.println("M - " + M[i]);
            System.out.println("L - " + L[i]);
        }
    }

    private static boolean checkSam(String function) {
        int summ = 0;
        for (int i = function.length() / 2; i >= 0; i--) {
            if (function.charAt(i) == function.charAt(function.length() - i - 1)) {
                summ++;
            }
        }
        return summ == function.length() / 2;
    }

    private static boolean checkMonoton(String function, int d) {
        for (int i = d - 1; i > 0; i--) {
            for (int j = i + 1; j < d; j++) {
                if ((i & j) == i && function.charAt(i) > function.charAt(j)) {
                    return false;
                }
            }
        }
        return true;
    }
        private static boolean checkLin(String function, int d) {
            StringBuilder sb = new StringBuilder(function);  // Преобразование в StringBuilder
            for (int i = d - 1; i > 0; i--) {
                char temp = sb.charAt(i);
                temp += sb.charAt(i - 1);
                sb.setCharAt(i, (char) (sb.charAt(i) + sb.charAt(i - 1)));  // Изменение символов в StringBuilder
            }
            function = sb.toString();  // Преобразование обратно в строку
            for (int i = 0; i < d; i++) {
                if (function.charAt(i) > 1) {
                    return false;
                }
            }
            return true;
        }
    }


