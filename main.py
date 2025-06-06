def teorema_de_bayes(p_a, p_b_dado_a, p_b_dado_nao_a):
    p_nao_a = 1 - p_a
    numerador = p_b_dado_a * p_a
    denominador = (p_b_dado_a * p_a) + (p_b_dado_nao_a * p_nao_a)
    p_a_dado_b = numerador / denominador

    explicacao = [
        f"Passo 1: Calcular P(¬A) = 1 - P(A) = {p_nao_a:.6f}",
        f"Passo 2: Calcular Numerador = P(B|A) * P(A) = {numerador:.6f}",
        f"Passo 3: Calcular Denominador = P(B|A)*P(A) + P(B|¬A)*P(¬A) = {denominador:.6f}",
        f"Passo 4: Calcular P(A|B) = Numerador / Denominador = {p_a_dado_b:.6f}",
    ]

    for linha in explicacao:
        print(linha)
    return p_a_dado_b, explicacao


print("==== Teorema de Bayes: Probabilidade de Spam dado Phishing ====\n")

# Dados com base em fontes reais:
p_a = 0.468  # P(Spam)
p_b_dado_a = 0.01825  # P(Phishing | Spam)
p_b_dado_nao_a = 0.0001  # P(Phishing | ¬Spam)

# Cálculo
resultado, passos = teorema_de_bayes(p_a, p_b_dado_a, p_b_dado_nao_a)
resultado_str = f"\nResultado final: P(Spam | Phishing) = {resultado:.6f} ({resultado * 100:.2f}%)"
print(resultado_str)

# Fontes
fontes = [
    "Mailmodo (2025): https://www.mailmodo.com/guides/email-spam-statistics/",
    "AAG IT (2025): https://aag-it.com/the-latest-phishing-statistics/",
    "Astra Security (2025): https://www.getastra.com/blog/security-audit/phishing-attack-statistics/"
]

print("\n=== Fontes ===")
for fonte in fontes:
    print(f"- {fonte}")

# Gerar arquivo de saída
with open("resultado_bayes.txt", "w", encoding="utf-8") as f:
    f.write("==== Teorema de Bayes: Probabilidade de Spam dado Phishing ====\n\n")
    f.write("Entradas:\n")
    f.write(f"- P(Spam) = {p_a}\n")
    f.write(f"- P(Phishing | Spam) = {p_b_dado_a}\n")
    f.write(f"- P(Phishing | ¬Spam) = {p_b_dado_nao_a}\n\n")

    f.write("Etapas do cálculo:\n")
    for passo in passos:
        f.write(passo + "\n")

    f.write(resultado_str + "\n\n")

    f.write("=== Fontes ===\n")
    for fonte in fontes:
        f.write("- " + fonte + "\n")

print("\nArquivo 'resultado_bayes.txt' gerado com sucesso.")
