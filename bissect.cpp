#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float function(float x){
    return x*x -5*x +6;

}

int main(int argc, char *argv[])
{   float x0=atof(argv[1]); // initial guess
    float a,b ,c;
    a=1 ; b=2.5 ; 
    if (signbit(function(a))==signbit(function(b))){
        printf("f(a) tem o mesmo sinal de f(b)");exit(1);}
    int N = 100;
    float epislon =0;
    for(int i=0;i<N ;i++){
        c =(a+b)/2;
        float f_c=function(c);
        if (abs(f_c)<epislon){break;}
        if (signbit(f_c)==signbit(function(a))) {a=c;}
        if (signbit(f_c)==signbit(function(b))){b=c;}}
    printf("x=%f",c);
}
