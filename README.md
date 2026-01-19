# 💼 Portfolio Rebalancer

> **Tax-efficient portfolio rebalancing tool with cash-only optimization**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

[English](#english) | [Italiano](#italiano)

---

## English

### 🎯 What is Portfolio Rebalancer?

Portfolio Rebalancer is a **free, open-source tool** that helps investors maintain their target asset allocation efficiently. Unlike traditional rebalancing that requires selling assets (triggering capital gains taxes), our **Cash-Only Rebalancing** feature optimizes new cash investments to bring your portfolio closer to target allocations.

### ✨ Features

#### Core Features (Free & Open Source)
- 🌍 **Global Asset Search** - Search stocks/ETFs via Yahoo Finance (100+ exchanges)
- 📊 **Visual Analytics** - Interactive charts showing current vs target allocation
- 💰 **Cash-Only Rebalancing** - Tax-efficient rebalancing without selling
- 📈 **Traditional Rebalancing** - Classic buy/sell recommendations
- 🔄 **Real-time Prices** - Automatic price updates via Yahoo Finance
- 📁 **Import/Export** - CSV support for portfolio management
- 🌐 **Bilingual** - English and Italian interface
- 🎨 **Professional UI** - Clean, modern interface with sidebar statistics

### 🚀 Quick Start

#### Try it Online
👉 **[Launch App](https://your-app-url.streamlit.app)** - No installation required!

#### Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/portfolio-rebalancer.git
cd portfolio-rebalancer

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### 📖 How to Use

1. **Set Target Allocation**
   - Define your target percentages (e.g., 80% Stocks, 20% Bonds)
   - Total must equal 100%

2. **Add Portfolio Items**
   - Search by ISIN, ticker, or name
   - Add quantity and let the app fetch current prices
   - Supports all Yahoo Finance markets

3. **Analyze Your Portfolio**
   - View current vs target allocation
   - See rebalancing recommendations
   - Use Cash-Only feature for tax-efficient investing

4. **Cash-Only Rebalancing**
   - Enter available cash to invest
   - Get optimized purchase plan
   - No selling = No capital gains taxes!

### 💡 Example Use Case

**Current Portfolio:** €10,000
- Stocks: 60% (Target: 80%)
- Bonds: 40% (Target: 20%)

**New Cash:** €2,000

**Traditional Rebalancing:** Sell €2,000 bonds → Pay capital gains tax 😞

**Cash-Only Rebalancing:** Buy €2,000 stocks → No taxes! 🎉

### 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** - Web framework
- **Pandas** - Data manipulation
- **Plotly** - Interactive visualizations
- **yfinance** - Market data
- **Yahoo Finance API** - Asset search

### 📋 Requirements

```
streamlit>=1.28.0
pandas>=2.0.0
yfinance>=0.2.28
plotly>=5.17.0
requests>=2.31.0
streamlit-option-menu>=0.3.6
matplotlib>=3.7.0
```

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 🙏 Acknowledgments

- Market data provided by [Yahoo Finance](https://finance.yahoo.com/)
- Built with [Streamlit](https://streamlit.io/)

### 📧 Contact

- [GitHub Discussions](https://github.com/prev-creator/portfolio-rebalancer/discussions)

### ⭐ Star History

If you find this project useful, please consider giving it a star!

---

## Italiano

### 🎯 Cos'è Portfolio Rebalancer?

Portfolio Rebalancer è uno **strumento gratuito e open-source** che aiuta gli investitori a mantenere l'allocazione target del portafoglio in modo efficiente. A differenza del ribilanciamento tradizionale che richiede la vendita di asset (generando tasse sulle plusvalenze), la nostra funzione **Ribilanciamento Cash-Only** ottimizza i nuovi investimenti in liquidità per avvicinare il portafoglio agli obiettivi.

### ✨ Funzionalità

#### Funzionalità Core (Gratuite & Open Source)
- 🌍 **Ricerca Asset Globale** - Cerca azioni/ETF tramite Yahoo Finance (100+ exchange)
- 📊 **Analisi Visuale** - Grafici interattivi che mostrano allocazione attuale vs target
- 💰 **Ribilanciamento Cash-Only** - Ribilanciamento efficiente fiscalmente senza vendite
- 📈 **Ribilanciamento Tradizionale** - Raccomandazioni classiche di acquisto/vendita
- 🔄 **Prezzi Real-time** - Aggiornamento automatico prezzi via Yahoo Finance
- 📁 **Import/Export** - Supporto CSV per gestione portafoglio
- 🌐 **Bilingue** - Interfaccia in Inglese e Italiano
- 🎨 **UI Professionale** - Interfaccia pulita e moderna con statistiche in sidebar

### 🚀 Avvio Rapido

#### Prova Online
👉 **[Avvia App](https://your-app-url.streamlit.app)** - Nessuna installazione richiesta!

#### Esegui Localmente

```bash
# Clona il repository
git clone https://github.com/yourusername/portfolio-rebalancer.git
cd portfolio-rebalancer

# Installa le dipendenze
pip install -r requirements.txt

# Avvia l'app
streamlit run app.py
```

### 📖 Come Usarlo

1. **Imposta Allocazione Target**
   - Definisci le percentuali target (es: 80% Azionario, 20% Obbligazionario)
   - Il totale deve essere 100%

2. **Aggiungi Titoli al Portfolio**
   - Cerca per ISIN, ticker o nome
   - Aggiungi quantità e l'app recupera i prezzi correnti
   - Supporta tutti i mercati Yahoo Finance

3. **Analizza il Tuo Portfolio**
   - Visualizza allocazione attuale vs target
   - Vedi raccomandazioni di ribilanciamento
   - Usa la funzione Cash-Only per investimenti efficienti fiscalmente

4. **Ribilanciamento Cash-Only**
   - Inserisci liquidità disponibile da investire
   - Ottieni piano di acquisto ottimizzato
   - Nessuna vendita = Nessuna tassa su plusvalenze!

### 💡 Caso d'Uso di Esempio

**Portfolio Attuale:** €10.000
- Azionario: 60% (Target: 80%)
- Obbligazionario: 40% (Target: 20%)

**Nuova Liquidità:** €2.000

**Ribilanciamento Tradizionale:** Vendi €2.000 obbligazioni → Paga tasse su plusvalenze 😞

**Ribilanciamento Cash-Only:** Acquista €2.000 azioni → Nessuna tassa! 🎉

### 📄 Licenza

Questo progetto è rilasciato sotto licenza MIT - vedi il file [LICENSE](LICENSE) per dettagli.

### 📧 Contatti

- [GitHub Discussions](https://github.com/prev-creator/portfolio-rebalancer/discussions)

---

**Made with ❤️ by [Andrea]**