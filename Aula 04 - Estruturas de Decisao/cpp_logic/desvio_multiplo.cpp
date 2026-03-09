#include <iostream>
using namespace std;

int main() {
    int quantidade;
    cout << "Digite a quantidade em estoque: ";
    cin >> quantidade;

    if (quantidade < 1) {
        cout << "Status: em falta." << endl;
    } else if (quantidade < 5) {
        cout << "Status: alerta de estoque baixo." << endl;
    } else {
        cout << "Status: estoque OK." << endl;
    } 

    return 0;
}
