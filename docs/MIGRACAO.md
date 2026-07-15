# Migração SabVolAudio → SabidosReceiver

Este documento controla a migração do projeto sem apagar circuitos ainda não conferidos.

## Estado atual

- [x] Arquivos principais renomeados para `SabidosReceiver`.
- [x] Netlist antiga removida.
- [x] Preferências locais `.kicad_prl` removidas do versionamento.
- [x] Backups, Gerbers e arquivos temporários ignorados.
- [ ] Identificador interno do projeto atualizado em todos os arquivos KiCad.
- [ ] Referências `sheetfile "SabVolAudio.kicad_sch"` eliminadas da PCB.
- [ ] Folha `display.kicad_sch` recuperada ou removida conscientemente.
- [ ] Folha `Ir.kicad_sch` recuperada ou removida conscientemente.
- [ ] Bibliotecas locais renomeadas e validadas.
- [ ] Modelos 3D migrados para caminhos `${KIPRJMOD}`.
- [ ] Arquivos legados removidos após comparação visual.

## Procedimento seguro no KiCad

1. Criar uma cópia externa da pasta do projeto.
2. Abrir `SabidosReceiver.kicad_pro` no KiCad 10.
3. Abrir cada folha hierárquica e salvar.
4. Comparar `display.sch` com `display.kicad_sch`.
5. Comparar `Ir.sch`, quando existir, com `Ir.kicad_sch`.
6. Recuperar os circuitos ausentes antes de excluir os arquivos antigos.
7. Executar **Ferramentas → Atualizar PCB a partir do esquemático**.
8. Não aceitar remoções automáticas sem conferir referência por referência.
9. Salvar o esquemático e a PCB.
10. Fechar e reabrir o projeto para confirmar os vínculos.

## Critério para apagar arquivos legados

Um arquivo antigo só pode ser removido quando:

- o circuito equivalente existir no formato atual;
- a comparação visual estiver concluída;
- nenhum símbolo ou footprint depender da biblioteca antiga;
- o ERC não acusar folhas ou símbolos ausentes;
- a atualização da PCB não remover componentes válidos;
- o DRC não apresentar conexões pendentes provocadas pela migração.

## Comando de auditoria

Execute na raiz do repositório:

```bash
bash scripts/auditar-projeto.sh
```

O script procura referências antigas, caminhos absolutos e folhas hierárquicas aparentemente vazias.
