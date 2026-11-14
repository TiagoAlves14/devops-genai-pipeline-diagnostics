"""Testes locais e determinísticos do pré-processamento do agente."""
from genai_analyst import scrub, build_prompt


def test_scrub_openai_key():
    assert "sk-" not in scrub("chave: sk-abcdefghijklmnop")


def test_scrub_gitlab_token():
    assert "glpat-" not in scrub("token: glpat-abcdefghijklmnop")


def test_build_prompt_with_log_and_diff():
    prompt = build_prompt("TypeError: float + str", "- return x + y")
    assert "TypeError" in prompt
    assert "- return x + y" in prompt
    assert "não confiáveis" in prompt
