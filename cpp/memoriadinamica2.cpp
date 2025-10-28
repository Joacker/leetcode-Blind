#include<iostream>
using namespace std;

int main(){

    char *pNotas = NULL;
    int tam;

    cout << "Cuantas notas deseas ingresar?: ";
    cin >> tam;

    pNotas = new char[tam];

    for(int i = 0; i < tam; i++){
        cout << "Ingresa la nota " << i + 1 << ": ";
        cin >> pNotas[i];
    }

    for(int i = 0; i < tam; i++){
        cout << "La nota " << i + 1 << " es: " << pNotas[i] << endl;
    }

    delete[] pNotas;

    return 0;
}