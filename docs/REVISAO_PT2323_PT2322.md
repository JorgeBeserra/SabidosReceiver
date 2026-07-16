# Revisão do caminho PT2323 → PT2322

## Arquitetura confirmada

O SabidosReceiver será utilizado em ambiente residencial como processador de áudio para home theater.

Fluxo de sinal:

```text
Entradas analógicas já definidas
        ↓
PT2323 — seleção de entrada
        ↓
PT2322 — volume, tonalidade, balanço e canais
        ↓
Saídas de linha
        ↓
Amplificadores de potência
```

As entradas existentes do PT2323 são consideradas corretas e não devem ser alteradas sem uma necessidade elétrica comprovada.

## Prioridades da revisão

### Ligação PT2323 → PT2322

- Manter as trilhas entre os dois CIs curtas e diretas.
- Evitar vias desnecessárias nesse trecho.
- Manter os canais com comprimentos e geometria semelhantes.
- Não passar SDA, SCL, alimentação chaveada ou sinais de display entre os dois CIs.
- Manter plano de GND contínuo sob o caminho analógico.
- Conferir a necessidade e o valor dos capacitores de acoplamento conforme os circuitos de aplicação dos dois componentes.

### Alimentação analógica

- Alimentar PT2323 e PT2322 pela mesma linha analógica regulada quando compatível com os dois componentes.
- Adicionar 100 nF cerâmico junto a cada pino de alimentação de cada CI.
- Adicionar pelo menos 10 µF de reserva próximo ao conjunto PT2323/PT2322.
- Evitar que a corrente do LM2596 ou do ESP32 retorne pelo mesmo caminho estreito do GND analógico.
- Manter o regulador e o conversor DC-DC fisicamente afastados das entradas e do caminho PT2323 → PT2322.

### Barramento I²C

- Confirmar os endereços de PT2323 e PT2322 antes de compartilhar o barramento.
- Usar conversão de nível adequada entre o ESP32 e o lado de alimentação dos CIs de áudio.
- Começar com pull-ups de 4,7 kΩ e manter possibilidade de ajuste para 10 kΩ.
- Posicionar os conversores de nível próximos aos CIs de áudio.
- Adicionar pontos de teste para SDA, SCL, 3V3, 5V, 8V e GND.

### Saídas para amplificadores

- Manter as saídas afastadas da fonte chaveada e da antena do ESP32.
- Identificar claramente FL, FR, C, SUB, SL e SR na serigrafia.
- Manter retorno de GND de cada conector de saída próximo ao caminho de retorno do respectivo canal.
- Evitar compartilhar trilhas estreitas de GND das saídas com display, ESP32 ou alimentação digital.

## Critérios de layout

- Entradas na borda da placa próximas ao PT2323.
- PT2323 próximo ao PT2322.
- PT2322 próximo aos conectores de saída.
- ESP32, display e IR fora do corredor analógico principal.
- LM2596 e entrada de alimentação na extremidade oposta às entradas analógicas.
- Antena do ESP32 na borda, com keepout de cobre nas duas camadas.

## Validação obrigatória

Antes de fabricar:

1. confirmar os encapsulamentos reais do PT2323 e PT2322;
2. atualizar a PCB a partir do esquemático;
3. executar ERC;
4. executar DRC;
5. conferir Gerbers visualmente;
6. imprimir footprints críticos em escala 1:1;
7. medir continuidade e ausência de curto entre as alimentações.
