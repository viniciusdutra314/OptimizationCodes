#include <math.h>
#include <iostream>

float polinomio(float x ,float coeficientes[],int grau){
    float soma=0;
    for (int i=0; i<grau+1; i++){
        soma+=std::pow(x,i)*coeficientes[i];}
    return soma;
}
float derivada_polinomio(float x ,float coeficientes[], int grau){
    float soma=0;
    for (int i=1; i<grau+1; i++){
        soma+=std::pow(x,i-1)*coeficientes[i]*i;}
    return soma;
}

int main(){
    int times=0;
    int grau=2;
    while (times<100){
        float coeficientes[grau+1];
        for (int i=0;i<grau+1;i++)
            {coeficientes[i]=(float) 2*rand()/RAND_MAX -1;}
        float x0=(float) 2*rand()/RAND_MAX -1;
        for(int _ =0; _<100;_++)
            {float x=x0-(polinomio(x0,coeficientes,grau)/derivada_polinomio(x0,coeficientes,grau));
            x0=x;}
        std::cout << "Polinomio ";
        for (int i=0;i<grau+1;i++){
            std::cout << coeficientes[i] << " ";}
        if (fabs(polinomio(x0,coeficientes,grau))<0.001){
            std::cout << "Raiz encontrada " << x0 <<std::endl;}
        else
        {   std::cout << "NÃO FOI ENCONTRADA " << x0 <<std::endl;}
        times+=1;}
    float array[3]={0,0,1};
    std::cout << polinomio(5,array,3);
    std::cout << derivada_polinomio(5,array,3);
}