"""OrderService: API demonstrativa de cálculo de frete.

A versão principal está correta. A falha é injetada apenas em uma branch de laboratório.
"""


def calculate_shipping(base_price: float, tax_rate: str) -> float:
    """Soma preço-base e taxa de frete recebida como texto."""
    return float(base_price) + float(tax_rate)


def create_app():
    """Cria a API Flask. Import adiado para permitir testar a regra isoladamente."""
    from flask import Flask, jsonify, request

    application = Flask(__name__)

    @application.post("/shipping")
    def shipping():
        payload = request.get_json(silent=True) or {}
        try:
            price = float(payload["price"])
            tax = str(payload.get("tax", "5.50"))
            total = calculate_shipping(price, tax)
        except (KeyError, TypeError, ValueError):
            return jsonify({"error": "Parâmetros de frete inválidos"}), 400
        return jsonify({"total": total}), 200

    return application


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000)
