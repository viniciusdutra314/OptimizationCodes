#include <iostream>
#include <math.h>
#include <fstream>


long double function(long double x){
    return sin(x);}

long double derivative(long double x){
    return cos(x);}

long double newton (long double x0){
    return x0-(function(x0)/derivative(x0));}

void write_to_file(long double x0, long double a_initial){
    std::fstream arquivo("data_bisnewton.dat",std::ios::app);
    arquivo <<x0<<" "<<a_initial<<"\n";

}


int main()
{   long double a=1 ; long double b=4; long double c;
    if (signbit(function(a))==signbit(function(b))){
    printf("f(a) tem o mesmo sinal de f(b)");exit(1);}
    long double epsilon = 1e-19;
    int N=100; //max iterations
    c=(a+b)/2;
    int times=1;
    while(times<N){
        c=newton(c);
        if (a>c || c>b){
            std::cout << a <<"  "<< c << "  " << b <<std::endl ;
            c =(a+b)/2;}
        float f_c=function(c);
        write_to_file(times,f_c);
        if (fabs(f_c)<fabs(epsilon)){break;}
        if (signbit(f_c)==signbit(function(a))) {a=c;}
        if (signbit(f_c)==signbit(function(b))){b=c;}
        times+=1;}

}