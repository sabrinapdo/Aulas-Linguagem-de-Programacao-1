#include <iostream>
using namespace std;

int main() {
    double ganho, investimento;

    cout << "Digite o ganho: ";
    cin >> ganho;

    cout << "Digite o investimento: ";
    cin >> investimento;

    if (investimento == 0) {
        cout << "Erro: investimento nao pode ser zero." << endl;
    } else {
        double roi = ((ganho - investimento) / investimento) * 100;
        cout << "ROI: " << roi << "%" << endl;
    }

    return 0;
}
