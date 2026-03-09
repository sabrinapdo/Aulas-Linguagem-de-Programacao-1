#include <iostream>
using namespace std;

int main() {

    string nome_do_produto;
    int quantidade_em_estoque;
    float preco_unitario;

    while (true) {

        cout << "Digite o nome do produto: ";
        cin >> nome_do_produto; 

        cout << "Digite a quantidade em estoque: ";
        cin >> quantidade_em_estoque;

        cout << "Digite o preco do produto: ";
        cin >> preco_unitario;

        if (quantidade_em_estoque >= 0) {
            cout << "Nome do produto: " << nome_do_produto
                 << ", quantidade em estoque: " << quantidade_em_estoque
                 << ", preco unitario: " << preco_unitario << endl;
        } 
        else {
            cout << "ERRO: a quantidade não pode ser um valor negativo. Por favor, tente novamente. " << endl;
        }

        cout << endl;
    }

    return 0;
}
