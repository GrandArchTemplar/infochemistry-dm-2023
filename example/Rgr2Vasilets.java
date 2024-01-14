import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Rgr2Vasilets {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Введите выражение в формате (ax + by), где\n" + "a и b произвольные целые или вещественные числа,\n" +
                "x и y — произвольные буквы латинского алфавита:");
        String expression = scanner.nextLine();

        System.out.println("Введите целую положительную степень n:");
        int n = scanner.nextInt();

        Pattern pattern = Pattern.compile("\\((-?\\d+(\\.\\d+)?)([a-z]) \\+ (-?\\d+(\\.\\d+)?)([a-z])\\)");
        Matcher matcher = pattern.matcher(expression);

        if (matcher.find()) {
            double x = Double.parseDouble(matcher.group(1));
            String a = matcher.group(3);
            double y = Double.parseDouble(matcher.group(4));
            String b = matcher.group(6);

            String solution = a.equals(b) ? sameSymbol(x + y, n, a) : calcSolution(x, y, n, a, b);
            System.out.println("Разложение: " + solution);
        } else {
            System.out.println("Неправильный формат выражения.");
        }
    }


     static String sameSymbol(double value, int n, String symbol) {
        double coefficient = Math.pow(value, n);
        return coefficient + outputSymbols(symbol, n);
    }

     static String calcSolution(double x, double y, int n, String a, String b) {
        StringBuilder result = new StringBuilder();

        for (int k = 0; k <= n; k++) {
            double coefficient = calcCoef(n, k) * Math.pow(x, n - k) * Math.pow(y, k);

            if (k > 0 && coefficient > 0) {
                result.append(" +");
            }

            if (coefficient != 0) {
                if (coefficient != 1) {
                    result.append(" " + outputCoef(coefficient));
                }
                result.append(outputSymbols(a, n - k)).append(outputSymbols(b, k));
            }
        }

        return result.toString();
    }

     static double calcCoef(int n, int k) {
        double result = 1;
        for (int i = 1; i <= k; i++) {
            result *= (n - (k - i)) / (double) i;
        }
        return result;
    }


    static String outputCoef (double coefficient) {
        if (coefficient == (long) coefficient) {
            return String.format("%d", (long) coefficient);
        } else {
            return Double.toString(coefficient);
        }
    }


     static String outputSymbols(String symbol, int n) {
        return new String(new char[n]).replace("\0", symbol);
    }

}
