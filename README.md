# ☁️ **Weather Scraper e Envio de E-mails** ☁️

Este projeto é um web scraper desenvolvido em Python que opera inteiramente via terminal. Sua principal funcionalidade é acessar um site de previsão do tempo, coletar os dados meteorológicos mais recentes e enviá-los diariamente por e-mail.
Como o objetivo principal do projeto foi a prática de habilidades de web scraping e automação, optou-se pelo uso do Yopmail — um serviço de e-mail temporário — para facilitar os testes e o desenvolvimento, sem a necessidade de utilizar uma conta de e-mail pessoal ou profissional.

---

## 🔧 **Funcionalidades**

- **Coleta de dados meteorológicos**: Usa o Scrapy para extrair as previsões de tempo para os próximos 3 dias.
- **Envio automatizado de e-mail**: Envia as previsões para o e-mail inserido pelo usuário.
- **Automatização Diária**: O programa é agendado para rodar diariamente às 06:00 da manhã.

---

## 📙 **Estrutura do Projeto**

```
weather-scraper/
├── run_spider.py              # Arquivo que executa a spider Scrapy
├── app.py                     # Arquivo principal do projeto (scraping, envio de e-mail e agendamento)
├── weather_spider.py          # Spider do Scrapy para coletar os dados do site de previsão
├── requirements.txt           # Dependências necessárias para executar o projeto
└── README.md                  # Documentação do projeto
```

---

## 🔄 **Instalação e Configuração**

### **1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/info-clima.git
cd info-clima
```

### **2. Crie um ambiente virtual e ative**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / MacOS
source venv/bin/activate
```

### **3. Instale as dependências**
```bash
pip install -r requirements.txt
```
---

## ⏰ **Como Executar o Projeto**

### **1. Executar Manualmente**
Para iniciar a coleta e o envio de e-mails manualmente, execute o arquivo **main.py**:
```bash
python main.py
```
Você será solicitado a inserir um e-mail para receber as previsões.

### **2. Execução Diária Automática**
O agendamento já está configurado para rodar todos os dias às 06:00. Isso é feito através da biblioteca **schedule**.

---

## 📚 **Exemplo de Saída**

Quando o programa é executado, a seguinte saída aparece no terminal:
```
Iniciando coleta de dados...

Coleta concluída.

Data: 10/12/2024
Condição: Ensolarado
Máxima: 32°C
Mínima: 22°C

Email enviado com sucesso!
```
O corpo do e-mail será semelhante a:
```
    Prezados,

Segue abaixo a previsão do tempo para os próximos dias:
    
         Hoje 
Condição: Chuva fraca
Temperatura: Mínima de 23° e Máxima de 27°
    
    
         Amanhã 
Condição: Trovoada
Temperatura: Mínima de 22° e Máxima de 27°
    
    
         Quarta 
Condição: Chuva fraca
Temperatura: Mínima de 21° e Máxima de 25°
```

---

## ⚒️ **Tecnologias Utilizadas**
- **Python**
- **Scrapy**: Para coleta de dados de previsão do tempo.
- **Selenium**: Para automação de ações no site de e-mail.
- **Schedule**: Para automatizar a execução do programa diariamente.

---

## 📊 **Possíveis Melhorias**
- Substituir o **Yopmail** por provedores de e-mail mais seguros.
- Adicionar suporte a multiplos destinatários.

---

## ⚠️ **Atenção**
- O **Yopmail** é usado apenas para testes e não é seguro para e-mails de produção.
- Verifique a legislação sobre raspagem de dados (web scraping) antes de usá-lo em sites de terceiros.

---

## 🔧 **Contribuições**
Contribuições são bem-vindas! Se você quiser sugerir melhorias, abrir issues ou fazer pull requests, fique à vontade.

---

## ✅ **Licença**
Este projeto está licenciado sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais informações.

