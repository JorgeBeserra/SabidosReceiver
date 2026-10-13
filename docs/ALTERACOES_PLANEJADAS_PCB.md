# Alterações planejadas para a PCB

As alterações abaixo devem ser aplicadas no KiCad com inspeção visual e DRC:

1. Keepout de cobre sob e à frente da antena do ESP32.
2. Reposicionamento do LM2596 para longe das entradas e saídas de áudio.
3. Trilhas de 12 V e alimentação do LM2596 com largura mínima de 1 mm.
4. Pontos de teste para 3V3, 5V, 8V, GND, SDA e SCL.
5. Capacitor cerâmico de 100 nF junto ao VCC do PT2322-S.
6. Capacitor de reserva de 220 µF a 470 µF junto ao ESP32.
7. Proteção de entrada com fusível e inversão de polaridade para uso residencial; avaliar TVS para surtos da fonte externa.
8. Serigrafia de todos os conectores, pinagens e revisão da placa.

Nenhuma dessas mudanças deve ser enviada para fabricação sem confirmação dos footprints físicos e execução de ERC/DRC.

## Nova seção PT2323

- Conferir dimensões físicas e atribuir o footprint de U3 (PT2323-S).
- Transferir J7..J10, C40..C47 e R46..R53 da folha Entradas Stereo.
- Posicionar os resistores série de 270 Ω junto ao seletor.
- Conferir os seis caminhos PT2323 → PT2322, principalmente a rede central corrigida.
- Corrigir GND, clearance, cobre na borda e courtyards identificados no DRC.
- Conciliar as 64 diferenças de paridade antes de fabricar.

Detalhes em [PT2323_INTEGRACAO.md](PT2323_INTEGRACAO.md).
