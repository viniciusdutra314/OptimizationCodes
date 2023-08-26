class Polinomio:
    '''gera polinomios apartir de raizes ou de coeficientes
    raizes : list[float or complex]
    coeficientes : list[float or complex]
    a_fator : float (p(x)=a_fator * prod (x-raiz_i))

    Possui métodos que printam os coeficiente do polinomio, com
    derivada e segunda_derivada é returnada a função que
    é a derivada primeira ou segunda do polinomio
    '''

    def __init__(self, raizes =[], coeficientes =[],a_fator=1):
        self.raizes=raizes ; self.a_fator=a_fator; self.coeficientes=coeficientes
        assert coeficientes or raizes , "Forneça as raizes ou os coeficientes"
        if not self.coeficientes:
            from itertools import combinations
            self.coeficientes=[self.a_fator]
            def girard(lista : iter) -> float:
                soma=0; 
                for tuplas in lista:
                    produto=1
                    for elemento in tuplas:
                        produto*=elemento
                    soma+=produto
                return (soma*self.a_fator).real
            for j in range(len(self.raizes)):
                combinacoes=combinations(self.raizes,j+1)
                self.coeficientes.append((girard(combinacoes))*(-1)**(j+1))
    def __call__(self, x:float) -> float:
        if self.raizes:
            produto=self.a_fator
            for raiz in self.raizes:
                produto*=(x-raiz)
            return produto if produto.imag!=0 else produto.real
        if self.coeficientes:
            soma=0
            for n,coeficiente in enumerate(self.coeficientes):
                soma+=coeficiente*x**(len(self.coeficientes)-n-1)
            return soma
    def __str__(self):
        string=''
        for i,coeficiente in enumerate(self.coeficientes):
            string+=f"{coeficiente}x^{len(self.coeficientes)-i-1} "
        return string[:-4]
    def derivada(self) -> callable:
        def grad(x):
            soma=0
            coeficientes_invertidos=reversed(self.coeficientes)
            for n,coeficiente in enumerate(coeficientes_invertidos):
                soma+=n*coeficiente*x**(n-1)
            return soma
        return grad
    def segunda_derivada(self) -> callable:
        def segundo_grad(x):
            soma=0
            coeficientes_invertidos=reversed(self.coeficientes)
            for n,coeficiente in enumerate(coeficientes_invertidos):
                soma+=(n-1)*n*coeficiente*x**(n-2)
            return soma
        return segundo_grad