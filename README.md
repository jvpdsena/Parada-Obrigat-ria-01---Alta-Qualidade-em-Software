# Agile Docs & Code Sprint

Projeto desenvolvido como atividade prática da disciplina de Alta Qualidade em Software, com o objetivo de aplicar conceitos de desenvolvimento ágil, documentação de software e testes unitários.

## Sobre o projeto

O projeto consiste em um conversor de moedas desenvolvido em Python. A aplicação permite realizar conversões entre Real brasileiro (BRL), Dólar americano (USD) e Euro (EUR).

Para fins didáticos, são utilizadas taxas de conversão pré-definidas.

## Objetivos

- Simular uma sprint de desenvolvimento;
- Utilizar o Trello para acompanhamento das atividades;
- Definir critérios de aceitação;
- Desenvolver um conversor de moedas;
- Produzir documentação técnica;
- Implementar testes unitários;
- Realizar revisão do código e da documentação.

## Tecnologias utilizadas

- Python
- unittest
- Git
- GitHub
- Trello
- Visual Studio Code

## Estrutura do projeto

```text
Parada Obrigatória 01 - Alta Qualidade em Software/
│
├── README.md
├── conversor.py
├── test_conversor.py
│
└── docs/
    ├── documentacao_tecnica.md
    └── revisao.md
```

## Como executar

No terminal, acesse a pasta do projeto e execute:

```bash
python conversor.py
```

O programa solicitará:

1. O valor a ser convertido;
2. A moeda de origem;
3. A moeda de destino.

### Exemplo

```text
=== Conversor de Moedas ===
Moedas disponíveis: BRL, USD e EUR
Digite o valor que deseja converter: 30
Digite a moeda de origem: USD
Digite a moeda de destino: BRL

30.00 USD = 150.00 BRL
```

## Testes unitários

Os testes foram desenvolvidos utilizando o framework `unittest`.

Para executá-los:

```bash
python -m unittest test_conversor.py -v
```

Foram implementados 10 testes unitários, contemplando cenários positivos e negativos.

Na execução realizada durante o desenvolvimento, todos os testes foram concluídos com sucesso.

```text
Ran 10 tests in 0.001s

OK
```

## Documentação

A documentação técnica completa está disponível em:

`docs/documentacao_tecnica.md`

O registro da revisão do projeto está disponível em:

`docs/revisao.md`

## Organização da sprint

O desenvolvimento foi organizado no Trello utilizando as listas:

- Backlog
- To Do
- In Progress
- Done

As tarefas foram movimentadas entre as listas conforme o andamento do desenvolvimento.

## Retrospectiva

A utilização do quadro permitiu visualizar as diferentes etapas necessárias para o desenvolvimento da aplicação e acompanhar o progresso das tarefas.

A definição dos critérios de aceitação antes da implementação também auxiliou no desenvolvimento dos testes unitários, pois os requisitos definidos puderam ser transformados em comportamentos verificáveis automaticamente.

A atividade demonstrou a importância de dividir o desenvolvimento em tarefas menores, documentar o software e utilizar testes automatizados para verificar seu funcionamento.

## Autor

João Vítor Sena