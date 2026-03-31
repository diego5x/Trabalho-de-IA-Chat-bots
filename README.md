Este repositório contém duas implementações de chatbots com abordagens diferentes:

* **ELIZA-style em C** (baseado em regras e palavras-chave)
* **Chatbot com N-grams em Python** (baseado em modelo probabilístico)

O objetivo é demonstrar diferentes técnicas de construção de chatbots, desde abordagens simples até modelos mais dinâmicos.

---

## 1. Chatbot ELIZA (C)

### Descrição

Este chatbot simula uma conversa utilizando:

* Correspondência de palavras-chave (`strstr`)
* Respostas pré-definidas
* Respostas aleatórias para entradas genéricas

Inspirado no clássico ELIZA, ele foca em perguntas reflexivas.

### Funcionalidades

* Conversa interativa via terminal
* Detecção de emoções (ex: "triste", "feliz", "ansioso")
* Respostas contextuais simples
* Respostas aleatórias para maior variedade

### Como compilar e executar

```bash
gcc eliza.c -o eliza
./eliza
```
## 2. Chatbot com N-grams (Python)

### Descrição

Este chatbot utiliza um modelo estatístico baseado em **N-grams** para gerar respostas.

Ele aprende padrões de linguagem a partir de um corpus de texto e gera frases com base em probabilidades.

### Funcionalidades

* Treinamento com texto (corpus interno ou arquivos externos)
* Geração de respostas probabilísticas
* Suporte a diferentes tamanhos de N-gram (padrão: 3)
* Continuação de frases baseada em contexto

### Como executar

```bash
python3 ngrams.py
```

### Comandos disponíveis

* `sair`, `exit`, `quit` → encerra o chatbot
* `treinar arquivo.txt` → treina o modelo com um arquivo externo
---

## 🔍 Diferenças entre as abordagens

| Característica | ELIZA (C)         | N-grams (Python)      |
| -------------- | ----------------- | --------------------- |
| Tipo           | Baseado em regras | Probabilístico        |
| Complexidade   | Baixa             | Média                 |
| Flexibilidade  | Limitada          | Alta                  |
| Aprendizado    | Não aprende       | Aprende com dados     |
| Respostas      | Fixas/aleatórias  | Geradas dinamicamente |

---

## Tecnologias utilizadas

* **C** (stdio, string, stdlib)
* **Python 3**

  * `re`
  * `random`
  * `collections`


Se quiser, posso deixar esse README mais “estilo GitHub top” (com badges, imagens, GIF demonstrando, etc.) ou até gerar um `.md` prontinho pra você baixar.
