# DevOps GenAI — Pipeline Failure Diagnostics

Projeto acadêmico para colocar em prática o conteúdo aplicado durante as aulas.

Laboratório baseado na **Unidade 5 — Projeto Integrador** de *Manutenção, DevOps e Operações com Ferramentas de Inteligência Artificial Generativa* (UFG/AKCIT).

**Objetivo:** usar testes automatizados para identificar uma falha intencional no cálculo de frete de uma API REST, gerar um diagnóstico assistido por GenAI a partir dos logs e validar a recomendação antes de corrigi-la.

## Componentes
- `app.py` — OrderService simplificado em Python/Flask (implementação correta na `main`).
- `test_app.py` — testes unitários e do endpoint HTTP.
- `test_analyst.py` — testes determinísticos do preparo do prompt.
- `genai_analyst.py` — analisa `pytest.log` e diff e gera `diagnosis.md`; nunca modifica código.
- `.gitlab-ci.yml` — jobs `unit_test` e `ai_debugger`.
- `.github/workflows/ci.yml` — CI para verificar a versão do GitHub.
- `scripts/inject_bug.py` — gera falha `float + str` somente em branch experimental.
- `docs/CHECKLIST.md` e `docs/POSTAGEM_FORUM.md` — roteiro da atividade.

## Execução local

```sh
python -m venv .venv
source .venv/bin/activate   # PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q test_app.py test_analyst.py
```

**A `main` deve passar nos testes**. Para reproduzir a falha, crie uma branch:

```sh
git switch -c feature/falha-frete
python scripts/inject_bug.py
python -m pytest -q test_app.py test_analyst.py
```

A falha esperada é `TypeError: unsupported operand type(s) for +: 'float' and 'str'`.

## GitLab para o fórum

A atividade exige link e evidências de **GitLab CI/CD**, por isso este GitHub é a vitrine do código e o GitLab será usado para a execução demonstrativa. Envie este código a um repositório GitLab e confirme o pipeline verde da `main`; abra um Merge Request com a falha controlada na branch `feature/falha-frete`. O job `unit_test` deverá falhar e `ai_debugger` deverá produzir `diagnosis.md`.

Configure `OPENAI_API_KEY` de forma segura em **GitLab → Settings → CI/CD → Variables**. Uma chamada à API pode gerar custos. Opcionalmente, forneça `GITLAB_API_TOKEN` com permissões mínimas para publicar o relatório como comentário no MR. Sem o token opcional, o relatório será preservado apenas como artefato. Sem a chave OpenAI, o agente indica explicitamente que **nenhuma análise com GenAI foi realizada**.

**Segurança:** use somente logs fictícios e não publique tokens, chaves ou informações pessoais. A remoção automática de segredos não garante proteção integral. O diagnóstico é preliminar, requer revisão humana e testes de regressão; o agente não aplica alterações automaticamente.

## Entrega

Documente com capturas e links: `main` verde; MR e `unit_test` falho; análise real do `ai_debugger`; recomendação validada; correção e testes novamente verdes. Complete `docs/POSTAGEM_FORUM.md` com fatos comprovados, sem inventar resultados.

**Referência:** material da Unidade 5, UFG/AKCIT; exemplo indicado no PDF: https://gitlab.com/tornis1/devops-genai-lab.
