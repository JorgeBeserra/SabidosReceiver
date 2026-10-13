# Integração do PT2323-S

O esquemático recebido já continha o seletor PT2323-S como **U3**, entradas 5.1, filtro de subwoofer e resistores de saída. A PCB ainda não incorpora essa revisão do esquema.

## Alterações aplicadas no esquema

- Corrigida a rede `SELECTOR-CTO` para `SELECTOR-CT`: R35 agora chega ao C3 e ao canal central do PT2322.
- Criada a biblioteca local `PT2323.kicad_sym` e registrada em `sym-lib-table`.
- Corrigidos os tipos elétricos do símbolo conforme a pinagem: MIXO e REF são saídas; SDA/SCL, LPF_I e entradas R1..R4 são entradas.
- Adicionada a folha `entradas_estereo.kicad_sch`, com J7..J10, oito capacitores C40..C47 de 10 µF e oito resistores R46..R53 de 100 kΩ.
- Conectadas as oito entradas estéreo aos pinos 1..4 e 28..25 do U3. Redes PT1L/PT1R..PT4L/PT4R ligam a folha nova ao seletor.

J7 corresponde a Stereo 1; J8 a Stereo 2; J9 a Stereo 3; J10 a Stereo 4. Nos conectores propostos: **1=L, 2=GND, 3=R**. Os capacitores de entrada têm positivo voltado ao CI, polarizado pela referência interna. Os resistores de 100 kΩ ficam do lado da fonte de sinal.

## Áudio

| Canal | Saída U3 | Resistor série | Capacitor de entrada PT2322 | Entrada U2 |
| --- | --- | --- | --- | --- |
| FL | 22 / FLO | R37 | C1 | 11 / IN_FL |
| FR | 21 / FRO | R36 | C6 | 4 / IN_FR |
| CT | 20 / CTO | R35 | C3 | 9 / IN_CT |
| SUB | 19 / SUBO | R34 | C4 | 6 / IN_SUB |
| SL | 18 / SLO | R33 | C2 | 10 / IN_SL |
| SR | 17 / SRO | R20 | C5 | 5 / IN_SR |

Os seis resistores de 270 Ω exigidos pelo circuito de aplicação já existiam. Devem ficar junto às saídas do PT2323 na PCB. Os valores atuais R44/R45=24 kΩ, C38=47 nF e C39=18 nF correspondem ao exemplo de crossover próximo de 280 Hz do datasheet. Não alterei a frequência do filtro sem definir a resposta desejada das caixas.

## Alimentação e I2C

U3 compartilha **+8V**, **GNDD**, **SDA-HV-8V** e **SCL-HV-8V** com o PT2322. O firmware usa o barramento I2C principal do ESP32, 100 kHz. O PT2322 responde em 0x44; o PT2323 em 0x4A.

O datasheet V1.3 informa alimentação mínima de 4,5 V e típica de 9 V, portanto 8 V está acima do mínimo especificado; desempenho analógico deve ser confirmado nessa alimentação. Para VCC=8 V, VIH mínimo de 0,7×VCC equivale a 5,6 V: utilize o lado convertido de 8 V, mantendo SDA/SCL de 3,3 V separados no ESP32.

## Encapsulamento e PCB pendentes

Foi confirmado pelo usuário **PT2323-S SMD, SOP-28**. Ainda é necessário conferir largura/comprimento do corpo e distância entre terminais do CI adquirido. Há diferenças entre versões de documentação (SO 330 mil / SOP 300 mil); por isso o footprint de U3 continua deliberadamente sem atribuição. A descrição SOP-28 não basta para validar a geometria. Os footprints dos novos conectores e capacitores são propostas e também precisam corresponder aos componentes comprados.

Não atualizei o arquivo `SabidosReceiver.kicad_pcb`, não gerei Gerbers e não liberei fabricação. A migração do esquema para PCB exige conciliar folhas legadas, atribuir os footprints ausentes, posicionar e rotear a nova seção e corrigir as falhas abaixo.

## Validação realizada

O script `scripts/verificar-pt2323.py` exporta uma netlist KiCad e verifica os seis caminhos de saída, oito entradas estéreo, terras, alimentação e I2C. A renderização das folhas principal e nova foi inspecionada.

ERC antes: **60 ocorrências, 17 erros e 43 avisos**. ERC depois: **45 ocorrências, 5 erros e 40 avisos**. Os cinco erros restantes são preexistentes:

1. Pinos de folha SDA-HV-5V e SCL-HV-5V sem conexão na folha Processador.
2. U2/VREF definido como entrada de alimentação sem driver no símbolo legado.
3. Alimentação +3V3 sem driver identificado no trecho legado.
4. GNDD sem driver identificado na folha Processador.

Os avisos incluem diferenças entre símbolos cacheados e bibliotecas, bibliotecas de footprints, nomes de terra e um pequeno segmento de fio desconectado. Veja `docs/validacao/erc-resumo.json`.

O DRC da PCB existente, incluindo paridade com o esquema atualizado, encontrou **86 violações**, **3 conexões ausentes** e **64 diferenças de paridade**. Entre as diferenças: 49 footprints ausentes, 9 extras e 6 conflitos de rede; incluem inconsistências antigas e a seção nova ainda não transferida.

Problemas físicos que precisam ser resolvidos:

- Clearance de +5V com zona sem rede: 0,3968 mm onde a regra exige 0,508 mm, perto de (110,55; 143,55) mm.
- Zona de cobre sem rede junto à borda perto de (69,75; 92,85) mm, além de cobre isolado.
- Courtyards abertos em U1 e U2.
- Três conexões de GNDD ausentes, inclusive ao pino 17 do ESP32.
- Ponta de trilha desconectada em Net-(C2-+) perto de (97,324; 168,706) mm.

Antes da bancada: confirmar a geometria de U3, validar o conversor de nível e verificar alimentação/continuidade. Na bancada: selecionar uma fonte por vez com sinal de baixo nível, verificar os seis canais e os mutes, testar falhas de comunicação e reinício. Entrada 5.1 deve vir de um decodificador/conversor com seis saídas analógicas; o PT2323 expande estéreo de forma simulada e não decodifica S/PDIF/Dolby/DTS.

Fontes: [datasheet Princeton PT2323 V1.3](https://datasheet4u.com/pdf-down/P/T/2/PT2323_PrincetonTechnology.pdf), [circuito de aplicação V1.1](https://cdn.promelec.ru/upload/datasheet/9/5/PT2323.pdf).
