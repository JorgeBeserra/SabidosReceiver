# Revisão eletrônica e PCB — SabidosReceiver V1

Este documento registra as alterações técnicas recomendadas antes da fabricação.

## Prioridade crítica

### PT2322-S

- Confirmar o encapsulamento físico e a pinagem do componente disponível.
- O footprint somente deve ser substituído depois da medição do CI real.
- Imprimir o footprint em escala 1:1 e conferir o componente sobre o papel.

### Folhas hierárquicas

- `display.kicad_sch` e `Ir.kicad_sch` estão vazias na versão atual.
- Não atualizar a PCB a partir do esquemático enquanto não for decidido se esses circuitos serão recuperados dos arquivos legados ou removidos.

## Alimentação

- Manter a fonte chaveada LM2596 fisicamente afastada das entradas e saídas de áudio.
- Criar retorno de corrente curto entre entrada de 12 V, LM2596 e conector de alimentação.
- Não permitir que o retorno do conversor atravesse a região do PT2322-S.
- Adicionar desacoplamento local próximo ao PT2322-S: 100 nF cerâmico em paralelo com 10 µF na alimentação de 8 V.
- Adicionar desacoplamento próximo ao ESP32: 100 nF cerâmico e capacitor de reserva entre 220 µF e 470 µF na linha de 5 V.
- Manter o LM78M08 com área de cobre suficiente para dissipação térmica.

## I²C e conversão de nível

- Manter os 2N7002 próximos ao PT2322-S.
- Usar pull-ups inicialmente de 4,7 kΩ em 3,3 V e 8 V; deixar footprints compatíveis com 10 kΩ para ajuste.
- Manter SDA e SCL curtos, paralelos somente por pequenos trechos e afastados das entradas analógicas.
- Adicionar pontos de teste para SDA, SCL, 3V3, 5V, 8V e GND.

## Áudio

- Separar fisicamente conectores de entrada, processamento e conectores de saída.
- Evitar trilhas de áudio paralelas às trilhas de alimentação chaveada.
- Usar plano de GND contínuo; não criar divisões de terra que obriguem sinais a atravessar fendas.
- Fazer o retorno dos conectores de áudio chegar à região do PT2322-S sem compartilhar caminhos estreitos com ESP32, display ou fonte.
- Manter os capacitores de acoplamento próximos aos respectivos pinos do PT2322-S.

## ESP32

- Manter a antena na borda da PCB.
- Criar keepout sem cobre nas duas camadas sob a antena e à frente dela.
- Evitar componentes metálicos, cabos e conectores sobre a região da antena.
- Conferir o footprint do módulo físico antes da fabricação.

## Proteção e manutenção

- Adicionar proteção contra inversão de polaridade na entrada de 12 V.
- Adicionar fusível ou polyfuse dimensionado para a placa.
- Adicionar TVS na entrada de 12 V quando a placa for usada em ambiente automotivo.
- Identificar todos os conectores na serigrafia com função e pinagem.
- Adicionar revisão da placa e nome `SabidosReceiver` na serigrafia.

## Regras mínimas sugeridas

- trilha de sinal: 0,25 mm ou maior;
- alimentação de baixa corrente: 0,50 mm ou maior;
- entrada de 12 V e alimentação do LM2596: 1,0 mm ou maior;
- cobre até a borda: pelo menos 0,30 mm;
- vias comuns: diâmetro de 0,60 mm e furo de 0,30 mm ou maiores;
- evitar ilhas de cobre sem conexão.

## Estado

Este documento não autoriza fabricação por si só. O projeto somente deve ser liberado depois de ERC, DRC, conferência física dos footprints e inspeção visual dos Gerbers.
