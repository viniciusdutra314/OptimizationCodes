#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float function(float x){
    return sin(x)*x +x -(x*x)/10;

}

int main()
{   float a,b ,c;
    a=1 ; b=4 ; 
    if (signbit(function(a))==signbit(function(b))){
        printf("f(a) tem o mesmo sinal de f(b)");exit(1);}
    int N = 100;
    float epislon =0;
    for(int i=0;i<N ;i++){
        c =((a*function(b)-b*function(a)))/(function(b)-function(a));
        float f_c=function(c);
        if (abs(f_c)<epislon){break;}
        if (signbit(f_c)==signbit(function(a))) {a=c;}
        if (signbit(f_c)==signbit(function(b))){b=c;}}
    printf("%f",c);
}
