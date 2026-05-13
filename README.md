# PRIMEIRO-TERMO
Material de aluno para o 1 Termo - LOPAL - SOP - ARI - LER 

## LOPAL
Lógica de programação em Python

##SOP
Sistemas operacionais

# 🎓 Plano de Ensino Unificado: Tecnologia, Desenvolvimento e Infraestrutura

---

## 📝 1. Engenharia de Requisitos

### Unidade 1: Introdução e Tipos de Requisitos
#### 1.1 Requisitos Funcionais (RF)
* **Conceito:** Funcionalidades que o sistema deve executar obrigatoriamente.
* **Mapeamento:** Entradas, processamentos e saídas esperadas pelo usuário.
* **Exemplos:**
  * O sistema deve permitir o cadastro de novos clientes.
  * O sistema deve emitir relatórios de vendas mensais em PDF.

#### 1.2 Requisitos Não Funcionais (RNF)
* **Conceito:** Restrições, propriedades de qualidade e características do sistema.
* **Categorias:** Desempenho, segurança, usabilidade, confiabilidade e portabilidade.
* **Exemplos:**
  * O sistema deve carregar qualquer página em menos de 2 segundos.
  * As senhas dos usuários devem ser armazenadas com hash criptográfico.

### Unidade 2: Técnicas de Elicitação de Requisitos
#### 2.1 Brainstorming
* **Análise:** Sessões criativas com a equipe para descobrir escopos ocultos.
* **Regras:** Proibição de críticas iniciais e foco na quantidade de ideias.

#### 2.2 Entrevistas
* **Estruturadas:** Perguntas fechadas e roteiro rígido para dados exatos.
* **Não Estruturadas:** Conversa aberta para entender o fluxo de negócios do cliente.

#### 2.3 Prototipagem
* **Baixa Fidelidade:** Wireframes em papel ou digitais simples (foco no fluxo).
* **Alta Fidelidade:** Protótipos interativos (Figma/Adobe XD) idênticos ao produto final.

### Unidade 3: Modelagem e Relatórios Técnicos
#### 3.1 Diagramas UML de Requisitos
* **Casos de Uso:** Atores, o sistema e as interações principais.
* **Diagrama de Atividades:** Fluxograma do processo de negócio.

#### 3.2 Relatórios Técnicos (SRS)
* **Estrutura Padrão:** Introdução, Descrição Geral, Requisitos Específicos e Apêndices.

---

## 🐍 2. Lógica de Programação com Python

### Unidade 1: Lógica Básica em Python
#### 1.1 Variáveis e Operadores
* **Tipos Dinâmicos:** Uso de `str`, `int`, `float` e `bool` sem declaração explícita.
* **Operadores:** Aritméticos (`+`, `-`, `*`, `/`, `//`, `%`) e lógicos (`and`, `or`, `not`).

#### 1.2 Estruturas de Controle e Coleções
* **Condicionais:** Desvios de fluxo com `if`, `elif` e `else`.
* **Laços:** Repetições controladas com `while` e iterações em coleções com `for`.
* **Estruturas de Dados:** Mandato e manipulação avançada de listas, tuplas e dicionários.

### Unidade 2: Git e GitHub (Controle de Versão)
#### 2.1 Git Local
* **Fluxo:** `git init` -> `git add .` -> `git commit -m "mensagem"`.
* **Histórico:** Uso do `git log` para rastrear alterações e autores.

#### 2.2 GitHub Remoto
* **Comandos:** `git push` (enviar), `git pull` (atualizar) e `git clone` (baixar).
* **Colaboração:** Resolução de conflitos de código e abertura de Pull Requests.

### Unidade 3: Clean Code e Projetos
#### 3.1 Princípios de Código Limpo
* **Legibilidade:** Regras da PEP 8 (indentação com 4 espaços, nomes em snake_case).
* **Funções:** Princípio da responsabilidade única (funções pequenas que fazem uma só coisa).

#### 3.2 Desenvolvimento de Projetos
* **Prática:** Criação de aplicações modulares documentadas com um arquivo `README.md`.

---

## 🌐 3. Arquitetura IoT e Dispositivos de Redes

### Unidade 1: Infraestrutura de Redes de Computadores
#### 1.1 Ativos de Rede
* **Componentes:** Roteadores, Switches, Gateways Residenciais e Access Points.
* **Função:** Processamento de pacotes, roteamento de pacotes IP e gerenciamento de rede.

#### 1.2 Passivos de Rede
* **Componentes:** Cabos UTP (Par Trançado), conectores RJ-45, Patch Panels e Racks.
* **Função:** Meio físico de transmissão sem interferência nas decisões de dados.

#### 1.3 Derivações da Internet
* **Tipologias:** Intranet (rede interna) e Extranet (acesso externo seguro).
* **Segmentações IoT:** IIoT (Industrial) e IoMT (Médica).

### Unidade 2: Hardware IoT - ESP32
#### 2.1 Arquitetura do Microcontrolador
* **Especificações:** Chip Xtensa Dual-Core, Wi-Fi e Bluetooth integrados.
* **Interfaces:** Uso de pinos GPIO (Entradas/Saídas), barramentos I2C, SPI e UART.

#### 2.2 Drivers e Ambiente
* **Instalação:** Configuração de drivers USB-UART (CH340/CP210x) no computador.
* **Firmware:** Estrutura de código para conexão em redes Wi-Fi locais.

### Unidade 3: Protocolo MQTT
#### 3.1 Arquitetura Publish/Subscribe
* **Elementos:** Broker (servidor), Publisher (sensores) e Subscriber (aplicativos).
* **Vantagens:** Protocolo extremamente leve, ideal para redes instáveis.

#### 3.2 Tópicos e QoS
* **Sintaxe:** Uso de tópicos hierárquicos separados por barras (`/`).
* **Níveis de Qualidade:** QoS 0 (rápido), QoS 1 (garantido) e QoS 2 (exato).

---

## 🖥️ 4. Sistemas Operacionais e Segurança Cibernética

### Unidade 1: Sistemas Operacionais Modernos
#### 1.1 Ecossistema de S.O.
* **Mercado:** Diferenças estruturais entre arquiteturas Windows (Kernel NT) e Linux (Unix).
* **Distribuições Linux:**
  * **Ubuntu/Debian:** Uso geral e servidores acadêmicos.
  * **Alpine Linux:** Otimizado e ultraleve para containers.
  * **Kali Linux:** Focado em auditoria de segurança e pentest.

### Unidade 2: Operação via CLI (Windows)
#### 2.1 Prompt de Comando (CMD) e PowerShell
* **Navegação:** `cd`, `dir`, `mkdir`, `copy`, `del`.
* **Análise de Rede:** `ping`, `ipconfig /all`, `netstat -ano`.
* **Gerenciamento do S.O.:** `tasklist` e `taskkill /PID`.

### Unidade 3: Segurança Cibernética
#### 3.1 Fundamentos de Proteção
* **Tríade CIA:** Garantia de Confidencialidade, Integridade e Disponibilidade.
* **Políticas:** Controle de contas de usuário e Princípio do Menor Privilégio.

#### 3.2 Hardening e Defesa
* **Mecanismos:** Configuração avançada de regras de Firewall.
* **Mitigação:** Desativação de portas vulneráveis e aplicação sistemática de Patches.
