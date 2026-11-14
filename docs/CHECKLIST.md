# Checklist — Projeto Integrador DevOps + GenAI

## Preparação de código
- [x] Analisar a Unidade 5 e o exemplo do laboratório.
- [x] Definir nome, estrutura e criar repositório público no GitHub.
- [x] Criar API OrderService, testes, agente e configuração GitLab CI.
- [x] Criar script reprodutível de injeção de falha.
- [x] Criar workflow GitHub Actions de testes.
- [x] Confirmar workflow GitHub Actions verde na primeira execução (run #1).

## Execução no GitLab (evidências exigidas pelo fórum)
- [x] Criar o repositório no GitLab: https://gitlab.com/tiagoalvess14/devops-genai-pipeline-diagnostics
- [x] Espelhar código da `main` e obter pipeline aprovado — #3068321629, job #18032305039, 9 passed (0,09s).
- [ ] Configurar `OPENAI_API_KEY` mascarada com acesso restrito.
- [ ] Opcional: cadastrar `GITLAB_API_TOKEN` para comentários em MRs.
- [x] Criar `feature/falha-frete` no GitHub, injetar TypeError e sincronizar com GitLab (GitHub Actions run #43600981535, tentativa 2: sucesso).\n- [ ] Abrir Merge Request de `feature/falha-frete` para `main` no GitLab.
- [ ] Verificar falha no `unit_test` e acionamento de `ai_debugger`.
- [ ] Examinar `diagnosis.md` da IA (não confundir com um exemplo simulado).
- [ ] Validar diagnóstico e correção, reexecutando os testes.
- [ ] Registrar links dos jobs, MR e evidências sem segredos.

## Entrega
- [ ] Documentar dificuldades reais e limitações da GenAI.
- [ ] Finalizar `docs/POSTAGEM_FORUM.md` com fatos verificados.
- [ ] Publicar o fórum com link GitLab.

## Extensões opcionais
- [ ] Container Docker e deploy de homologação.
- [ ] Observabilidade de logs, métricas e traces.
