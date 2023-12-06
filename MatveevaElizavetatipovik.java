import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static boolean FT0 = false;
    static boolean FT1 = false;
    static boolean FTM = false;
    static boolean FTS = false;
    static boolean FTL = false;

    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);

        System.out.println("Введите количество функций:");
        int num = console.nextInt();
        if (num <= 0){
            System.out.println("Количество функций должно быть > 0");
            return;
        }
        for (int f =1; f <= num; f++) {
            System.out.print("Введите количество переменных для функции №" + f + ": ");
            int numVariables = console.nextInt();

            if (numVariables <= 0) {
                System.out.println("Количество переменных должно быть > 0");
                return;
            }
            System.out.println("\nВведите значения булевой функции №" + f + " для каждого набора переменных:");

            ArrayList<Integer> function_values = new ArrayList<>();

            readFunctionValues(console, numVariables, function_values);


            T0(function_values);
            T1(function_values);
            TS(function_values);
            TM(function_values);
            TL(function_values);
        }
        FunctionalSet();
    }
    private static void readFunctionValues(Scanner console, int numVariables, ArrayList<Integer> function_values) {
        int value;
        int a = 1 << numVariables;
        for (int i = 0; i < a; i++) {
            System.out.print("Функция для " + String.format("%0" + numVariables + "d", Integer.parseInt(Integer.toBinaryString(i))) + ":");
            if (console.nextInt() != 0) {
                value = 1;
            } else {
                value = 0;
            }
            function_values.add(value);
        }
        System.out.println(function_values);
    }

    private static void T0(ArrayList<Integer> function_values) {
        int t0 = function_values.get(0);
        if (t0 == 0) {
            System.out.println("Функция принадлежит классу Т0");
        } else {
            System.out.println("Функция не принадлежит классу Т0");
            FT0 = true;

        }
    }


    private static void T1(ArrayList<Integer> function_values) {
        int t1 = function_values.get(function_values.size() - 1);
        if (t1 == 1) {
            System.out.println("Функция принадлежит классу Т1");
        } else {
            System.out.println("Функция не принадлежит классу Т1");
            FT1 = true;
        }
    }

    private static void TS(ArrayList<Integer> function_values) {
        for (int i = 0; i < function_values.size(); i++) {
            int tS1 = function_values.get(function_values.size() - 1 - i);
            int tS2 = function_values.get(i);
            if (tS1 == tS2) {
                System.out.println("Функция не принадлежит классу TS");
                FTS = true;
                return;
            }
        }
        System.out.println("Функция принадлежит классу TS");

    }

    private static void TM(ArrayList<Integer> function_values) {
        for (int i = 0; i < function_values.size(); i++) {
            for (int j = 0; j < function_values.size(); j++) {
                if (i <= j) {
                    int TM1 = function_values.get(i);
                    int TM2 = function_values.get(j);
                    if (TM1 > TM2) {
                        System.out.println("Функция не принадлежит классу TM");
                        FTM = true;
                        return;
                    }
                }
            }
        }
        System.out.println("Функция принадлежит классу ТM");

    }

    private static void TL(ArrayList<Integer> function_values){
        ArrayList<ArrayList<Integer>> pascal = new ArrayList<>();
        ArrayList<Integer> triangle = new ArrayList<>();

        pascal.add(function_values);
        int l = function_values.size();
        for (int i = 0; i < l-1; i++){
            ArrayList<Integer> line = new ArrayList<>();
            for (int j = 1; j < l-i; j++){
                int result = (pascal.get(i).get(j) ^ pascal.get(i).get(j-1));
                line.add(result);
            }
            pascal.add(line);
        }

        ArrayList<Integer> lastValues = new ArrayList<>();

        for (ArrayList<Integer> line : pascal) {
            int lastValue = line.get(line.size() - 1);
            lastValues.add(lastValue);
        }

        ArrayList<Integer> index = new ArrayList<>();
        for (int i = 0; i < lastValues.size(); i++) {
            if (lastValues.get(i) == 1) {
                index.add(i);
            }
        }

        for (int i =0; i < index.size(); i++) {
            int countOnes = Integer.bitCount(index.get(i));
            if (countOnes > 1) {
                System.out.println("Функция не принадлежит классу TL");
                FTL = true;
                return;
            }
        }
        System.out.println("Функция принадлежит классу TL");

    }
    private static void FunctionalSet(){
        if (FT0 && FT1 && FTM && FTS && FTL) {
            System.out.println("Данный набор является полным");
        } else {
            System.out.println("Данный набор не является полным");
        }
    }
}