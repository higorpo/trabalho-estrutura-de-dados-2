class Nodo:
    # Inicializa o construtor da classe recebendo um dado numérico.
    # Inicializa também as informações do nodo referente a se tem filhos para esquerda/direita e o seu balanceamento
    def __init__(self, code: int) -> None:
        self.__code = code
        self.__left = None
        self.__right = None

    @property
    def code(self) -> str:
        return str(self.__code)

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
        # Elemento filho da direta se torna o elemento filho da direita da antiga raíz
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

    def balancear_nodo(self):
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

        self.balancear_nodo()

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
