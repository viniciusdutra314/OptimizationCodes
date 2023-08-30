
class Polinomio:
    '''gera polinomios apartir de raizes ou de coeficientes
    raizes : list[float or complex]
    coeficientes : list[float]
    a_fator : float (p(x)=a_fator * prod (x-raiz_i))

    Possui métodos que printam os coeficiente do polinomio, com
    derivada(k) é retorna a derivada de ordem 1 do polinomio

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
        soma=0
        for n,coeficiente in enumerate(self.coeficientes):
            soma+=coeficiente*x**(len(self.coeficientes)-n-1)
        return soma
    def __str__(self):
        string=''
        for i,coeficiente in enumerate(self.coeficientes):
            string+=f"{coeficiente}x^{len(self.coeficientes)-i-1} "
        return string[:-4]
    def derivada(self,n=1):
        '''Calcula a enesima derivada, por padrão n=1
           Retorna um objeto da classe Polinomio'''
        novos_coeficientes=[]
        for i in range(len(self.coeficientes)-n):
            produto=1
            for j in range(n):
                produto*=(len(self.coeficientes)-i-j-1)
            novos_coeficientes.append(produto*self.coeficientes[i])
        return Polinomio(coeficientes=novos_coeficientes)