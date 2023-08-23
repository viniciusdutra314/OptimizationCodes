#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float function(float x)
    {return sin(x);}

float derivate(float x)
    {return cos(x);}
float secondderivate(float x)
    {return -sin(x);}

int main(int argc, char *argv[])
{  float x0=atof(argv[1]);
   if (derivate(x0)==0){
    printf("Escolha outro ponto, neste a derivada é zero"); exit(1);}
   int N=1000000;
   for(int _ =0; _<N;_++)
   {float x=x0-(function(x0)/derivate(x0))/(1-(function(x)*secondderivate(x))/(2*derivate(x)*derivate(x)));
    x0=x;}
   printf("%f",x0);
}
