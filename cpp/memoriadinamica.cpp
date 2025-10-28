#include <iostream>

using namespace std;

int main(){

    // new Permite asignar memoria en el monticulo (heap) en lugar del stack
    int *pNum = NULL;

    pNum = new int; // asigna memoria para un entero y asi devuelve una direccion igualda al puntero

    *pNum = 25;

    cout<< "direccion: "<< pNum << endl;
    cout<< "valor: "<< *pNum << endl;

    // de buena practica liberar la memoria
    delete pNum;

    return 0;
}