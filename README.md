# projetorefatorado
Refatoramento
   1 O método pagar() no aqruivo Menu possuia o smell Long Method que foi resolvido dividindo-o em passos através de outros três métodos com base no design move accumulation to collecting parameter, foram criados os metodos weeklyPagar, biweeklyPagar e monthlyPagar.
   
   2 O padrão Strategy foi aplicado no método changePersonalData() de modo a evitar ifs desnecesários que checavam o tipo de empregado. Foi criada uma interface e duas estratégias, SimpleChange e DifferentChange, sendo a classe DifferentChange() aos comissionados.

   3 O padrão Template foi implementado para substituir os três métodos de inserção de cada tipo de empregado. A classe abstrata Inserirtemplate() contém a implementação comum a todas as subclasses, e as subclasses implementam conforme suas necessidades no método instantiate(). As subclasses são instanciadas no método adicionar() no modulo Menu.py 
