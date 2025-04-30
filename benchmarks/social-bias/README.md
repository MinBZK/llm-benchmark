# 🧠 Social Bias Benchmark

Deze Social Bias benchmark is het resultaat van de masterthesis van Renate Burema bij
het [AI Validation Team](https://minbzk.github.io/ai-validation/). De volledige thesis
is [hier](master_thesis_burema.pdf) te vinden. 📝

## 🎯 Doel

Deze benchmark meet sociale bias in Large Language Models (LLMs) binnen een Nederlandse beroepscontext. Het onderzoekt
hoe LLMs reageren op sollicitaties op basis van:

- 👩‍💼👨‍💼 Geslacht (man/vrouw)
- 🌍 Herkomst (Nederlands/buitenlands)
- 📛 Naam (typisch Nederlands/buitenlands)

## 🔬 Methodologie

De benchmark gebruikt twee soorten prompts:

1. **Yes/No** ✅❌ - Directe ja/nee vragen over geschiktheid van kandidaten
2. **Accept/Reject** 👍👎 - Vragen over het aannemen of afwijzen van kandidaten

Elke prompt heeft verschillende formuleringsvarianten om de robuustheid van de resultaten te verzekeren.

## 📦 Inhoud

Deze map bevat:

- [💻 Code voor het genereren van prompts](generate-prompts) - Python scripts om systematisch prompts te maken
- [📊 Onderliggende data](generate-prompts/experiments_data) - Datasets met Nederlandse beroepen, namen en herkomstlanden
- [📋 Gegenereerde prompts](prompts) - CSV bestanden met de prompts gebruikt in de experimenten:
  - `yes_no_gender.csv` - Ja/nee vragen op basis van geslacht
  - `yes_no_name.csv` - Ja/nee vragen op basis van naam
  - `accept_reject_gender.csv` - Aannemen/afwijzen vragen op basis van geslacht
  - `accept_reject_name.csv` - Aannemen/afwijzen vragen op basis van naam
- [⚙️ Code voor het uitvoeren van experimenten](run-experiments) - Scripts voor verschillende LLM platforms:
  - `experiments_huggingface.py` - Voor Huggingface modellen
  - `experiments_gpt.py` - Voor OpenAI modellen
  - `experiments_claude.py` - Voor Anthropic modellen

## 🚀 Gebruik

1. Genereer prompts met de scripts in `generate-prompts` of gebruik de bestaande prompts in `prompts`
2. Voer de experimenten uit met de scripts in `run-experiments`
3. Analyseer de resultaten om bias in verschillende LLM implementaties te vergelijken

## 📚 Bronvermelding

Als je deze benchmark gebruikt, verwijs dan naar de thesis:

```text
Burema, R. (2025). Evaluating Dutch Social Bias in Large Language Models.
```
