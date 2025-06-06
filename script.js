function calcularBayes() {
    // 
    // Calcula P(A|B) usando o Teorema de Bayes.
    // Fórmula: P(A|B) = [P(B|A) * P(A)] / [P(B|A) * P(A) + P(B|¬A) * P(¬A)]

    // Args:
    //     p_a (float): Probabilidade de A (P(A)).
    //     p_b_dado_a (float): Probabilidade de B dado A (P(B|A)).
    //     p_b_dado_nao_a (float): Probabilidade de B dado não A (P(B|¬A)).

    // Returns:
    //     float: Probabilidade de A dado B (P(A|B)).
    // 

    const pA = parseFloat(document.getElementById('pA').value);
    const pBgivenA = parseFloat(document.getElementById('pBgivenA').value);
    const pBgivenNotA = parseFloat(document.getElementById('pBgivenNotA').value);
  
    //Dados com base em fontes reais:
    //Fonte: Mailmodo (https://www.mailmodo.com/guides/email-spam-statistics/)
    //- P(Spam) ≈ 46.8% => p_a = 0.468
    //- P(Phishing | Spam) ≈ 1.825% => p_b_dado_a = 0.01825
    // - P(Phishing | ¬Spam) ≈ 0.01% => p_b_dado_nao_a = 0.0001 

    const pNotA = 1 - pA;
    const numerador = pBgivenA * pA;
    const denominador = (pBgivenA * pA) + (pBgivenNotA * pNotA);
    const pAgivenB = numerador / denominador;
  
    const resultadoDiv = document.getElementById('resultado');
    resultadoDiv.innerHTML = `
      <h2>Resultado:</h2>
      <p>Passo 1: Calcular P(¬A) = 1 - P(A) = ${pNotA.toFixed(6)}</p>
      <p>Passo 2: Calcular Numerador = P(B|A) * P(A) = ${numerador.toFixed(6)}</p>
      <p>Passo 3: Calcular Denominador = P(B|A)*P(A) + P(B|¬A)*P(¬A) = ${denominador.toFixed(6)}</p>
      <p>Passo 4: Calcular P(A|B) = Numerador / Denominador = ${pAgivenB.toFixed(6)}</p>
      <h3>P(Spam | Phishing) = ${pAgivenB.toFixed(6)} (${(pAgivenB * 100).toFixed(2)}%)</h3>
    `;
  }
  