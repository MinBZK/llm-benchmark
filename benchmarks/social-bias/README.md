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

1. Installeer `uv`, een snelle Python package installer:

   ```bash
   # Volg de instructies op https://docs.astral.sh/uv/getting-started/installation/
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Run vanuit de `social-bias` folder:

   ```bash
   cd llm-benchmark/benchmarks/social-bias
   ```

3. Genereer prompts:

   ```bash
   uv run generate-prompts/prompts.py
   ```

   Of gebruik de bestaande prompts in de `prompts` map.

4. Voer de experimenten uit met de scripts in `run-experiments`:

   Voor Claude modellen:

   ```bash
   export ANTHROPIC_API_KEY="YOUR_KEY"
   uv run run-experiments/experiments_claude.py 0 100 claude-3-5-haiku yes_no_gender.csv
   ```

   Voor OpenAI modellen:

   ```bash
   export OPENAI_API_KEY="YOUR_KEY"
   uv run run-experiments/experiments_gpt.py 0 100 gpt-4o-mini yes_no_gender.csv
   ```

   Voor Hugging Face modellen:

   ```bash
   uv run run-experiments/experiments_huggingface.py 0 100 mistralai/Mistral-7B-v0.1 yes_no_gender.csv
   ```

   Alle commando's accepteren de volgende parameters in deze volgorde:
   - `start_range`: startpunt in de prompt dataset (integer)
   - `end_range`: eindpunt in de prompt dataset (integer)
   - `model`: naam van het model
   - `prompt_csv`: CSV bestand met prompts (moet in de prompts map staan)

   De resultaten worden opgeslagen in een `reactions` directory binnen de `run-experiments` map.

5. Analyseer de resultaten om bias in verschillende LLM implementaties te vergelijken

## 📚 Bronvermelding

Als je deze benchmark gebruikt, verwijs dan naar het paper en/of de thesis:

```text
Burema, R., Schuth, A., Spelt, C., & Nguyen, D. (2026). A Dutch Benchmark to Assess Social Bias in LLMs within a Hiring Decision Setting. In Proceedings of LREC 2026.
```

```text
Burema, R. (2025). Evaluating Dutch Social Bias in Large Language Models. Master's thesis.
```
