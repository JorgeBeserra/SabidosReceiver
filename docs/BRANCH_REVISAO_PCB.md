# Branch de revisão eletrônica e PCB

Esta branch foi criada para concentrar as alterações de circuito e layout da próxima revisão do SabidosReceiver.

## Escopo

- concluir a migração interna do nome do projeto;
- revisar encapsulamento e pinagem do PT2322-S;
- revisar alimentação de 12 V, 8 V, 5 V e 3,3 V;
- revisar conversão de nível I²C;
- criar proteção de entrada para uso automotivo;
- revisar posicionamento do LM2596 e retornos de corrente;
- criar keepout da antena do ESP32;
- adicionar pontos de teste;
- revisar regras de trilhas e vias;
- executar ERC e DRC antes da fabricação.

As alterações de geometria e roteamento devem ser conferidas visualmente no KiCad antes do merge.
