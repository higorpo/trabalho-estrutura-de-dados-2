class Nodo:
    # Inicializa o construtor da classe recebendo um dado numérico.
    # Inicializa também as informações do nodo referente a se tem filhos para esquerda/direita e o seu balanceamento
    def __init__(self, code: int) -> None:
        self.__code = code
        self.__left = None
        self.__right = None

    @property
    def code(self) -> int:
        return self.__code

    @code.setter
    def code(self, new_code) -> str:
        self.__code = new_code

    # Método para descobrir a profundidade de um nó
    def profundidade(self):
        profundidade_esquerda = 0
        profundidade_direita = 0

        if self.__left is not None:
            # Aplica uma função de recursividade para ir até o último nó possível começando a partir do filho da esquerda do nó atual,
            # e então através dos retornos da função recursiva trazer o total de níveis do filho a esquerda do nó atual;
            profundidade_esquerda = self.__left.profundidade()

        if self.__right is not None:
            # Aplica uma função de recursividade para ir até o último nó possível começando a partir do filho da direita do nó atual,
            # e então através dos retornos da função recursiva trazer o total de níveis do filho a direita do nó atual;
            profundidade_direita = self.__right.profundidade()

        # Usa a função max para pegar qual dos dois lados tem o maior número de níveis a baixo (para saber qual é a maior profundidade)
        # Usa o 1 apenas para a função recursiva funcionar, e quando ir ao último nível, recursivamente vai fazendo a soma dos valores
        # dos níveis necessário.
        return 1 + max(profundidade_esquerda, profundidade_direita)

    # Método para descobrir qual é o fator de balanceamento do nó atual
    def fator_balanceamento(self):
        # Pega a profundidade total do elemento a esquerda e a direita do nó atual, depois
        # subtraí a quantidade de níveis do filho da esquerda com a quantidade de níveis do filho da direita.
        profundidade_esquerda = self.__left.profundidade() if self.__left else 0
        profundidade_direita = self.__right.profundidade() if self.__right else 0

        return profundidade_esquerda - profundidade_direita

    # Método para rotacionar para esquerda
    def __rotacionar_esquerda(self):
        # Guarda os valores antigos para podermos reutilizar na nova variação
        old_self_code = self.code
        old_self_left = self.__left
        elem_right = self.__right

        self.code = elem_right.code  # Elemento da direita se torna o nó raiz
        # Elemento filho da direta se torna o elemento filho da direita da nova raíz
        self.__right = elem_right.__right

        # A antiga raíz se torna filha a esquerda da nova raíz
        self.__left = Nodo(old_self_code)
        # O filho esquerdo da antiga raíz continua o mesmo
        self.__left.__left = old_self_left
        # O filho esquerdo da atual raíz (quando era filho da antiga raíz) se torna o filho direito da raíz antigo
        self.__left.__right = elem_right.__left

    # Método para rotacionar a direita
    def __rotacionar_direita(self):
        # Guarda os zalores antigos para podermos reutilizar na nova variação
        old_self_code = self.code
        elem_left = self.__left
        elem_right = self.__right

        self.code = elem_left.code  # Elemento da esquerda se torna o nó raíz

        # Antiga raíz se torna elemento da direita da nova raíz
        self.__right = Nodo(old_self_code)
        # Elemento da direita da nova raíz recebe antigo elemento da direita da antiga raíz em sua direita
        self.__right.__right = elem_right
        # Elemento da direita da nova raíz recebe antigo elemento direito do antigo elemento esquerdo da antiga raíz a sua esquerda
        self.__right.__left = elem_left.__right

        # Elemento esquerdo da nova raíz recebe elemento esquerdo da antiga esquerda da antiga raíz
        self.__left = elem_left.__left

    def __balancear_nodo(self):
        fator_balanceamento = self.fator_balanceamento()

        if fator_balanceamento in [-1, 0, 1]:
            pass
        else:
            if fator_balanceamento == -2:
                if self.__right.fator_balanceamento() < 0:
                    # Rotação simples para a esquerda
                    self.__rotacionar_esquerda()
                else:
                    # Rotação direita esquerda
                    self.__right.__rotacionar_direita()
                    self.__rotacionar_esquerda()
            elif fator_balanceamento == 2:
                if self.__left.fator_balanceamento() > 0:
                    # Rotação simples para a direita
                    self.__rotacionar_direita()
                else:
                    # Rotacionar esquerda direita
                    self.__left.__rotacionar_esquerda()
                    self.__rotacionar_direita()

    # Função para adicionar um novo dado a árvore AVL
    def add(self, new_code: int) -> None:
        # print('adicionando... ', str(new_code))
        # Verifica se o valor que estamos tentando adicionar é menor que o valor do nó
        if int(new_code) < int(self.__code):
            # É um valor menor, verifica se existe um filho a esquerda desse nó
            if self.__left is None:
                # Não existe um filho a esquerda, então adicionamos um.
                self.__left = Nodo(new_code)
            else:
                # Já existe filho a esquerda, então pedimos pra ele seguir o fluxo para adicionar um novo elemento
                self.__left.add(new_code)
        else:
            # Éu m valor maior, verifica se existe um filho a direita desse nó
            if self.__right is None:
                # Não existe um filho a direita, então adicionamos um.
                self.__right = Nodo(new_code)
            else:
                # Já existe filho a direita, então pedimos pra ele seguir o fluxo para adicionar um novo elemento
                self.__right.add(new_code)

        self.__balancear_nodo()

    # Método para realizar uma busca dentro da árvore
    def buscar(self, code: int):
        # Verifica se o código que está sendo buscado é menor que o código do nó atual
        if code < self.code:
            # Se não existir filhos, é porque o elemento não existe
            if self.__left is None and self.__right is None:
                return None

            # Se existir filhos menor que o nó atual, então vamos percorrer ele
            return self.__left.buscar(code)

        # Verifica se o código que está sendo buscado é maior que o código do nó atual
        elif code > self.code:
            # Se não existir filhos, é porque o elemento não existe
            if self.__left is None and self.__right is None:
                return None

            # Se existir filhos maior que o nó atual, então vamos percorrer ele
            return self.__right.buscar(code)

        # O código do nó atual é igual ao que está sendo procurado... encontramos o elemento!
        elif code == self.code:
            return self

    # Procura o menor elemento de um nó
    def procura_menor(self):
        no1 = self
        no2 = self.__left
        while no2 != None:
            no1 = no2
            no2 = no2.__left
        return no1

    # Remove os elementos vazios da árvore através de uma recursividade
    def __limpar_arvore(self):
        if self.__left is not None and self.__left.code is None:
            self.__left = None

        if self.__right is not None and self.__right.code is None:
            self.__right = None

        if self.__left is not None:
            self.__left.__limpar_arvore()

        if self.__right is not None:
            self.__right.__limpar_arvore()

    # Método para remover um elemento da árvore [https://www.youtube.com/watch?v=F7_Daymw-WM]
    def remover(self, code: int):
        # Faz uma consulta inicial para saber se o elemento existe na minha árvore...
        if self.buscar(code) is None:
            return None

        res = None
        # Se o elemento a ser removido é menor que a minha raíz atual...
        if code < self.code:
            # Executa função recursiva de remoção do nó da esquerda
            res = self.__left.remover(code)
            if res == 1:
                # Se retornar que removeu, então balanceia a árvore novamente
                self.__balancear_nodo()

        # Se o elemento a ser removido é maior ue a minha raíz atual
        elif code > self.code:
            # Executa função recursiva de remoção do nó da direita
            res = self.__right.remover(code)
            if res == 1:
                # Se retornar que removeu, então balanceia a árvore novamente
                self.__balancear_nodo()
        else:
            # Se o elemento a ser removido é o elemento da raíz atual, verificamos se um dos filhos dele é nulo
            if self.__left is None or self.__right is None:
                # Verifica se o filho da esquerda não é nulo
                if self.__left is not None:
                    # Pegamos então o filho direto a esquerda do elemento atual e ele passa a ser a nova raíz
                    self.code = self.__left.code
                    # Atribuímos a nova raíz o left e o right do elemento que pegamos para ser a raíz
                    self.__left = self.__left.__left if self.__left else None
                    self.__right = self.__left.__right if self.__left else None
                else:
                    # Pegamos então o filho direto a direita do elemento atual e ele passa a ser a nova raíz
                    self.code = self.__right.code if self.__right else None
                    # Atribuímos a nova raíz o left e o right do elemento que pegamos para ser a raíz
                    self.__left = self.__right.__left if self.__right else None
                    self.__right = self.__right.__right if self.__right else None
            else:
                # Nenhum dos dois filhos é nulo, então procuramos o menor elemento da raíz da direita
                # e ao encontrarmos ele passa a ser a nova raíz
                temp = self.__right.procura_menor()
                self.code = temp.code
                # depois removemos a sua "duplicada" do nó da direita e assim finalizamos
                self.__right.remover(temp.code)
                # Balanceia novamente a árvore
                self.__balancear_nodo()
                return 1

        # Lipamos os elementos vazios da árvore
        self.__limpar_arvore()

        # Fazemos um último balanceamento se assim for necessário
        self.__balancear_nodo()

        return res

    def printThree(self, indent=0):
        print(
            ' ' * indent + str(self.code) +
            ' (profundidade: ' + str(self.profundidade()) + ')'
            ' (balanço: ' + str(self.fator_balanceamento()) + ')'
        )
        if self.__left:
            self.__left.printThree(indent + 4)
        if self.__right:
            self.__right.printThree(indent + 4)
