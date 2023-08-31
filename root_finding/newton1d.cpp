#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float function(float x)
    {return x*x -3;}

float derivate(float x)
    {return 2*x;}

int main(int argc, char *argv[])
{  float x0=atof(argv[1]);
   if (derivate(x0)==0){
    printf("Escolha outro ponto, neste a derivada é zero"); exit(1);}
   int N=10;
   for(int _ =0; _<N;_++)
   {float x=x0-(function(x0)/derivate(x0));
    x0=x;}
   printf("%f",x0);
}
