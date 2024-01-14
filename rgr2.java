import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class rgr2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите выражение вида (ax+by): ");
        String input = scanner.nextLine();

        System.out.print("Введите степень n: ");
        int n = scanner.nextInt();

        if (input.startsWith("-") && (n % 2) != 0) {
            System.out.print("-");
        }

        List<String> letters = new ArrayList<>();
        StringBuilder charStr = new StringBuilder();

        for (char x : input.toCharArray()) {
            if (Character.isLetter(x)) {
                charStr.append(x);
            } else {
                if (!charStr.isEmpty()) {
                    letters.add(charStr.toString());
                    charStr = new StringBuilder();
                }
            }
        }

        if (!charStr.isEmpty()) {
            letters.add(charStr.toString());
        }


        List<Double> integers = new ArrayList<>();
        StringBuilder num = new StringBuilder();

        for (char c : input.toCharArray()) {
            if (Character.isDigit(c) || (c == '.')) {
                num.append(c);
            } else if (!num.isEmpty()) {
                integers.add(Double.parseDouble(num.toString()));
                num = new StringBuilder();
            }
        }

        if (!num.isEmpty()) {
            integers.add(Double.parseDouble(num.toString()));
        }

        int k = 0;

        if (!letters.get(0).equals(letters.get(1))) {
            for (int i = 0; i < integers.size(); i++) {
                double a = integers.get(0);
                double b = integers.get(1);

                while (k <= n) {
                    System.out.print(IntFloat (n, k, a, b) + pow(n, k, letters));
                    k++;

                    if (k <= n) {
                        if (input.chars().filter(ch -> ch == '-').count() == 2 && (n % 2) != 0) {
                            System.out.print(" - ");
                        } else if (input.chars().filter(ch -> ch == '-').count() == 2 && (n % 2) == 0) {
                            System.out.print(" + ");
                        } else if (input.startsWith("-") && (n % 2) != 0) {
                            char operation = "-+".charAt(k % 2);
                            System.out.print(" " + operation + " ");
                        } else if (input.startsWith("-") && (n % 2) == 0) {
                            char operation = "+-".charAt(k % 2);
                            System.out.print(" " + operation + " ");
                        } else if (input.contains("-")) {
                            char operation = "+-".charAt(k % 2);
                            System.out.print(" " + operation + " ");
                        } else {
                            System.out.print(" + ");
                        }
                    }
                }
            }
        } else {
            System.out.print(overlap (n, letters, integers));
        }
    }

    public static int factorial (int m) {
        if (m == 0 || m == 1) {
            return 1;
        } else {
            return m * factorial(m - 1);
        }
    }

    public static int ratio (int n, int k) {
        int x = factorial(n);
        int y = factorial(k);
        int c = factorial(n - k);
        return x / (y * c);
    }

    public static Number IntFloat (int n, int k, double a, double b) {
        double num = ratio(n, k) * Math.pow(a, n - k) * Math.pow(b, k);
        if (num % 1 == 0) {
            return (int) num;
        } else {
            return num;
        }
    }

    public static String pow (int n, int k, List<String> letters) {
        String letter1 = String.valueOf(letters.get(0)).repeat(n - k);
        String letter2 = String.valueOf(letters.get(1)).repeat(k);
        return letter1 + letter2;
    }

    public static String overlap (int n, List<String> letters, List<Double> integers) {
        String letter = String.valueOf(letters.get(0)).repeat(n);
        double integer = Math.pow(integers.get(0) + integers.get(1), n);
        return integer + letter;
    }
}