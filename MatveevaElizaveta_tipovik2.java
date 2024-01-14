import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    private static String variable(double base, int n, String symbol) {
        double coefficient = Math.pow(base, n);
        return coefficient + repeat(symbol, n);
    }
    private static String binomial(double x, double y, int n, String a, String b) {
        StringBuilder expression = new StringBuilder();

        for (int k = 0; k <= n; k++) {
            double coefficient = binomialCoefficient(n, k) * Math.pow(x, n - k) * Math.pow(y, k);

            if (k > 0 && coefficient > 0) {
                expression.append(" + ");
            }

            if (coefficient != 0) {
                if (coefficient != 1) {
                    expression.append(coefficient);
                }
                expression.append(repeat(a, n - k)).append(repeat(b, k));
            }
        }
        return expression.toString();
    }
    private static double binomialCoefficient(int n, int k) {
        double result = 1;
        for (int i = 1; i <= k; i++) {
            result *= (n - (k - i)) / (double) i;
        }
        return result;
    }
    private static String repeat(String symbol, int times) {
        return new String(new char[times]).replace("\0", symbol);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите выражение в формате (ax + by):");
        String expression = scanner.nextLine();
        System.out.println("Введите степень n:");
        int valueN = scanner.nextInt();
        Pattern pattern = Pattern.compile("\\((-?\\d+(\\.\\d+)?)([a-z]) \\+ (-?\\d+(\\.\\d+)?)([a-z])\\)");
        Matcher matcher = pattern.matcher(expression);

        if (matcher.find()) {
            double valueX = Double.parseDouble(matcher.group(1));
            String x = matcher.group(3);
            double valueY = Double.parseDouble(matcher.group(4));
            String y = matcher.group(6);

            String expressionEnd = x.equals(y) ? variable(valueX + valueY, valueN, x) : binomial(valueX, valueY, valueN, x, y);
            System.out.println("Разложение: " + expressionEnd);
        } else {
            System.out.println("Неправильный формат выражения.");
        }
    }
}