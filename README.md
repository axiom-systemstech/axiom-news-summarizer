
# 📰 AXIOM News Summarizer

> **AI-powered intelligence from your terminal**

Intelligent news summarization tool by AXIOM Systems. Fetches latest news and generates concise AI summaries using Facebook's BART model.

## ✨ AXIOM Features

- 🎯 **Terminal-native** - Pure CLI intelligence
- 🧠 **BART AI summaries** - Facebook's state-of-the-art model
- ⚡ **Real-time fetch** - Google News RSS integration
- 🎨 **Rich UI** - Colored panels and progress bars
- 📦 **One-command install** - `pip install axiom-news-summarizer`

## 🚀 Quick Install

```bash
pip install axiom-news-summarizer
```
💻 Usage
bash
axiom-news-summarizer elecciones
axiom-news-summarizer tecnologia
axiom-news-summarizer deportes

## 🛠️ Development
```bash
git clone https://github.com/axiom-systemstech/axiom-news-summarizer.git
cd axiom-news-summarizer
pip install -e .
pytest tests/
```

## 📄 License
MIT © Manuel Echepares / AXIOM Systems
<br>

---

<br>

## 🚀 Cómo crear el repo en GitHub (paso a paso)


# 1. Crear carpeta local
```bash
mkdir axiom-news-summarizer
cd axiom-news-summarizer
```

# 2. Crear subcarpetas
```bash
mkdir axiom_summarizer tests
```

# 3. Copiar cada archivo en su lugar (usa nano o el editor que quieras)
# - axiom_summarizer/__init__.py
# - axiom_summarizer/cli.py
# - tests/test_summarizer.py
# - pyproject.toml, setup.py, requirements.txt, README.md, LICENSE, .gitignore

# 4. Inicializar git
git init
git add .
git commit -m "feat: initial AXIOM news summarizer release"

# 5. Crear repo en GitHub (web)
# Ve a https://github.com/axiom-systemstech
# Botón "New" → nombre: axiom-news-summarizer
# NO inicialices con README (ya lo tienes)

# 6. Vincular y subir
git remote add origin https://github.com/axiom-systemstech/axiom-news-summarizer.git
git branch -M main
git push -u origin main
