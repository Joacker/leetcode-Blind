#include <iostream>
using namespace std;

int main() {

    int *puntero = nullptr;
    int x = 123;

    // Asignar la direccion de x al puntero
    puntero = &x;

    if(puntero == nullptr) {
        // la direccion no se asigno
        cout << "El puntero es nulo." << endl;
    } else {
        // la direccion fue asignada
        cout << "El puntero no es nulo." << endl;
        cout << "Direccion almacenada en el puntero: " << puntero << endl;
        cout << "Valor apuntado por el puntero: " << *puntero << endl;
    }

    return 0;
}