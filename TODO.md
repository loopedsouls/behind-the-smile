# TODO.md - Jogo Behind the Smile

## Dia 1
- [x] Colocar áudio de despertador na cena inicial
  - `audio/alarm-clock-90867.mp3` ✓
- [ ] Mostrar imagem do uniforme pendurado e da máscara
  - `add img uniform_hanging.jpg`
- [x] Espelho reflete um estranho: imagem do homem de terno com olheiras colocando a máscara (igual ao da capa)
  - Placeholder adicionado: `bg mirror_putting_mask`
- [x] Cena "Mantenha o sorriso": personagem atrás do balcão com a máscara, pronto para atender clientes
  - Placeholder adicionado: `bg behind_counter_masked`
- [x] Saída para a rua: inserir imagem conforme descrição
  - Placeholder adicionado: `bg street_neon_dystopia`
- [x] Chegada à conveniência: adicionar neon "Sorria, você está sendo observado"
  - Placeholder adicionado: `bg store_neon_sign`
- [x] Entrada: mostrar corredor com prateleiras e balcão vazio ao fundo
  - Placeholder adicionado: `bg store_entrance`
- [ ] Atender clientes:
  - [ ] Ação violenta na parte negativa (ex.: tela escurece com berro do atendente → game over no monstro com pernas de aranha)
    - `add audio scream_horror.mp3`
    - `add img spider_legs_monster.jpg`
  - [ ] Definir ações específicas para outros monstros
    - `add audio bizarre_sound.mp3`
    - `add audio angry_growl.mp3`
    - `add audio robot_beep.mp3`
  - [ ] Adicionar sons para os monstros
    - `add audio vip_footsteps.mp3`
    - `add audio paranoid_whisper.mp3`
- [ ] Animações ocasionais no cenário (ex.: goteira pingando)
  - `add audio dripping_water.mp3`
- [ ] Som de caixa registradora quando algum monstro comprar algo
  - `add audio cash_register.mp3`

## Dias seguintes (Dia 2, Dia 3, Dia 4, Dia 5)
- [x] Início novamente no quarto
  - `audio/alarm-clock-90867.mp3` (reutilizado) ✓
  - Placeholder adicionado: `bg waking_in_pain`, `bg bedroom_day2`, `bg day4_deteriorated`
- [ ] Tela de desempenho: janela com resultados
  - Placeholder adicionado: `bg performance_report`
- [ ] Adicionar transição entre os dias
  - Estrutura de dias criada ✓

### Dia 2 Específico
- [x] Cliente olhando: mostrar cara sinistra
  - Placeholder adicionado: `bg creepy_customer`
- [ ] Telefone tocando à noite: imagem/áudio
  - `add audio phone_ringing_distorted.mp3`

### Dia 3 Específico
- [x] Bilhete misterioso na porta
  - Placeholder adicionado: `bg mysterious_note`

### Dia 4 Específico
- [ ] Scanner de produtos falhando
  - `add audio scanner_glitch.mp3`
- [x] Café com gosto de metal
  - Placeholder adicionado: `bg corrupted_coffee`

### Dia 5 Específico (Clímax)
- [x] Cidade em caos: imagem deteriorada
  - Placeholder adicionado: `bg city_chaos`
- [x] Máscaras caídas nas ruas
  - Placeholder adicionado: `bg fallen_masks`

## Elementos adicionais

### UI Elements
- [ ] Café: imagem de uma xícara de café
  - `add img coffee_cup.jpg`
- [ ] Carimbo: imagem do carimbo
  - `add img stamp_icon.jpg`
- [ ] Diagnóstico do sistema: imagem representando sistema
  - `add img system_diagnostic.jpg`
- [ ] Protocolo: imagem correspondente
  - `add img protocol_screen.jpg`

### Cenas Narrativas
- [x] Dormir inquieto: imagem de pesadelo + som de gritos
  - Placeholder adicionado: `bg nightmare_surreal` ✓
  - Som ambiente reutilizado: `audio/ambiente.mp3`
- [x] Alarme toca novamente: personagem sentado na cama com expressão de dor
  - Placeholder adicionado: `bg waking_in_pain` ✓
- [x] Dia em que está pior: imagem dele com a máscara e aparência deteriorada
  - Placeholder adicionado: `bg day4_deteriorated` ✓
- [x] Dorme com a máscara na frente: adicionar imagem
  - Placeholder adicionado: `bg mask_on_nightstand` ✓

### Ambient Sounds
- [ ] Som da cafeteira para dar mais vida
  - `add audio coffee_machine.mp3`
- [ ] Fluorescent lights humming
  - `add audio fluorescent_hum.mp3`
- [ ] Clock ticking
  - `add audio clock_ticking.mp3`

---

## Observações
- Sons e imagens devem ser consistentes com a estética sombria do jogo.
- Transições entre dias devem reforçar a atmosfera de desgaste psicológico.
- Cada monstro deve ter comportamento e áudio próprios para aumentar a imersão.
- Placeholders: `add img [nome]` para imagens, `add audio [nome]` para áudios
