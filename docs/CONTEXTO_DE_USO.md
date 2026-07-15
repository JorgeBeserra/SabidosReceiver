# Contexto de uso — SabidosReceiver

O SabidosReceiver será utilizado em ambiente residencial, como processador de áudio para home theater.

## Cadeia de sinal prevista

1. TV com saída digital S/PDIF;
2. conversor externo S/PDIF para áudio analógico multicanal;
3. entradas analógicas do SabidosReceiver;
4. processamento e controle de volume pelo PT2322-S;
5. saídas para amplificadores de potência do sistema de caixas acústicas.

## Consequências para o projeto

- a alimentação não precisa atender transientes automotivos;
- não é necessária TVS automotiva nem proteção específica contra load dump;
- continuam recomendados fusível, proteção contra inversão de polaridade e filtragem de entrada;
- a prioridade passa a ser baixo ruído, baixa ondulação da alimentação, aterramento adequado e redução de interferência da fonte chaveada;
- o LM2596 deve permanecer fisicamente afastado das entradas analógicas e do PT2322-S;
- conectores de entrada devem ser identificados conforme os canais entregues pelo conversor S/PDIF;
- o gabinete deve prever ventilação, aterramento e separação física entre fonte, circuito de sinal e amplificadores.

## Premissa elétrica

A entrada prevista é uma fonte DC regulada de 12 V para uso interno. A corrente necessária deve ser confirmada considerando ESP32, display, PT2322-S, relés e demais periféricos; os amplificadores de potência devem preferencialmente usar alimentação própria.
