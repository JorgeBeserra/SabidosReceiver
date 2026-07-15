# Checklist antes da fabricação

## Esquemático

- [ ] ERC executado sem erros não justificados.
- [ ] Todas as folhas hierárquicas abrem corretamente.
- [ ] PT2322-S conferido pino a pino com o datasheet e com o componente físico.
- [ ] Polaridade de todos os eletrolíticos conferida.
- [ ] Pinagem e orientação de todos os conectores conferidas.
- [ ] Barramento I²C validado entre 3,3 V e 8 V.
- [ ] Pull-ups do I²C revisados e documentados.
- [ ] Entradas não utilizadas possuem tratamento definido.
- [ ] Pontos de teste adicionados para `+12V`, `+8V`, `+5V`, `+3V3`, GND, SDA e SCL.

## PCB

- [ ] DRC executado sem erros não justificados.
- [ ] Footprint do PT2322-S validado em impressão 1:1.
- [ ] Footprint do módulo ESP32 medido no hardware real.
- [ ] Antena do ESP32 sem cobre nas duas camadas e afastada de metal.
- [ ] LM2596 afastado das entradas e trilhas de áudio.
- [ ] Correntes de retorno da fonte não atravessam a região analógica.
- [ ] Plano de terra contínuo e sem gargalos.
- [ ] Trilhas de alimentação dimensionadas para a corrente prevista.
- [ ] Cobre afastado da borda conforme a capacidade da fabricante.
- [ ] Furos de montagem e áreas mecânicas conferidos.
- [ ] Serigrafia não cobre pads e indica polaridade/pino 1.

## Arquivos de produção

- [ ] Gerbers regenerados a partir da revisão aprovada.
- [ ] Arquivo de furação regenerado.
- [ ] Gerbers inspecionados em visualizador independente.
- [ ] Camadas, espessura e acabamento definidos.
- [ ] BOM revisada.
- [ ] Arquivo de posição revisado, quando houver montagem automática.
- [ ] Revisão da placa gravada na serigrafia.
- [ ] Hash ou tag Git da versão de fabricação registrado.
