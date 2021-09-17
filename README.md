# projetorefatorado
Code Smells identificados

Long Parameter List: Existem muitos métodos com parâmetros que nem sempre são necessários.

Feature Envy: Métodos na folha de pagamento parecem mais interessadas em todas as outras classes importadas

Lazy Class: Todos os módulos de pagamento têm Lazy Class.

Middle Man: Métodos de interface estão delegando trabalho a outras classes da folha de pagamento.

Data Class: Empregados e todos os módulos de pagamento não possuem métodos.

Long Method: Muitos metodos com long method.

Large Class: A folha possui muitas atribuiçoes.



Refatoramento
   1 O método pagar() no aqruivo Menu possuia o smell Long Method que foi resolvido dividindo-o em passos através de outros três métodos com base no design move accumulation to collecting parameter, foram criados os metodos weeklyPagar, biweeklyPagar e monthlyPagar.
   
   2 O padrão Strategy foi aplicado no método alterapessoal() de modo a evitar ifs desnecesários que checavam o tipo de empregado. Foi criada uma interface e duas estratégias, Alteraum e Alteradois.

   3 O padrão Template foi implementado para substituir os três métodos de inserção de cada tipo de empregado. A classe abstrata Inserirtemplate() contém a implementação comum a todas as subclasses, e as subclasses implementam conforme suas necessidades no método instantiate(). As subclasses são instanciadas no método adicionar() no modulo Menu.py 
