# Alterações planejadas para a PCB

As alterações abaixo devem ser aplicadas no KiCad com inspeção visual e DRC:

1. Keepout de cobre sob e à frente da antena do ESP32.
2. Reposicionamento do LM2596 para longe das entradas e saídas de áudio.
3. Trilhas de 12 V e alimentação do LM2596 com largura mínima de 1 mm.
4. Pontos de teste para 3V3, 5V, 8V, GND, SDA e SCL.
5. Capacitor cerâmico de 100 nF junto ao VCC do PT2322-S.
6. Capacitor de reserva de 220 µF a 470 µF junto ao ESP32.
7. Proteção de entrada com fusível, inversão de polaridade e TVS para uso automotivo.
8. Serigrafia de todos os conectores, pinagens e revisão da placa.

Nenhuma dessas mudanças deve ser enviada para fabricação sem confirmação dos footprints físicos e execução de ERC/DRC.
