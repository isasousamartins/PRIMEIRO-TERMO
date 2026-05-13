# 🌐 Plano de Aula: Arquitetura IoT e Dispositivos de Redes

## 1. Fundamentos e Dispositivos de Redes
### Ativos de Redes
* **Definição:** Equipamentos que processam dados e gerenciam o tráfego ativamente.
* **Exemplos:** Roteadores, switches gerenciáveis, pontos de acesso (Access Points) e gateways.
* **Papel na IoT:** Direcionam os pacotes de dados dos sensores até os servidores.

### Passivos de Redes
* **Definição:** Componentes físicos que apenas transportam ou organizam os sinais elétricos/ópticos.
* **Exemplos:** Cabos de par trançado, fibra óptica, racks, patch panels e conectores RJ-45.
* **Papel na IoT:** Garantem a infraestrutura física estável para a conexão dos ativos.

---

## 2. A Internet e suas Derivações na IoT
### Evolução da Rede
* **Internet Tradicional:** Conexão focada em computadores, servidores e interação humana.
* **Intranet:** Rede privada restrita a uma organização para controle local de dispositivos.
* **Extranet:** Extensão segura da intranet permitindo acesso externo controlado a parceiros.

### Derivações Específicas para IoT
* **IIoT (IoT Industrial):** Foco em automação de fábricas, redes de alta confiabilidade e baixa latência.
* **IoMT (IoT Médica):** Dispositivos de saúde conectados com foco em segurança crítica de dados.
* **Redes LPWAN:** Redes de longo alcance e baixo consumo (ex: LoRaWAN, NB-IoT) derivadas para sensores.

---

## 3. Hardware IoT: O Microcontrolador ESP32
### Arquitetura do Dispositivo
* **Hardware:** Processador Xtensa Dual-Core de 32 bits com conectividade Wi-Fi e Bluetooth nativa.
* **Periféricos:** Pinos GPIO, conversores ADC/DAC, interfaces SPI, I2C e UART para sensores.

### Drivers e Instalação
* **Driver USB-UART:** Necessário para traduzir a comunicação USB do computador para a placa (ex: CP210x ou CH340).
* **Ambiente de Desenvolvimento:** Configuração da IDE (Arduino IDE ou VS Code + PlatformIO) com o core do ESP32.
* **Firmware:** Estrutura básica de inicialização do driver e conexão automática à rede sem fio local.

---

## 4. Comunicação IoT com o Protocolo MQTT
### Arquitetura Publish/Subscribe
* **Conceito:** Protocolo de mensagens leve e de baixo consumo, ideal para redes instáveis ou saturação de dados.
* **Componentes Principais:**
  * **Broker:** Servidor central que recebe e distribui todas as mensagens (ex: Mosquitto, HiveMQ).
  * **Publisher:** Dispositivo IoT (como o ESP32) que publica dados em um tópico específico.
  * **Subscriber:** Aplicação ou dispositivo que assina um tópico para receber os dados gerados.

### Tópicos e Qualidade de Serviço (QoS)
* **Estrutura de Tópicos:** Organização hierárquica por barras (ex: `casa/sala/temperatura`).
* **Níveis de QoS:**
  * **QoS 0:** Entrega no máximo uma vez (sem confirmação).
  * **QoS 1:** Entrega pelo menos uma vez (garante o recebimento, pode duplicar).
  * **QoS 2:** Entrega exatamente uma vez (mecanismo mais seguro e pesado).
