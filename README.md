# 📖 Editor Ricette di Famiglia

Editor collaborativo per digitalizzare e correggere ricette di famiglia da quaderni manoscritti.

## 🚀 Avvio rapido

1. **Apri l'editor**: Apri `index.html` nel browser (doppio click o `file:///percorso/index.html`)
2. **Modifica le ricette**: Correggi il testo OCR nell'editor a destra
3. **Visualizza l'originale**: Consulta le scansioni a sinistra
4. **Marca come verificato**: Spunta la checkbox quando hai finito di correggere
5. **Esporta**: Clicca "💾 Esporta JSON" quando hai completato alcune ricette

## 📁 Struttura progetto

```
ricette-famiglia/
├── index.html              # Editor web
├── style.css               # Stili interfaccia
├── convert_ocr.py          # Script conversione MD → JSON
├── README.md               # Questa guida
├── data/
│   └── ricette.json        # Database ricette (JSON)
└── immagini/
    ├── IMG_4199.jpg
    ├── IMG_4200.jpg
    └── ...                 # Scansioni quaderni
```

## 🎯 Come usare l'editor

### Interfaccia

- **Sinistra (50%)**: Visualizzazione immagini delle ricette originali scannerizzate
  - Click su un'immagine per ingrandirla
  - Scroll per vedere immagini multiple della stessa ricetta

- **Destra (50%)**: Editor markdown
  - Titolo della ricetta corrente
  - Checkbox "Verificato" per marcare ricette corrette
  - Area di testo per modificare il markdown
  - Navigazione precedente/successiva

### Workflow consigliato

1. **Leggi l'originale**: Guarda attentamente la scansione a sinistra
2. **Correggi il testo**: Modifica gli errori OCR nell'editor
3. **Verifica ingredienti**: Controlla quantità, unità di misura, nomi
4. **Verifica procedimento**: Assicurati che i passaggi abbiano senso
5. **Marca come verificato**: Spunta la checkbox
6. **Passa alla successiva**: Click su "Successiva →" o usa `Alt+→`

### Scorciatoie da tastiera

- `Alt + ←` : Ricetta precedente
- `Alt + →` : Ricetta successiva
- `Alt + V` : Toggle checkbox "Verificato"
- `Alt + E` : Apri modal esportazione JSON

## 💾 Salvare le modifiche

L'editor lavora **solo in memoria del browser**. Per salvare permanentemente hai tre opzioni:

### Opzione 1: Salvataggio automatico su GitHub ⭐ (consigliata)

Configura il salvataggio automatico per pushare direttamente su GitHub con un click!

#### Come ottenere il Personal Access Token GitHub:

1. Vai su [github.com](https://github.com) ed effettua il login
2. Click sulla tua foto profilo (in alto a destra) → **Settings**
3. Scorri in basso nella sidebar sinistra → **Developer settings**
4. Click su **Personal access tokens** → **Tokens (classic)**
5. Click su **Generate new token** → **Generate new token (classic)**
6. Compila il form:
   - **Note**: "Editor Ricette Famiglia" (o un nome a tua scelta)
   - **Expiration**: scegli la durata (es. 90 giorni, 1 anno, o No expiration)
   - **Scope**: spunta **SOLO "repo"** (accesso completo ai repository privati)
7. Scorri in basso e click su **Generate token**
8. **IMPORTANTE**: Copia subito il token (inizia con `ghp_...`) - non lo vedrai più!

#### Configurazione nell'editor:

1. Apri l'editor (`index.html`)
2. Scorri in fondo alla pagina e apri **"⚙️ Impostazioni GitHub"**
3. Compila i campi:
   - **GitHub Username**: il tuo username (es. `StE2808`)
   - **Repository Name**: nome del repo dove hai il progetto (default: `ricette-famiglia`)
   - **Personal Access Token**: incolla il token copiato (es. `ghp_xxxxxxxxxxxx`)
4. Click su **"💾 Salva impostazioni"**

#### Utilizzo:

- Dopo aver configurato, il bottone **"💾 Esporta JSON"** salverà automaticamente su GitHub
- Il commit message includerà il progresso (es. "Aggiornamento ricette (42/99 verificate)")
- Vedrai **"✅ Salvato su GitHub!"** quando il salvataggio è completato
- In caso di errore, ti verrà chiesto se vuoi usare il metodo manuale

### Opzione 2: Esportazione manuale

1. Click su "💾 Esporta JSON" (o `Alt+E`)
2. Click su "📋 Copia negli appunti" oppure "💾 Scarica file"
3. Se hai copiato: incolla il contenuto in `data/ricette.json`
4. Se hai scaricato: sostituisci il file `data/ricette.json` con quello scaricato

### Opzione 3: Git commit da terminale

Se usi Git per versionare il progetto:

```bash
# Dopo aver esportato e salvato ricette.json
git add data/ricette.json
git commit -m "Verificate ricette 1-10: corretto OCR e ingredienti"
git push
```

## 🔄 Riconvertire da Markdown

Se modifichi il file `Quaderno_Ricette_Completo.md` originale e vuoi rigenerare il JSON:

```bash
cd ricette-famiglia
python3 convert_ocr.py
```

**⚠️ ATTENZIONE**: Questo sovrascriverà `data/ricette.json` e perderai tutte le correzioni già fatte!

## 📊 Progresso

Il contatore in alto a destra mostra quante ricette sono state verificate:

```
42/99 verificate
```

Obiettivo: arrivare a 99/99! 🎉

## 🛠️ Personalizzazioni

### Modificare lo stile

Modifica `style.css` per cambiare colori, font, layout:

```css
:root {
    --primary: #2c3e50;      /* Colore principale header */
    --accent: #3498db;       /* Colore bottoni */
    --success: #27ae60;      /* Colore "verificato" */
}
```

### Aggiungere funzionalità

Modifica il `<script>` in `index.html`. Alcune idee:

- Ricerca ricette per titolo
- Filtro per ricette verificate/non verificate
- Anteprima HTML del markdown
- Auto-salvataggio in localStorage

## ❓ Domande frequenti

### Le modifiche vengono salvate automaticamente?

No. Le modifiche sono in memoria del browser. Devi esportare manualmente il JSON per salvarle su disco.

### Posso usare l'editor offline?

Sì! È un'applicazione HTML/CSS/JS statica. Funziona anche senza connessione internet.

### Posso lavorare in più persone contemporaneamente?

Non direttamente. Per collaborare:
1. Dividete le ricette (es. persona A fa 1-50, persona B fa 51-99)
2. Usate Git per sincronizzare
3. Esportate e committate frequentemente

### Cosa succede se chiudo il browser senza esportare?

Perdi tutte le modifiche non esportate. Esporta frequentemente!

## 📝 Note tecniche

- **Browser consigliati**: Chrome, Firefox, Safari moderni
- **Formato immagini**: JPEG (già incluse in `immagini/`)
- **Formato dati**: JSON con encoding UTF-8
- **Responsive**: Funziona anche su tablet (layout verticale sotto 768px)

## 🎨 Screenshot workflow

```
1. [IMMAGINE]          2. [EDITOR]           3. [✓ VERIFICATO]
   ┌─────────┐           ┌─────────┐           ┌─────────┐
   │Scansione│   →       │Correggi │    →      │ Esporta │
   │originale│           │errori   │           │  JSON   │
   └─────────┘           └─────────┘           └─────────┘
```

---

**Buon lavoro con la digitalizzazione delle ricette! 👨‍🍳👩‍🍳**
