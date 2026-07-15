# SabidosReceiver

Projeto de receptor e processador de áudio multicanal baseado no **PT2322-S**, controlado por um **ESP32**.

## Ferramenta

O projeto principal está em formato **KiCad 10**:

- `SabidosReceiver.kicad_pro`
- `SabidosReceiver.kicad_sch`
- `SabidosReceiver.kicad_pcb`

Abra sempre o arquivo `SabidosReceiver.kicad_pro` para manter o esquemático e a PCB associados ao mesmo projeto.

## Situação da migração

O projeto foi renomeado de `SabVolAudio` para `SabidosReceiver`. Ainda existem arquivos e identificadores legados preservados no repositório para conferência durante a migração.

Antes de removê-los definitivamente, é necessário confirmar que todas as folhas hierárquicas e todos os componentes foram convertidos corretamente para o formato atual do KiCad.

## Cuidados antes da fabricação

1. Confirmar fisicamente o encapsulamento do PT2322-S e validar o footprint em escala 1:1.
2. Abrir e salvar todas as folhas hierárquicas no KiCad 10.
3. Executar o ERC no esquemático.
4. Atualizar a PCB a partir do esquemático e revisar cada inclusão ou remoção proposta.
5. Executar o DRC na PCB.
6. Conferir a região da antena do ESP32 e manter cobre afastado.
7. Conferir polaridade dos capacitores eletrolíticos e pinagem de todos os conectores.
8. Gerar novos Gerbers somente depois da validação.

## Organização recomendada

- Arquivos `.kicad_*`: fontes atuais do projeto.
- Bibliotecas locais: símbolos e footprints necessários para abrir o projeto em outro computador.
- Modelos 3D: devem usar caminhos relativos com `${KIPRJMOD}`.
- Gerbers, backups, netlists e preferências locais não devem ser versionados.

## Observação importante

Os arquivos legados não devem ser apagados sem comparação visual com o esquemático atual, porque algumas folhas convertidas aparecem vazias e podem ainda depender do conteúdo antigo.
