import javax.swing.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
public class rgr1 {
    public static boolean CheckSet(char[][] s, char[][] y) {
        for (int i = 0; i < s.length; i++) {
            if (y[i][0] < s[i][0]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        ArrayList<String> listT0 = new ArrayList<>();
        ArrayList<String> listT1 = new ArrayList<>();
        ArrayList<String> listS = new ArrayList<>();
        ArrayList<String> listL = new ArrayList<>();
        ArrayList<String> listM = new ArrayList<>();

        int g = -1;
        while (g < 0) {
            String func;
            func = JOptionPane.showInputDialog("Введите количество функций");
            int a = Integer.parseInt(func);
            if (a > 0) {
                g++;
                for (int i = 0; i < a; i++) {
                    int r = -1;
                    while (r < 0) {
                        int u = -1;
                        while (u < 0) {
                            String input = JOptionPane.showInputDialog("Введите функцию");
                            if (input.matches("[01]+")) {
                                u++;
                                int b = input.length();
                                boolean t = false;
                                int power = 0, temp = 0;

                                while (temp < b) {
                                    temp = (int) (Math.pow(2, power));
                                    power++;
                                    if (temp == b) {
                                        t = true;
                                    }
                                }
                                if (t) {
                                    r++;

                                        char[] text = input.toCharArray();

                                        int size = text.length;
                                        char[][] array = new char[size][];

                                        //T0
                                        for (int j = 0; j < size; j++) {
                                            array[j] = String.valueOf(text[j]).toCharArray();
                                        }
                                        if (array[0][0] == '0') {
                                            System.out.print("T0 ");
                                            listT0.add("1");
                                        } else {
                                            System.out.print("not T0 ");
                                            listT0.add("0");
                                        }

                                        //T1
                                        for (int j = 0; j < size; j++) {
                                            array[j] = String.valueOf(text[j]).toCharArray();
                                        }
                                        if (array[array.length - 1][0] == '1') {
                                            System.out.print("T1 ");
                                            listT1.add("1");
                                        } else {
                                            System.out.print("not T1 ");
                                            listT1.add("0");
                                        }

                                        //S
                                        ArrayList<String> listS1 = new ArrayList<>();

                                        for (int o = 0; o < size; o++) {
                                            int oppositeI = size - 1 - o;

                                            int valueI = Character.getNumericValue(input.charAt(o));
                                            int valueOppositeI = Character.getNumericValue(input.charAt(oppositeI));


                                            if (valueI == valueOppositeI) {
                                                listS1.add("0");
                                            } else {
                                                listS1.add("1");
                                            }
                                        }
                                        if (listS1.contains("0")) {
                                            System.out.print("not S ");
                                            listS.add("0");
                                        } else {
                                            System.out.print("S ");
                                            listS.add("1");
                                        }

                                        //L
                                        ArrayList<String> listL1 = new ArrayList<>();

                                        List<Integer> functionList = new ArrayList<>();
                                        for (int n = 0; n < size; n++) {
                                            int value = Character.getNumericValue(input.charAt(n));
                                            functionList.add(value);
                                        }
                                        ArrayList<ArrayList<Integer>> triangle = new ArrayList<>();
                                        ArrayList<Integer> firstValuesList = new ArrayList<>();

                                        triangle.add((ArrayList<Integer>) functionList);
                                        firstValuesList.add(triangle.get(0).get(0));

                                        for (int n = 0; n < functionList.size() - 1; n++) {
                                            ArrayList<Integer> nextLine = new ArrayList<>();
                                            for (int j = 1; j < functionList.size() - n; j++) {
                                                Integer resault = (triangle.get(n).get(j) ^ triangle.get(n).get(j - 1));
                                                nextLine.add(resault);
                                            }
                                            triangle.add(nextLine);
                                            firstValuesList.add(triangle.get(n + 1).get(0));
                                        }


                                        List<Integer> indexWith1 = new ArrayList<>();
                                        for (int n = 0; n < firstValuesList.size(); n++) {
                                            if (firstValuesList.get(n) == 1) {
                                                indexWith1.add(n);
                                            }
                                        }

                                        for (int n = 0; n < indexWith1.size(); n++) {
                                            int count1 = Integer.bitCount(indexWith1.get(n));

                                            if (count1 > 1) {
                                                listL1.add("0");
                                            } else {
                                                listL1.add("1");
                                            }
                                        }

                                        if (listL1.contains("0")) {
                                            System.out.print("not L ");
                                            listL.add("0");
                                        } else {
                                            System.out.print("L ");
                                            listL.add("1");
                                        }

                                        //M
                                        boolean M = true;
                                        int ka = 1;
                                        int ve = 1;
                                        while (ka < size && M) {
                                            for (int in = 0; in < size && M; in += 2 * ka) {
                                                char[][] s = Arrays.copyOfRange(array, in, in + ka);
                                                char[][] y = Arrays.copyOfRange(array, in + ka, in + 2 * ka);
                                                if (!CheckSet(s, y)) {
                                                    M = false;
                                                    //нарушено
                                                } else {
                                                    M = true;
                                                    //выполнено
                                                }
                                            }
                                            ka *= 2;
                                            ve++;
                                        }
                                        if (M) {
                                            System.out.print("M");
                                            System.out.println(" ");
                                            listM.add("1");
                                        } else {
                                            System.out.print("not M");
                                            System.out.println(" ");
                                            listM.add("0");
                                        }

                                } else {
                                    System.out.println("Неверная длина функции!");
                                }

                            } else {
                                System.out.println("Ввод не содержит только цифры 0 и 1!");
                            }
                        }
                    }
                }


            } else {
                System.out.println("Введите корректное количество функций!");
            }
        }

        if(listT0.contains("0") && listT1.contains("0") && listS.contains("0") && listL.contains("0") && listM.contains("0")) {
            System.out.println("Набор является полным");
        } else {
            System.out.println("Набор не является полным");
        }
    }
}