# projetorrefatorado
Refatoramento

    O método payEmployee() do modulo payroll possuia o smell Long Method que foi resolvido dividindo-o em passos através de outros três métodos com base no design move accumulation to collecting parameter, foram criados os metodos weeklyPayment(), biweeklyPayment() e monthlyPayment() que passaram a ser invocados em payEmployee(). Veja alterações clicando aqui
    O padrão Strategy foi aplicado no método changePersonalData() de modo a evitar ifs desnecesários que checavam o tipo de funcionário. Foi criada uma interface e duas estratégias, SimpleChange e DifferentChange, sendo a classe DifferentChange() aplicável aos funcionários comissionados, pois possuem mais atributos que precisam ser alterados. Veja alterações clicando aqui
    O padrão Template foi implementado para substituir os três métodos de inserção de cada tipo de funcionário. A classe abstrata InsertEmployee() contem a implementação comum a todas as subclasses, e as subclasses implementam conforme suas necessidades no método instantiate(). As subclasses são instanciadas no método addEmployee() no modulo payroll.py Veja alterações clicando aqui
