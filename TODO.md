# Behind the Smile - Lista TODO

Baseado no README.md e no código atual, esta é uma lista detalhada do que já foi implementado e o que ainda falta para alcançar a visão completa do jogo.

## ✅ **JÁ IMPLEMENTADO**

### **Estrutura Básica**
- Sistema de estados do jogo (menu, playing, paused, game_over)
- Loop de jogo com timer de 90 segundos
- Spawn aleatório de clientes e perigos baseado em raridade/severidade
- Sistema de dificuldade progressiva (multiplier aumenta com tempo)

### **Mecânica de Máscara**
- Toggle da máscara via teclado (Z) - agora com movimento por mouse
- Detecção de "olhar" do cliente (game over se máscara baixa quando olha)
- Overlay visual da máscara no HUD (segue mouse com clamp)
- Estados visuais do jogador (normal, alert, infected)
- Barra de estabilidade do braço com tremor visual

### **Clientes e Perigos**
- 7 tipos de funcionários com linhas de diálogo, paciência e pontos
- 9 tipos de perigos com tempo de resolução e pontos
- Sistema de spawn com timers e notificações

### **Interface e Telas**
- Tela de menu com efeito glitch
- Tela de game over com estatísticas
- Tela de pausa e ajuda de controles
- Diálogo de cliente com efeito typewriter
- Backgrounds dinâmicos (mudam com status e perigos)
- Barra de estabilidade do braço

### **Lore e Narrativa**
- História completa implementada (Cordyceps-7, infecção, máscaras)
- Sistema de narração com personagem "narrator_dystopia"

### **Assets Básicos**
- Backgrounds para loja e perigos
- Sprites de funcionários (monstro, alien, he, she)
- Música ambiente e efeitos básicos

## ❌ **AINDA FALTA IMPLEMENTAR**

### **Mecânica Principal (Crítica)**
- ✅ **Controle por mouse**: Mover máscara fisicamente na tela (clamp para área do rosto)
- ✅ **Tremor da mão**: Sistema de fadiga com barra de estabilidade e tremor visual
- **Tarefas burocráticas**: Bipar produtos, carimbos, café (atual só atende/resolve)
- **Relógio digital**: Contador visual do tempo restante

### **Narrativa Ambiental**
- **Anúncios da Gerência**: Voz automática com anúncios
- **Mudanças no cenário**: Luzes piscando, elementos dinâmicos
- **Narrativa procedural**: História baseada em ações

### **Arte e Visual**
- **Pixel art completa**: Sprites procedurais, protagonista detalhado
- **Animações**: Respiração, fade, screen shake
- **Efeitos visuais**: Glitch, luzes, polimento geral

### **Áudio**
- **Trilha mallsoft**: Música distorcida de elevador
- **Efeitos sonoros**: Zumbido, papel, rosnados
- **Voz da Gerência**: Anúncios narrativos

### **Progressão**
- **Sistema de turnos**: 5 noites com dificuldade crescente
- **Clientes avançados**: Comportamentos específicos e padrões
- **Gestão de inventário**: Bipar itens na ordem certa

### **Polimento**
- **HUD completo**: Reativar timer, status, pontuação
- **Correção de bugs**: Resolver erros de lint
- **Exportação**: Para web e PC

## 📋 **PRÓXIMOS PASSOS RECOMENDADOS**

1. **Implementar controle por mouse** para mover a máscara
2. **Adicionar tarefas interativas** (bipar produtos, etc.)
3. **Criar barra de estabilidade** do braço
4. **Desenvolver arte pixel art** completa
5. **Implementar anúncios da Gerência**
6. **Adicionar efeitos sonoros** e trilha mallsoft
7. **Sistema de turnos/noites**
8. **Polimento visual** (screenshake, glitch)

## 📊 **STATUS GERAL**
- **Implementado**: ~50% (mecânicas core adicionadas)
- **Falta**: ~50% (tarefas e polimento)
- **Prioridade**: Tarefas burocráticas e relógio digital