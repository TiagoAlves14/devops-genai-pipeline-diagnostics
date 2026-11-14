# Checklist — Projeto Integrador DevOps + GenAI

## Preparação de código
- [x] Analisar a Unidade 5 e o exemplo do laboratório.
- [x] Definir nome e estrutura do repositório.
- [x] Criar API OrderService, testes, agente e configuração GitLab CI.
- [x] Criar script reprodutível de injeção de falha.
- [x] Criar workflow GitHub Actions de testes.
- [ ] Confirmar o workflow verde no repositório remoto GitHub.

## Execução no GitLab (evidências exigidas pelo fórum)
- [ ] Criar o repositório no GitLab.
- [ ] Espelhar o código da `main` e obter pipeline de testes aprovado.
- [ ] Configurar `OPENAI_API_KEY` mascarada com acesso restrito.
- [ ] Opcional: cadastrar `GITLAB_API_TOKEN` para comentários em MRs.
- [ ] Criar `feature/falha-frete`, injetar TypeError e abrir Merge Request.
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
