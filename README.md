1. Introdução
As seguites tarefas foram realizadas para adicionar a nova funcionadalide de itens "Conjurados" e garantir que todo o sistema funcione conforme solicitado no exercício:
a- Refatoração do código para ter métodos mais bem separados e unitários.
b- Adição de nova categoria de itens "Conjurados".

2. Descrição do Processo de Refatoração
Abaixo descrevo o que foi realizado no processo:

a. Análise do Código Existente: O código forncido foi análisado para compreender o que o mesmo fazia em detalhes;
b. Divisão em Métodos Menores: Separação da lógica em métodos menores e mais unitários para cada tipo de item;
c. Nova Funcionalidade: Implementação da lógica para itens "Conjurados";
d. Teste e Validação: Garantia de que todas as regras de negócios especificadas continuam a ser respeitadas após a refatoração e a adição da nova funcionalidade rodando os testes test_gilded_rose.py e textteste_fixture.py.

3. Dificuldades Encontradas
a. Compreensão Inicial: Toda a lógica estava em um único método com diversos ifs e elses com diferentes objetivos, o que dificultou bastante a compreenção do que cada parte do código fazia;
b. Gerenciamento de Qualidade: Garantir que a qualidade dos itens não excedesse 50 e não fosse negativa em todas as situações foi um processo dificil na compreensção do código e como separar esta funcionalidade;

4. Considerações finais
a. Importância da Modulação: Foi evidênciado como que estabelecer métodos menores e mais unitários em suas funcionalidades é importante para ter uma clareza do que o código faz e facilitar sua manutenção.
b. Refatoração com teste: A realização de pequenas mudanças no código com realização de testes durante o processo ajuda a evitar bugs e comportamentos inesperados.
c. Nomes Significantes:  Depois de modularizar o código em métodos menos, nomear os mesmos com significados claros é importante para o entendimento do código por pessoas novas que possam vir a trabalhar neste código.
