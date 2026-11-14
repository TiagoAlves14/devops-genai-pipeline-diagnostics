"""Injeta a falha do laboratório: executar APENAS na branch feature."""
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "app.py"
original = "return float(base_price) + float(tax_rate)"
buggy = "return base_price + tax_rate  # ERRO INTENCIONAL: float + str"
text = p.read_text(encoding="utf-8")
if original not in text:
    raise SystemExit("Não foi possível injetar: código original não encontrado.")
p.write_text(text.replace(original, buggy, 1), encoding="utf-8")
print("Falha intencional injetada em app.py.")
