#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

status=0

printf 'Verificando referências legadas...\n'
legacy_matches=$(grep -RInE \
  --exclude-dir=.git \
  --exclude-dir=SabVolAudio-backups \
  --exclude='*.bak' \
  --exclude='*.sch' \
  --exclude='*.pro' \
  --exclude='*.net' \
  'SabVolAudio|SabVol' \
  -- *.kicad_pro *.kicad_sch *.kicad_pcb 2>/dev/null || true)

if [[ -n "$legacy_matches" ]]; then
  printf '%s\n' "$legacy_matches"
  printf '\nATENÇÃO: ainda existem identificadores legados nos arquivos atuais.\n'
  status=1
else
  printf 'Nenhuma referência legada encontrada nos arquivos atuais.\n'
fi

printf '\nVerificando caminhos absolutos de modelos e bibliotecas...\n'
absolute_paths=$(grep -RInE \
  --exclude-dir=.git \
  --include='*.kicad_*' \
  '([A-Za-z]:[/\\]|/home/|/Users/)' \
  . || true)

if [[ -n "$absolute_paths" ]]; then
  printf '%s\n' "$absolute_paths"
  printf '\nATENÇÃO: substitua caminhos locais por ${KIPRJMOD}/...\n'
  status=1
else
  printf 'Nenhum caminho absoluto encontrado.\n'
fi

printf '\nVerificando folhas hierárquicas vazias...\n'
for sheet in display.kicad_sch Ir.kicad_sch; do
  if [[ -f "$sheet" ]] && ! grep -qE '^\s*\((symbol|wire|junction|label|global_label|hierarchical_label)\b' "$sheet"; then
    printf 'ATENÇÃO: %s parece estar vazia.\n' "$sheet"
    status=1
  fi
done

exit "$status"
