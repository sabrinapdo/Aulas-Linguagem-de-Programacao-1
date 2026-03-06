#include <iostream>
using namespace std;

int main() {
    int quantidade;
    cout << "Digite quantidade em estoque: ";
    cin >> quantidade;
    
    // Usando a estrutura if 
    if (quantidade < 5) {
        cout << "AVISO: O estoque desse produto está baixo!" << endl;
    } 

    return 0;
}