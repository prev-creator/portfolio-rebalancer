import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import requests
from typing import List, Dict
from streamlit_option_menu import option_menu

# ==================== TRANSLATIONS ====================
TRANSLATIONS = {
    'en': {
        'app_title': 'Portfolio Rebalancer', 'app_subtitle': 'Tax-Efficient Edition',
        'menu_targets': 'Targets & Portfolio', 'menu_analysis': 'Analysis', 'menu_settings': 'Settings',
        'sidebar_title': '📊 Dashboard', 'total_value': '💰 Total Value', 'portfolio_items': '🎯 Portfolio Items',
        'max_imbalance': '⚖️ Max Imbalance', 'allocation_quick': '🥧 Allocation Quick View',
        'add_items_info': '📊 Add items to see statistics', 'quick_guide': 'ℹ️ Quick Guide',
        'target_distribution': '🎯 Target Distribution', 'asset_class': 'Asset Class', 'target_pct': '% Target',
        'asset_class_help': 'Name of category (e.g., Stocks, Bonds)', 'target_pct_help': 'Desired percentage',
        'valid_target': '✅ Valid Target', 'invalid_target': '⚠️ Must be 100%', 'total': 'Total',
        'perfect': '✅ **Perfect!**', 'categories': 'categories', 'save_targets': '💾 Save Target Changes',
        'cancel_changes': '🔄 Cancel Changes', 'targets_saved': '✅ Targets saved successfully!',
        'your_portfolio': '📈 Your Portfolio', 'add_new_item': '➕ Add a New Item', 'category': 'Category',
        'select_category': 'Select the asset class', 'category_warning': '⚠️ First add at least one Asset Class!',
        'search_placeholder': 'Search by ISIN, Ticker or Name', 'search_example': 'Example: IE00B4L5Y983, SWDA.MI',
        'search_help': 'Enter ISIN, ticker or part of asset name', 'searching': '🔍 Searching...',
        'results_found': '✅ Found {n} results', 'select_asset': 'Select the asset:', 'ticker': 'Ticker',
        'exchange': 'Exchange', 'type': 'Type', 'no_results': '❌ No results found. Try another term.',
        'quantity': 'Quantity', 'quantity_help': 'Number of units to add', 'add_to_portfolio': '➕ Add to Portfolio',
        'fetching_data': '📊 Fetching data...', 'added_success': '✅ {ticker} added successfully!',
        'price_error': '❌ Unable to fetch price. Verify ticker.', 'current_portfolio': '📊 Current Portfolio',
        'category_help': 'Modify the asset class', 'ticker_help': 'Modify ticker/ISIN', 'name': 'Name',
        'name_help': 'Modify asset name', 'quantity_edit_help': 'Modify quantity owned', 'price': 'Price',
        'price_help': 'Modify unit price', 'total_value': 'Total Value',
        'total_value_help': 'Auto-calculated: Quantity × Price', 'update_prices': '🔄 Update Prices',
        'updating_prices': '⏳ Updating prices...', 'prices_updated': '✅ Prices updated!',
        'save_changes': '💾 Save Changes', 'changes_saved': '✅ Changes saved and recalculated!',
        'export_csv': '🔥 Export CSV', 'download_csv': '⬇️ Download CSV', 'delete_items': '🗑️ Delete Items',
        'select_delete': '⚠️ Select items to delete:', 'items_to_delete': 'Items to delete',
        'confirm_delete': '✅ Confirm Deletion', 'items_deleted': '✅ Items deleted!', 'cancel': '❌ Cancel',
        'empty_portfolio': '👆 Your portfolio is empty. Add first item!',
        'add_for_analysis': '📊 Add items to portfolio to view analysis', 'current_vs_target': '📊 Current vs Target',
        'percentage': 'Percentage %', 'current_allocation': '🥧 Current Allocation',
        'allocation_detail': '📋 Allocation Detail', 'current_pct': '% Current', 'difference': 'Difference',
        'rebalance_amount': '€ to Rebalance', 'traditional_plan': '💡 Traditional Rebalancing Plan',
        'action_threshold': 'Minimum action threshold (% difference)', 'threshold_help': 'Show only actions above threshold',
        'perfectly_balanced': '🎉 Portfolio perfectly balanced! No action required.',
        'buy_section': '### 📈 Buy', 'buy_action': '**{category}**: Buy ~**€{amount:,.2f}** ({diff:+.2f}%)',
        'sell_section': '### 📉 Sell', 'sell_action': '**{category}**: Sell ~**€{amount:,.2f}** ({diff:+.2f}%)',
        'cash_rebalancing': '💰 Cash-Only Rebalancing (Tax-Efficient)',
        'cash_subtitle': 'Purchase suggestions with new cash, without selling',
        'available_cash': '💵 Available cash to invest (€)', 'cash_help': 'Enter new cash to invest',
        'calculate_plan': '🧮 Calculate Cash-Only Plan', 'all_at_target': '✅ All categories at target!',
        'sufficient_cash': '✅ Sufficient cash! Remaining: €{remaining:,.2f}',
        'partial_cash': 'ℹ️ Partial cash: distributed proportionally', 'optimized_plan': '### 📈 Optimized Purchase Plan',
        'gap_to_fill': 'Gap to fill: €{gap:,.2f}', 'to_invest_metric': '💰 To Invest',
        'improvement_metric': '📊 Improvement', 'suggested_assets': '💡 Suggested assets in {category}',
        'shares_suggestion': '- **{ticker}** ({name}): ~{shares} shares × €{price:.2f} = €{total:,.2f}',
        'no_assets_warning': '⚠️ No assets for {category}. Add new assets.',
        'investment_summary': '### 📊 Investment Summary', 'cash_invested': '💰 Cash Invested',
        'cash_remaining': '💵 Cash Remaining', 'new_total_metric': '📈 New Total',
        'avg_improvement': '📊 Average Improvement', 'allocation_comparison': '### 📊 Allocation Before/After',
        'before': 'Before', 'after': 'After', 'target': 'Target', 'complete_detail': '### 📋 Complete Detail',
        'new_pct_col': 'New %', 'diff_from_target': 'Diff from Target',
        'enter_cash': '👆 Enter available cash to calculate investment plan',
        'data_management': '💾 Data Management', 'import_portfolio': '### 📥 Import Portfolio',
        'upload_csv': 'Upload a CSV file', 'csv_help': 'CSV must have: Category, Ticker, Name, Quantity, Price',
        'confirm_import': '✅ Confirm Import', 'import_success': '✅ Portfolio imported!',
        'csv_error': '❌ CSV must contain columns: {cols}', 'import_error': '❌ Import error: {error}',
        'reset_data': '### 🗑️ Reset Data', 'clear_portfolio': '⚠️ Clear Portfolio',
        'portfolio_cleared': '✅ Portfolio cleared!', 'reset_targets': '⚠️ Reset Targets',
        'targets_reset': '✅ Targets reset!', 'complete_reset': '🔥 Complete Reset',
        'all_cleared': '✅ All data cleared!', 'app_info': 'ℹ️ App Information',
        'default_stocks': 'Stocks', 'default_bonds': 'Bonds', 'default_alternatives': 'Alternatives',
    },
    'it': {
        'app_title': 'Portfolio Rebalancer', 'app_subtitle': 'Edizione Tax-Efficient',
        'menu_targets': 'Target & Portfolio', 'menu_analysis': 'Analisi', 'menu_settings': 'Impostazioni',
        'sidebar_title': '📊 Dashboard', 'total_value': '💰 Valore Totale', 'portfolio_items': '🎯 Titoli in Portfolio',
        'max_imbalance': '⚖️ Max Sbilanciamento', 'allocation_quick': '🥧 Allocazione Quick View',
        'add_items_info': '📊 Aggiungi titoli per vedere le statistiche', 'quick_guide': 'ℹ️ Guida Rapida',
        'target_distribution': '🎯 Distribuzione Target', 'asset_class': 'Asset Class', 'target_pct': '% Target',
        'asset_class_help': 'Nome categoria (es: Azionario, Obbligazionario)', 'target_pct_help': 'Percentuale desiderata',
        'valid_target': '✅ Target Valido', 'invalid_target': '⚠️ Deve essere 100%', 'total': 'Totale',
        'perfect': '✅ **Perfetto!**', 'categories': 'categorie', 'save_targets': '💾 Salva Modifiche Target',
        'cancel_changes': '🔄 Annulla Modifiche', 'targets_saved': '✅ Target salvati con successo!',
        'your_portfolio': '📈 Il Tuo Portafoglio', 'add_new_item': '➕ Aggiungi un Nuovo Titolo', 'category': 'Categoria',
        'select_category': 'Seleziona la categoria', 'category_warning': '⚠️ Aggiungi prima una Asset Class!',
        'search_placeholder': 'Cerca per ISIN, Ticker o Nome', 'search_example': 'Esempio: IE00B4L5Y983, SWDA.MI',
        'search_help': 'Inserisci ISIN, ticker o parte del nome', 'searching': '🔍 Ricerca in corso...',
        'results_found': '✅ Trovati {n} risultati', 'select_asset': 'Seleziona il titolo:', 'ticker': 'Ticker',
        'exchange': 'Exchange', 'type': 'Tipo', 'no_results': '❌ Nessun risultato. Prova altro termine.',
        'quantity': 'Quantità', 'quantity_help': 'Numero di unità da aggiungere', 'add_to_portfolio': '➕ Aggiungi al Portfolio',
        'fetching_data': '📊 Recupero dati...', 'added_success': '✅ {ticker} aggiunto con successo!',
        'price_error': '❌ Impossibile recuperare il prezzo. Verifica ticker.', 'current_portfolio': '📊 Portafoglio Attuale',
        'category_help': 'Modifica la categoria', 'ticker_help': 'Modifica ticker/ISIN', 'name': 'Nome',
        'name_help': 'Modifica nome titolo', 'quantity_edit_help': 'Modifica quantità posseduta', 'price': 'Prezzo',
        'price_help': 'Modifica prezzo unitario', 'total_value': 'Valore Totale',
        'total_value_help': 'Calcolato automaticamente: Quantità × Prezzo', 'update_prices': '🔄 Aggiorna Prezzi',
        'updating_prices': '⏳ Aggiornamento prezzi...', 'prices_updated': '✅ Prezzi aggiornati!',
        'save_changes': '💾 Salva Modifiche', 'changes_saved': '✅ Modifiche salvate e ricalcolate!',
        'export_csv': '🔥 Esporta CSV', 'download_csv': '⬇️ Download CSV', 'delete_items': '🗑️ Elimina Titoli',
        'select_delete': '⚠️ Seleziona i titoli da eliminare:', 'items_to_delete': 'Titoli da eliminare',
        'confirm_delete': '✅ Conferma Eliminazione', 'items_deleted': '✅ Titoli eliminati!', 'cancel': '❌ Annulla',
        'empty_portfolio': '👆 Il tuo portafoglio è vuoto. Aggiungi il primo titolo!',
        'add_for_analysis': '📊 Aggiungi titoli per visualizzare l\'analisi', 'current_vs_target': '📊 Attuale vs Target',
        'percentage': 'Percentuale %', 'current_allocation': '🥧 Allocazione Corrente',
        'allocation_detail': '📋 Dettaglio Allocazione', 'current_pct': '% Attuale', 'difference': 'Differenza',
        'rebalance_amount': '€ da Ribilanciare', 'traditional_plan': '💡 Piano Ribilanciamento Tradizionale',
        'action_threshold': 'Soglia minima di azione (% differenza)', 'threshold_help': 'Mostra solo azioni sopra soglia',
        'perfectly_balanced': '🎉 Portfolio perfettamente bilanciato! Nessuna azione richiesta.',
        'buy_section': '### 📈 Acquistare', 'buy_action': '**{category}**: Acquistare ~**€{amount:,.2f}** ({diff:+.2f}%)',
        'sell_section': '### 📉 Vendere', 'sell_action': '**{category}**: Vendere ~**€{amount:,.2f}** ({diff:+.2f}%)',
        'cash_rebalancing': '💰 Ribilanciamento Cash-Only (Tax-Efficient)',
        'cash_subtitle': 'Suggerimenti acquisto con nuova liquidità, senza vendere',
        'available_cash': '💵 Liquidità disponibile da investire (€)', 'cash_help': 'Inserisci nuova liquidità da investire',
        'calculate_plan': '🧮 Calcola Piano Cash-Only', 'all_at_target': '✅ Tutte le categorie già al target!',
        'sufficient_cash': '✅ Liquidità sufficiente! Residuo: €{remaining:,.2f}',
        'partial_cash': 'ℹ️ Liquidità parziale: distribuita proporzionalmente', 'optimized_plan': '### 📈 Piano Acquisto Ottimizzato',
        'gap_to_fill': 'Gap da colmare: €{gap:,.2f}', 'to_invest_metric': '💰 Da Investire',
        'improvement_metric': '📊 Miglioramento', 'suggested_assets': '💡 Titoli suggeriti in {category}',
        'shares_suggestion': '- **{ticker}** ({name}): ~{shares} azioni × €{price:.2f} = €{total:,.2f}',
        'no_assets_warning': '⚠️ Nessun titolo per {category}. Aggiungi nuovi titoli.',
        'investment_summary': '### 📊 Riepilogo Investimento', 'cash_invested': '💰 Liquidità Investita',
        'cash_remaining': '💵 Liquidità Residua', 'new_total_metric': '📈 Nuovo Totale',
        'avg_improvement': '📊 Miglioramento Medio', 'allocation_comparison': '### 📊 Confronto Allocazione Prima/Dopo',
        'before': 'Prima', 'after': 'Dopo', 'target': 'Target', 'complete_detail': '### 📋 Dettaglio Completo',
        'new_pct_col': 'Nuova %', 'diff_from_target': 'Differenza dal Target',
        'enter_cash': '👆 Inserisci liquidità disponibile per calcolare piano',
        'data_management': '💾 Gestione Dati', 'import_portfolio': '### 📥 Importa Portfolio',
        'upload_csv': 'Carica un file CSV', 'csv_help': 'CSV deve avere: Categoria, Ticker, Nome, Quantità, Prezzo',
        'confirm_import': '✅ Conferma Importazione', 'import_success': '✅ Portfolio importato!',
        'csv_error': '❌ CSV deve contenere colonne: {cols}', 'import_error': '❌ Errore importazione: {error}',
        'reset_data': '### 🗑️ Reset Dati', 'clear_portfolio': '⚠️ Cancella Portfolio',
        'portfolio_cleared': '✅ Portfolio cancellato!', 'reset_targets': '⚠️ Reset Target',
        'targets_reset': '✅ Target resettati!', 'complete_reset': '🔥 Reset Completo',
        'all_cleared': '✅ Tutti i dati cancellati!', 'app_info': 'ℹ️ Informazioni App',
        'default_stocks': 'Azionario', 'default_bonds': 'Obbligazionario', 'default_alternatives': 'Alternativi',
    }
}

t = lambda k: TRANSLATIONS[st.session_state.get('language', 'en')].get(k, k)

# ==================== CONFIG & INIT ====================
st.set_page_config(layout="wide", page_title="Portfolio Rebalancer", page_icon="💼")

defaults = {
    'language': 'en',
    'portfolio': pd.DataFrame(),
    'df_targets': lambda: pd.DataFrame({
        "Asset Class": [t('default_stocks'), t('default_bonds'), t('default_alternatives')],
        "% Target": [80.0, 10.0, 10.0]
    })
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v() if callable(v) else v

if 'targets' not in st.session_state:
    st.session_state.targets = dict(zip(st.session_state.df_targets["Asset Class"], st.session_state.df_targets["% Target"]))

# ==================== HELPER FUNCTIONS ====================
@st.cache_data(ttl=3600)
def search_yahoo_finance(query: str, max_results: int = 10) -> List[Dict]:
    try:
        response = requests.get(
            "https://query2.finance.yahoo.com/v1/finance/search",
            params={'q': query, 'quotesCount': max_results, 'newsCount': 0, 'enableFuzzyQuery': False},
            headers={'User-Agent': 'Mozilla/5.0'},
            timeout=5
        )
        if response.status_code == 200:
            return [
                {'symbol': q.get('symbol', ''), 'name': q.get('longname') or q.get('shortname', ''),
                 'exchange': q.get('exchDisp', q.get('exchange', '')), 'type': q.get('typeDisp', ''),
                 'isin': q.get('isin', 'N/A')}
                for q in response.json().get('quotes', [])
                if q.get('quoteType') in ['EQUITY', 'ETF', 'MUTUALFUND']
            ]
    except Exception as e:
        st.error(f"Search error: {str(e)}")
    return []

@st.cache_data(ttl=3600)
def get_price(ticker: str) -> float:
    try:
        data = yf.Ticker(ticker).history(period="1d")
        return float(data["Close"].iloc[-1]) if not data.empty else 0.0
    except:
        return 0.0

# ==================== HEADER ====================
col_title, col_lang = st.columns([4, 1])
with col_title:
    st.title(f"💼 {t('app_title')}")
    st.caption(t('app_subtitle'))
with col_lang:
    st.write("")
    lang_map = {'English': 'en', 'Italiano': 'it'}
    sel_lang = st.selectbox("🌐", list(lang_map.keys()), 
                            index=list(lang_map.values()).index(st.session_state.language),
                            label_visibility="collapsed")
    if lang_map[sel_lang] != st.session_state.language:
        st.session_state.language = lang_map[sel_lang]
        st.rerun()

page = option_menu(
    None, [t('menu_targets'), t('menu_analysis'), t('menu_settings')],
    icons=["bullseye", "bar-chart-line", "gear"], default_index=0, orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"}}
)
st.divider()

# ==================== SIDEBAR ====================
with st.sidebar:
    st.title(t('sidebar_title'))
    if not st.session_state.portfolio.empty:
        total = st.session_state.portfolio["Valore"].sum()
        st.metric(t('total_value'), f"€{total:,.2f}")
        st.metric(t('portfolio_items'), len(st.session_state.portfolio))
        
        curr_alloc = st.session_state.portfolio.groupby("Categoria")["Valore"].sum()
        pct_curr = (curr_alloc / total * 100).round(2)
        all_cats = list(set(st.session_state.df_targets["Asset Class"].tolist() + pct_curr.index.tolist()))
        df_comp = pd.DataFrame({"Asset Class": all_cats})
        df_comp["% Current"] = df_comp["Asset Class"].map(lambda x: pct_curr.get(x, 0.0))
        df_comp["% Target"] = df_comp["Asset Class"].map(lambda x: st.session_state.targets.get(x, 0.0))
        df_comp["Diff"] = df_comp["% Target"] - df_comp["% Current"]
        
        st.metric(t('max_imbalance'), f"{df_comp['Diff'].abs().max():.1f}%")
        st.divider()
        st.subheader(t('allocation_quick'))
        fig_mini = go.Figure(data=[go.Pie(labels=df_comp["Asset Class"], values=df_comp["% Current"], 
                                          hole=0.4, textinfo='label+percent', textposition='inside')])
        fig_mini.update_layout(height=250, showlegend=False, margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig_mini, use_container_width=True)
    else:
        st.info(t('add_items_info'))
    
    st.divider()
    with st.expander(t('quick_guide')):
        st.markdown(f"### 🎯 {t('menu_targets')}\n{t('select_category')}")
        st.markdown(f"### 📊 {t('menu_analysis')}\nVisualize allocation")
        st.markdown(f"### ⚙️ {t('menu_settings')}\nManage data")
        st.markdown("### 💡 Cash-Only\nZero taxes!")

# ==================== PAGE: TARGETS & PORTFOLIO ====================
if page == t('menu_targets'):
    st.header(t('target_distribution'))
    col_edit, col_sum = st.columns([3, 1])
    
    with col_edit:
        if 'editing_targets' not in st.session_state:
            st.session_state.editing_targets = st.session_state.df_targets.copy()
        
        edited_df = st.data_editor(
            st.session_state.editing_targets,
            column_config={
                "Asset Class": st.column_config.TextColumn(t('asset_class'), help=t('asset_class_help')),
                "% Target": st.column_config.NumberColumn(t('target_pct'), min_value=0, max_value=100, 
                                                          step=0.1, format="%.1f%%", help=t('target_pct_help'))
            },
            num_rows="dynamic", use_container_width=True, hide_index=True, key="targets_editor"
        )
    
    with col_sum:
        tot_pct = edited_df["% Target"].sum()
        
        if abs(tot_pct - 100) < 0.5:
            st.success(t('valid_target'))
            st.metric(t('total'), f"{tot_pct:.1f}%", delta=None)
            st.markdown(t('perfect'))
        else:
            st.error(t('invalid_target'))
            st.metric(t('total'), f"{tot_pct:.1f}%", delta=f"{tot_pct-100:+.1f}%")
        
        st.caption(f"📊 {len(edited_df)} {t('categories')}")
    
    st.divider()
    col_save, col_reset = st.columns(2)
    with col_save:
        if st.button(t('save_targets'), type="primary", use_container_width=True):
            st.session_state.editing_targets = st.session_state.df_targets = edited_df.copy()
            st.session_state.targets = dict(zip(edited_df["Asset Class"], edited_df["% Target"]))
            st.success(t('targets_saved'))
            st.rerun()
    with col_reset:
        if st.button(t('cancel_changes'), use_container_width=True):
            st.session_state.editing_targets = st.session_state.df_targets.copy()
            st.rerun()
    
    st.divider()
    st.header(t('your_portfolio'))
    
    with st.expander(t('add_new_item'), expanded=st.session_state.portfolio.empty):
        if st.session_state.get('reset_add_form'):
            for k in ['search_query', 'ticker_select', 'add_quantity']:
                st.session_state.pop(k, None)
            st.session_state.reset_add_form = False
            st.rerun()
        
        col1, col2 = st.columns([1, 2])
        with col1:
            cats = st.session_state.df_targets["Asset Class"].tolist()
            if not cats:
                st.warning(t('category_warning'))
                category = None
            else:
                category = st.selectbox(t('category'), cats, help=t('select_category'), key="add_categoria")
        
        with col2:
            query = st.text_input(t('search_placeholder'), placeholder=t('search_example'), 
                                 help=t('search_help'), key="search_query")
        
        selected_ticker = selected_name = None
        if query and len(query) >= 3:
            with st.spinner(t('searching')):
                results = search_yahoo_finance(query)
            
            if results:
                st.success(t('results_found').format(n=len(results)))
                opts = [f"{r['symbol']} - {r['name'][:50]} ({r['exchange']})" + 
                       (f" | ISIN: {r['isin']}" if r['isin'] != 'N/A' else "") for r in results]
                sel = st.selectbox(t('select_asset'), opts, key="ticker_select")
                idx = opts.index(sel)
                selected_ticker, selected_name = results[idx]['symbol'], results[idx]['name']
                
                c1, c2, c3 = st.columns(3)
                c1.caption(f"**{t('ticker')}:** {selected_ticker}")
                c2.caption(f"**{t('exchange')}:** {results[idx]['exchange']}")
                c3.caption(f"**{t('type')}:** {results[idx]['type']}")
            else:
                st.warning(t('no_results'))
        
        col_qty, col_add = st.columns([2, 1])
        with col_qty:
            qty = st.number_input(t('quantity'), min_value=0.0, step=1.0, value=1.0, 
                                 help=t('quantity_help'), key="add_quantity")
        with col_add:
            st.write(""); st.write("")
            if st.button(t('add_to_portfolio'), use_container_width=True, type="primary", 
                        disabled=not selected_ticker or not category):
                with st.spinner(t('fetching_data')):
                    price = get_price(selected_ticker)
                    if price > 0:
                        new_row = pd.DataFrame([{"Categoria": category, "Ticker": selected_ticker,
                                                "Nome": selected_name or selected_ticker, "Quantità": qty,
                                                "Prezzo": price, "Valore": qty * price}])
                        st.session_state.portfolio = pd.concat([st.session_state.portfolio, new_row], ignore_index=True)
                        st.session_state.reset_add_form = True
                        st.success(t('added_success').format(ticker=selected_ticker))
                        st.rerun()
                    else:
                        st.error(t('price_error'))
    
    st.divider()
    if not st.session_state.portfolio.empty:
        st.subheader(t('current_portfolio'))
        edited_pf = st.data_editor(
            st.session_state.portfolio.copy(),
            column_config={
                "Categoria": st.column_config.SelectboxColumn(t('category'), 
                    options=st.session_state.df_targets["Asset Class"].tolist(), help=t('category_help'), required=True),
                "Ticker": st.column_config.TextColumn(t('ticker'), help=t('ticker_help'), required=True),
                "Nome": st.column_config.TextColumn(t('name'), width="large", help=t('name_help')),
                "Quantità": st.column_config.NumberColumn(t('quantity'), min_value=0, step=0.01, 
                                                          format="%.4f", help=t('quantity_edit_help')),
                "Prezzo": st.column_config.NumberColumn(t('price'), min_value=0, step=0.01, 
                                                        format="€%.4f", help=t('price_help')),
                "Valore": st.column_config.NumberColumn(t('total_value'), format="€%.2f", 
                                                        disabled=True, help=t('total_value_help'))
            },
            use_container_width=True, hide_index=True, num_rows="dynamic", key="portfolio_editor"
        )
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            if st.button(t('update_prices'), use_container_width=True):
                with st.spinner(t('updating_prices')):
                    for idx, row in st.session_state.portfolio.iterrows():
                        if (p := get_price(row["Ticker"])) > 0:
                            st.session_state.portfolio.at[idx, "Prezzo"] = p
                            st.session_state.portfolio.at[idx, "Valore"] = row["Quantità"] * p
                st.success(t('prices_updated'))
                st.rerun()
        with c2:
            if st.button(t('save_changes'), use_container_width=True, type="primary"):
                for idx in edited_pf.index:
                    for col in ["Categoria", "Ticker", "Nome", "Quantità", "Prezzo"]:
                        st.session_state.portfolio.at[idx, col] = edited_pf.at[idx, col]
                    st.session_state.portfolio.at[idx, "Valore"] = edited_pf.at[idx, "Quantità"] * edited_pf.at[idx, "Prezzo"]
                
                if len(edited_pf) > len(st.session_state.portfolio):
                    new_rows = edited_pf.iloc[len(st.session_state.portfolio):].copy()
                    new_rows["Valore"] = new_rows["Quantità"] * new_rows["Prezzo"]
                    st.session_state.portfolio = pd.concat([st.session_state.portfolio, new_rows], ignore_index=True)
                elif len(edited_pf) < len(st.session_state.portfolio):
                    st.session_state.portfolio = st.session_state.portfolio.iloc[:len(edited_pf)].reset_index(drop=True)
                
                st.success(t('changes_saved'))
                st.rerun()
        with c3:
            if st.button(t('export_csv'), use_container_width=True):
                st.download_button(t('download_csv'), st.session_state.portfolio.to_csv(index=False),
                                  "portfolio.csv", "text/csv", use_container_width=True)
        with c4:
            if st.button(t('delete_items'), use_container_width=True):
                st.session_state['show_delete'] = not st.session_state.get('show_delete', False)
                st.rerun()
        
        if st.session_state.get('show_delete'):
            st.warning(t('select_delete'))
            to_del = st.multiselect(t('items_to_delete'), options=st.session_state.portfolio.index,
                format_func=lambda x: f"{st.session_state.portfolio.at[x, 'Ticker']} - {st.session_state.portfolio.at[x, 'Nome']}")
            c1, c2 = st.columns(2)
            with c1:
                if st.button(t('confirm_delete'), type="primary", use_container_width=True):
                    st.session_state.portfolio = st.session_state.portfolio.drop(to_del).reset_index(drop=True)
                    st.session_state['show_delete'] = False
                    st.success(t('items_deleted'))
                    st.rerun()
            with c2:
                if st.button(t('cancel'), use_container_width=True):
                    st.session_state['show_delete'] = False
                    st.rerun()
    else:
        st.info(t('empty_portfolio'))

# ==================== PAGE: ANALYSIS ====================
elif page == t('menu_analysis'):
    if st.session_state.portfolio.empty:
        st.info(t('add_for_analysis'))
    else:
        tot_pf = st.session_state.portfolio["Valore"].sum()
        curr_alloc = st.session_state.portfolio.groupby("Categoria")["Valore"].sum()
        pct_curr = (curr_alloc / tot_pf * 100).round(2)
        all_cats = list(set(st.session_state.df_targets["Asset Class"].tolist() + pct_curr.index.tolist()))
        
        df_comp = pd.DataFrame({
            "Asset Class": all_cats,
            "% Current": [pct_curr.get(x, 0.0) for x in all_cats],
            "% Target": [st.session_state.targets.get(x, 0.0) for x in all_cats]
        })
        df_comp["Difference"] = df_comp["% Target"] - df_comp["% Current"]
        df_comp["€ to Rebalance"] = (df_comp["Difference"] / 100 * tot_pf).round(2)
        df_comp = df_comp.sort_values("Asset Class").reset_index(drop=True)
        
        c1, c2, c3 = st.columns(3)
        c1.metric(t('total_value'), f"€{tot_pf:,.2f}")
        c2.metric(t('max_imbalance'), f"{df_comp['Difference'].abs().max():.1f}%")
        c3.metric("🎯 Actions", len([x for x in df_comp["€ to Rebalance"] if abs(x) > tot_pf * 0.01]))
        
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(t('current_vs_target'))
            fig = go.Figure([
                go.Bar(name=t('current_pct'), x=df_comp["Asset Class"], y=df_comp["% Current"], marker_color='lightblue'),
                go.Bar(name=t('target'), x=df_comp["Asset Class"], y=df_comp["% Target"], marker_color='orange')
            ])
            fig.update_layout(barmode='group', yaxis_title=t('percentage'), height=400, showlegend=True)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader(t('current_allocation'))
            fig_pie = go.Figure([go.Pie(labels=df_comp["Asset Class"], values=df_comp["% Current"], hole=0.3)])
            fig_pie.update_layout(height=400)
            st.plotly_chart(fig_pie, use_container_width=True)
        
        st.divider()
        st.subheader(t('allocation_detail'))
        disp_df = df_comp.rename(columns={
            "% Current": t('current_pct'), "% Target": t('target_pct'),
            "Difference": t('difference'), "€ to Rebalance": t('rebalance_amount')
        })
        st.dataframe(
            disp_df.style.format({
                t('current_pct'): "{:.2f}%", t('target_pct'): "{:.2f}%",
                t('difference'): "{:+.2f}%", t('rebalance_amount'): "€{:,.2f}"
            }).background_gradient(subset=[t('difference')], cmap="RdYlGn", vmin=-10, vmax=10),
            use_container_width=True, hide_index=True
        )
        
        st.divider()
        st.subheader(t('traditional_plan'))
        thresh = st.slider(t('action_threshold'), 0.5, 5.0, 1.0, 0.5, help=t('threshold_help'))
        actions = df_comp[df_comp["Difference"].abs() > thresh].copy()
        
        if actions.empty:
            st.success(t('perfectly_balanced'))
        else:
            if not (buys := actions[actions["Difference"] > 0].sort_values("Difference", ascending=False)).empty:
                st.markdown(t('buy_section'))
                for _, r in buys.iterrows():
                    st.success(t('buy_action').format(category=r['Asset Class'], 
                              amount=abs(r['€ to Rebalance']), diff=r['Difference']))
            
            if not (sells := actions[actions["Difference"] < 0].sort_values("Difference")).empty:
                st.markdown(t('sell_section'))
                for _, r in sells.iterrows():
                    st.warning(t('sell_action').format(category=r['Asset Class'], 
                              amount=abs(r['€ to Rebalance']), diff=r['Difference']))
        
        st.divider()
        st.subheader(t('cash_rebalancing'))
        st.caption(t('cash_subtitle'))
        
        c1, c2 = st.columns([2, 1])
        with c1:
            cash = st.number_input(t('available_cash'), min_value=0.0, value=0.0, step=100.0, help=t('cash_help'))
        with c2:
            st.write(""); st.write("")
            calc = st.button(t('calculate_plan'), type="primary", use_container_width=True)
        
        if cash > 0 and calc:
            st.markdown("---")
            new_tot = tot_pf + cash
            
            df_cash = df_comp.copy()
            df_cash["Curr Val €"] = (df_cash["% Current"] / 100) * tot_pf
            df_cash["Tgt Val €"] = (df_cash["% Target"] / 100) * new_tot
            df_cash["Gap €"] = df_cash["Tgt Val €"] - df_cash["Curr Val €"]
            
            to_buy = df_cash[df_cash["Gap €"] > 0].copy()
            
            if to_buy.empty:
                st.success(t('all_at_target'))
            else:
                tot_gap = to_buy["Gap €"].sum()
                if cash >= tot_gap:
                    to_buy["€ Invest"] = to_buy["Gap €"]
                    remaining = cash - tot_gap
                    st.success(t('sufficient_cash').format(remaining=remaining))
                else:
                    to_buy["€ Invest"] = (to_buy["Gap €"] / tot_gap * cash).round(2)
                    remaining = 0
                    st.info(t('partial_cash'))
                
                to_buy["New Val €"] = to_buy["Curr Val €"] + to_buy["€ Invest"]
                to_buy["New %"] = (to_buy["New Val €"] / new_tot * 100).round(2)
                to_buy["Improv"] = (to_buy["New %"] - to_buy["% Current"]).round(2)
                
                st.markdown(t('optimized_plan'))
                for _, r in to_buy.sort_values("€ Invest", ascending=False).iterrows():
                    ca, cb, cc = st.columns([2, 1, 1])
                    with ca:
                        st.markdown(f"**{r['Asset Class']}**")
                        st.caption(t('gap_to_fill').format(gap=r['Gap €']))
                    with cb:
                        st.metric(t('to_invest_metric'), f"€{r['€ Invest']:,.2f}")
                    with cc:
                        st.metric(t('improvement_metric'), f"{r['Improv']:+.2f}%",
                                 delta=f"{r['% Current']:.1f}% → {r['New %']:.1f}%")
                    
                    cat_assets = st.session_state.portfolio[st.session_state.portfolio["Categoria"] == r["Asset Class"]]
                    if not cat_assets.empty:
                        with st.expander(t('suggested_assets').format(category=r['Asset Class'])):
                            for _, a in cat_assets.iterrows():
                                if (n := int(r["€ Invest"] / a["Prezzo"])) > 0:
                                    st.write(t('shares_suggestion').format(
                                        ticker=a['Ticker'], name=a['Nome'], shares=n,
                                        price=a['Prezzo'], total=n * a['Prezzo']))
                    else:
                        st.info(t('no_assets_warning').format(category=r['Asset Class']))
                
                st.divider()
                st.markdown(t('investment_summary'))
                c1, c2, c3, c4 = st.columns(4)
                c1.metric(t('cash_invested'), f"€{cash - remaining:,.2f}")
                c2.metric(t('cash_remaining'), f"€{remaining:,.2f}")
                c3.metric(t('new_total_metric'), f"€{new_tot:,.2f}")
                c4.metric(t('avg_improvement'), f"+{to_buy['Improv'].mean():.2f}%")
                
                st.markdown(t('allocation_comparison'))
                df_full = df_comp.copy()
                df_full["New %"] = df_full["% Current"]
                for _, r in to_buy.iterrows():
                    if (idx := df_full[df_full["Asset Class"] == r["Asset Class"]].index).any():
                        df_full.loc[idx, "New %"] = r["New %"]
                for i, r in df_full.iterrows():
                    if r["Asset Class"] not in to_buy["Asset Class"].values:
                        df_full.loc[i, "New %"] = ((r["% Current"] / 100) * tot_pf / new_tot * 100)
                
                fig_comp = go.Figure([
                    go.Bar(name=t('before'), x=df_full["Asset Class"], y=df_full["% Current"], marker_color='lightcoral'),
                    go.Bar(name=t('after'), x=df_full["Asset Class"], y=df_full["New %"], marker_color='lightgreen'),
                    go.Bar(name=t('target'), x=df_full["Asset Class"], y=df_full["% Target"], marker_color='gold', opacity=0.6)
                ])
                fig_comp.update_layout(barmode='group', yaxis_title=t('percentage'), height=400, showlegend=True)
                st.plotly_chart(fig_comp, use_container_width=True)
                
                st.markdown(t('complete_detail'))
                det = df_full[["Asset Class", "% Current", "New %", "% Target"]].copy()
                det["Diff"] = (det["% Target"] - det["New %"]).round(2)
                det = det.rename(columns={
                    "% Current": t('current_pct'), "New %": t('new_pct_col'),
                    "% Target": t('target_pct'), "Diff": t('diff_from_target')
                })
                st.dataframe(
                    det.style.format({
                        t('current_pct'): "{:.2f}%", t('new_pct_col'): "{:.2f}%",
                        t('target_pct'): "{:.2f}%", t('diff_from_target'): "{:+.2f}%"
                    }).background_gradient(subset=[t('diff_from_target')], cmap="RdYlGn", vmin=-5, vmax=5),
                    use_container_width=True, hide_index=True
                )
        elif cash == 0:
            st.info(t('enter_cash'))

# ==================== PAGE: SETTINGS ====================
elif page == t('menu_settings'):
    st.subheader(t('data_management'))
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown(t('import_portfolio'))
        if (f := st.file_uploader(t('upload_csv'), type=['csv'], help=t('csv_help'))):
            try:
                df_imp = pd.read_csv(f)
                req = ["Categoria", "Ticker", "Nome", "Quantità", "Prezzo"]
                if all(c in df_imp.columns for c in req):
                    df_imp["Valore"] = df_imp["Quantità"] * df_imp["Prezzo"]
                    if st.button(t('confirm_import'), type="primary"):
                        st.session_state.portfolio = df_imp
                        st.success(t('import_success'))
                        st.rerun()
                else:
                    st.error(t('csv_error').format(cols=', '.join(req)))
            except Exception as e:
                st.error(t('import_error').format(error=str(e)))
    
    with c2:
        st.markdown(t('reset_data'))
        if st.button(t('clear_portfolio'), use_container_width=True):
            st.session_state.portfolio = pd.DataFrame()
            st.success(t('portfolio_cleared'))
            st.rerun()
        
        if st.button(t('reset_targets'), use_container_width=True):
            lang = st.session_state.language
            st.session_state.df_targets = pd.DataFrame({
                "Asset Class": [TRANSLATIONS[lang][k] for k in ['default_stocks', 'default_bonds', 'default_alternatives']],
                "% Target": [80.0, 10.0, 10.0]
            })
            st.session_state.targets = dict(zip(st.session_state.df_targets["Asset Class"], st.session_state.df_targets["% Target"]))
            st.session_state.editing_targets = st.session_state.df_targets.copy()
            st.success(t('targets_reset'))
            st.rerun()
        
        if st.button(t('complete_reset'), type="secondary", use_container_width=True):
            st.session_state.clear()
            st.success(t('all_cleared'))
            st.rerun()
    
    st.divider()
    st.subheader(t('app_info'))
    
    features_text = {
        'en': """
**Portfolio Rebalancer - Professional Edition**

✅ Global search via Yahoo Finance  
✅ International ISIN support  
✅ Real-time price updates  
✅ Visual allocation analysis  
✅ Automatic rebalancing suggestions  
✅ Cash-Only Rebalancing (Tax-Efficient)  
✅ Bilingual: English/Italian  
✅ Professional navigation menu  
✅ Sidebar with statistics  
✅ CSV Import/Export  

**Supported markets:** All markets on Yahoo Finance (100+ global exchanges)
""",
        'it': """
**Portfolio Rebalancer - Professional Edition**

✅ Ricerca globale via Yahoo Finance  
✅ Supporto ISIN internazionali  
✅ Aggiornamento prezzi real-time  
✅ Analisi visuale allocazione  
✅ Suggerimenti automatici di ribilanciamento  
✅ Ribilanciamento Cash-Only (Tax-Efficient)  
✅ Bilingue: Inglese/Italiano  
✅ Menu professionale di navigazione  
✅ Sidebar con statistiche  
✅ Import/Export CSV  

**Mercati supportati:** Tutti i mercati su Yahoo Finance (100+ exchange globali)
"""
    }
    
    st.markdown(features_text[st.session_state.language])