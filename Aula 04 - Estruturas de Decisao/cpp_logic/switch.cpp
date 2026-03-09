#include <iostream>
using namespace std;

int main() {
    int codigo_status;
    cout << "Digite o código de status (1= Disponínel, 2= Reposição, 3= Descontinuado): ";
    cin >> codigo_status;

    switch (codigo_status) {
        case 1: cout << "Status: Disponível." << endl;
            break;
        case 2: cout << "Status: Em Reposição." << endl;
            break;
        case 3: cout << "Status: Desconinuado." << endl;
            break;
        default: cout << "Código de status inválido." << endl;
    }


    return 0;
}