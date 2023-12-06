#include <iostream>
#include <cmath>
#include <vector>

int n;
std::vector <std::string> functions;

void Input() {
    std::cout << "Enter number of functions:\n";
    std::string buff;
    // Проверка на корректность входных данных
    while(true) {
        std::cin >> buff;
        // Проверка, что ввели число
        bool OK = true;
        for(int i = 0; i < buff.size(); i++) {
            if(buff[i] < '0' || buff[i] > '9') {
                OK = false;
                break;
            }
        }
        if(!OK || buff.size() > 9) {
            std::cout << "\nInvalid input data.\nEnter number of functions:";
            continue;
        }
        n = std::stoi(buff);
        if(n == 0) {
            std::cout << "\nInvalid input data.\nEnter number of functions:";
            continue;
        }
        break;
    }
    for(int i = 1 ; i <= n; i++) {
        std::cout << "Enter function " << i << ":\n";
        std::string s;
        std::cin >> s;
        // Проверка, что введенная функция содержит только нули и единицы
        bool OK = 1;
        for(int j = 0; j < s.size(); j++) {
            if(s[j] != '0' && s[j] != '1') {
                OK = 0;
                break;
            }
        }
        if(!OK) {
            std::cout << "Invalid input data! Try again!\n";
            i--;
            continue;
        }
        // Проверка, что длина функции степень двойки
        int length = s.size();
        if(powl(2,log2((long double) length)) != length) {
            std::cout << "Invalid input data! Try again!\n";
            i--;
            continue;
        }
        // Если введенная функция прошла проверку, то записываем ее
        functions.push_back(s);
    }
}

bool less(int a,int b) {
    while(b > 0) {
        if(a % 2 > b % 2) {
            return false;
        }
        a /= 2;
        b /= 2;
    }
    return true;
}

int kolv_1(int x) {
    // Функция, которая считает количество единиц в двоичной записи числа
    int ans = 0;
    while(x > 0) {
        if(x % 2 == 1){
            ans++;
        }
        x /= 2;
    }
    return ans;
}

int class_S(std::string s) {
    for(int i = 0; i < s.size() / 2; i++) {
        if(s[i] == s[s.size() - i - 1]) {
            return 0;
        }
    }
    return 1;
}

int class_T0(std::string s) {
    if(s[0] == '0') {
        return 1;
    } else {
        return 0;
    }
}

int class_T1(std::string s) {
    if(s[s.size() - 1] == '1') {
        return 1;
    } else {
        return 0;
    }
}

int class_M(std::string s) {
    for(int i = 0; i < s.size(); i++) {
        for(int j = i + 1; j < s.size(); j++) {
            if(less(i,j) && s[i] > s[j]) {
                return 0;
            }
        }
    }
    return 1;
}

int class_L(std::string s) {
    // Строим полином Жегалкина методом треугольника
    std::string triangle[s.size()];
    triangle[0] = s;
    for(int i = 1; i < s.size(); i++) {
        int j = 1;
        while(j < triangle[i - 1].size()) {
            if(triangle[i - 1][j - 1] == triangle[i - 1][j]) {
                triangle[i] += '0';
            } else {
                triangle[i] += '1';
            }
            j++;
        }
    }
    // Проверяем, функцию на линейность
    for(int i = 0; i < s.size(); i++) {
        if(triangle[i][0] == '1' && kolv_1(i) > 1) {
            return false;
        }
    }
    return true;
}

int main() {
    Input();
    int T0 = 0, T1 = 0, S = 0, M = 0, L = 0;

    std::cout << "T0 ";
    for(int i = 0; i < n; i++) {
        if(class_T0(functions[i]) == 1) {
            std::cout << 1 << ' ';
        } else {
            std::cout << 0 << ' ';
            T0 = 1;
        }
    }

    std::cout << '\n' << "T1 ";
    for(int i = 0; i < n; i++) {
        if(class_T1(functions[i]) == 1) {
            std::cout << 1 << ' ';
        } else {
            std::cout << 0 << ' ';
            T1 = 1;
        }
    }

    std::cout << '\n' << "S  ";
    for(int i = 0; i < n; i++) {
        if(class_S(functions[i]) == 1) {
            std::cout << 1 << ' ';
        } else {
            std::cout << 0 << ' ';
            S = 1;
        }
    }

    std::cout << '\n' << "M  ";
    for(int i = 0; i < n; i++) {
        if(class_M(functions[i]) == 1) {
            std::cout << 1 << ' ';
        } else {
            std::cout << 0 << ' ';
            M = 1;
        }
    }

    std::cout << '\n' << "L  ";
    for(int i = 0; i < n; i++) {
        if(class_L(functions[i]) == 1) {
            std::cout << 1 << ' ';
        } else {
            std::cout << 0 << ' ';
            L = 1;
        }
    }

    if(T0 && T1 && S && M && L) {
        std::cout << "\nThe set of Boolean functions is complete";
    } else {
        std::cout << "\nThe set of Boolean functions is not complete";
    }
    return 0;
}