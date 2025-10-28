// & direccion
// * referencia
#include <iostream>
using namespace std;
int main() {
    string nombre = "Joaquin";
    int edad = 24;
    string pizzasGratis[5] = {"Margarita", "Cuatro Quesos", "Hawaiana", "Pepperoni", "Vegetariana"};
    // tipo de dato del puntero es para una cadena con el operador de referecia *
    // apuntamos al nombre y se establece a la direccion de esa variable &
    string *pNombre = &nombre;
    int *pEdad = &edad;
    // string *pPizzasGratis = &pizzasGratis;

    cout << pNombre << endl; //mostrar puntero en la consola
    // para mostrar el contenido del puntero se usa el oprador *
    cout << *pNombre << endl; //mostrar contenido del puntero en la consola

    cout << pEdad << endl; //mostrar puntero en la consola
    // para mostrar el contenido del puntero se usa el oprador *
    cout << *pEdad << endl; //mostrar contenido del puntero en la consola
    // En el caso de un arreglo le estamos pasando la direccion a nuestro puntero
    cout << pizzasGratis << endl; //mostrar puntero en la consola
    cout << *pizzasGratis << endl; //mostrar puntero en la consola

    return 0;
}