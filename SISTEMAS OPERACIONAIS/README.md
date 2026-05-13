# 🖥️ Plano de Aula: Sistemas Operacionais e Segurança Cibernética

## 1. Introdução aos Sistemas Operacionais
### Conceitos Fundamentais
* **Função Principal:** Intermediar a comunicação entre o hardware e os softwares aplicativos.
* **Gerenciamento de Recursos:** Controle de memória RAM, tempo de CPU, processos e armazenamento.
* **Tipos de Interface:** GUI (Interface Gráfica do Usuário) e CLI (Interface de Linha de Comando).

### Indicações e Ecossistemas Atuais
* **Desktop e Produtividade:** Microsoft Windows (ampla compatibilidade) e macOS (ecossistema fechado/design).
* **Servidores e Infraestrutura:** Distribuições Linux (estabilidade e código aberto).
* **Dispositivos Móveis:** Android (baseado em Linux) e iOS (baseado em Unix).

---

## 2. Ecossistema Linux e Windows
### Distribuições Linux (Distros)
* **Debian/Ubuntu:** Foco em estabilidade, facilidade de uso e grande comunidade de suporte.
* **Red Hat (RHEL) / Rocky Linux:** Padrão corporativo voltado para servidores de missão crítica.
* **Alpine Linux:** Ultramínimo e leve, amplamente utilizado em containers Docker.
* **Kali Linux:** Distro especializada e pré-configurada para testes de invasão e auditoria.

### Ecossistema Windows
* **Windows Client:** Versões domésticas e corporativas focadas no usuário final (Windows 10 e 11).
* **Windows Server:** Sistema otimizado para serviços de rede, Active Directory e virtualização Hyper-V.
* **Arquitetura:** Baseada no kernel NT com suporte a sistemas de arquivos NTFS.

---

## 3. Operação do Windows via CLI (Linha de Comando)
### Interfaces de Terminal
* **Prompt de Comando (CMD):** Terminal legado baseado no MS-DOS para tarefas simples.
* **PowerShell:** Ambiente de automação baseado em objetos e no framework .NET.

### Comandos Essenciais de Administração
* **Navegação e Arquivos:**
  * `cd`: Altera o diretório atual de trabalho.
  * `dir`: Lista arquivos e pastas do diretório.
  * `mkdir` / `rmdir`: Cria e remove diretórios.
* **Diagnóstico de Rede:**
  * `ping`: Testa a conectividade de rede com um host.
  * `ipconfig`: Exibe as configurações de IP das interfaces de rede.
  * `netstat`: Mostra conexões de rede ativas e portas abertas.
* **Gestão do Sistema:**
  * `tasklist`: Lista todos os processos em execução.
  * `taskkill`: Encerra um processo por ID ou nome.

---

## 4. Fundamentos de Segurança Cibernética
### Princípios de Proteção no S.O.
* **Tríade CIA:** Confidencialidade (segredo), Integridade (exatidão) e Disponibilidade (acesso).
* **Princípio do Menor Privilégio:** Usuários devem ter apenas as permissões necessárias para suas funções.
* **Controle de Acesso:** Uso de contas locais separadas de contas de Administrador/Root.

### Ameaças Comuns e Mitigação
* **Malware:** Engenharia social, vírus, cavalos de troia e ransomware.
* **Mecanismos de Defesa:**
  * **Hardening:** Desativação de serviços, portas e recursos desnecessários no S.O.
  * **Firewall:** Filtragem do tráfego de rede de entrada e saída.
  * **Atualizações (Patches):** Correção imediata de vulnerabilidades conhecidas no kernel.
