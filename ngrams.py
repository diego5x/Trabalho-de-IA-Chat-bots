import random
import re
import os
from collections import defaultdict, Counter


class NGramChatbot:
    def __init__(self, n=3):
        self.n = n
        self.model = defaultdict(Counter)
        self.start_words = []

    def _preprocess(self, text):
        text = text.lower().strip()
        tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
        return tokens

    def train(self, text):
        tokens = self._preprocess(text)
        if len(tokens) < self.n:
            return

        
        if tokens[0].isalnum():
            self.start_words.append(tuple(tokens[:self.n - 1]))

        for i in range(len(tokens) - self.n + 1):
            gram = tuple(tokens[i:i + self.n - 1])
            next_word = tokens[i + self.n - 1]
            self.model[gram][next_word] += 1

    def train_from_file(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                self.train(f.read())
            print(f"Modelo treinado com: {file_path}")
        else:
            print(f"Arquivo não encontrado: {file_path}")

    def _weighted_choice(self, counter):
        words = list(counter.keys())
        weights = list(counter.values())
        return random.choices(words, weights=weights, k=1)[0]

    def generate_response(self, seed=None, max_length=30):
        if not self.model:
            return "Eu ainda não aprendi nada."

        
        if seed:
            tokens = self._preprocess(seed)
            if len(tokens) >= self.n - 1:
                current = tuple(tokens[-(self.n - 1):])
                if current not in self.model:
                    current = random.choice(list(self.model.keys()))
            else:
                current = random.choice(list(self.model.keys()))
        else:
            current = random.choice(self.start_words or list(self.model.keys()))

        response = list(current)

        for _ in range(max_length):
            if current not in self.model:
                
                current = random.choice(list(self.model.keys()))
                response.extend(list(current))
                continue

            next_word = self._weighted_choice(self.model[current])
            response.append(next_word)

            if next_word in ".!?":
                break

            current = tuple(response[-(self.n - 1):])

        return self._format_response(response)

    def _format_response(self, tokens):
        text = " ".join(tokens)
        text = re.sub(r'\s+([?.!,;])', r'\1', text)
        text = re.sub(r'\s+', ' ', text)
        return text.capitalize()


def main():
    corpus = """
    Olá, tudo bem? Como você está hoje?
    Oi! Estou bem sim, e você?
    Estou ótimo, obrigado por perguntar.
    Que bom! Como posso te ajudar hoje?
    Você gosta de tecnologia?
    Sim, adoro aprender sobre novas tecnologias.
    Eu também gosto muito de programação.
    Programar é divertido e desafiador ao mesmo tempo.
    Você prefere Python ou JavaScript?
    Eu gosto mais de Python, acho mais simples.
    JavaScript também é muito útil para web.
    Você está estudando atualmente?
    Sim, estou estudando bastante todos os dias.
    Aprender coisas novas é sempre bom.
    Qual foi a última coisa que você aprendeu?
    Aprendi sobre inteligência artificial recentemente.
    Isso é muito interessante!
    Você já usou algum chatbot antes?
    Sim, já conversei com alguns.
    E o que você achou deles?
    Achei úteis, mas alguns são meio limitados.
    Concordo, ainda há muito a melhorar.
    Você gosta de ler livros?
    Sim, gosto bastante de leitura.
    Qual é o seu gênero favorito?
    Gosto de ficção científica.
    Eu prefiro fantasia e aventura.
    Você já assistiu algum filme recentemente?
    Sim, assisti um filme muito bom ontem.
    Do que se tratava?
    Era sobre viagens no tempo.
    Esse tema é fascinante!
    Você gosta de música?
    Sim, ouço música todos os dias.
    Qual seu estilo favorito?
    Gosto de rock e música eletrônica.
    Eu prefiro música calma para relaxar.
    Você toca algum instrumento?
    Não, mas gostaria de aprender violão.
    Aprender música é muito legal.
    Você pratica esportes?
    Sim, faço exercícios algumas vezes por semana.
    Isso é importante para a saúde.
    Você prefere manhã ou noite?
    Prefiro a noite, sou mais produtivo.
    Eu gosto da tranquilidade da manhã.
    Você trabalha ou estuda?
    Faço os dois atualmente.
    Deve ser cansativo.
    Sim, mas vale a pena.
    O que você gosta de fazer no tempo livre?
    Gosto de assistir séries e jogar.
    Eu gosto de caminhar ao ar livre.
    Contato com a natureza faz bem.
    Você tem animais de estimação?
    Sim, tenho um cachorro.
    Eu tenho um gato.
    Animais são ótimos companheiros.
    Qual sua comida favorita?
    Gosto muito de pizza.
    Eu adoro comida japonesa.
    Sushi é muito bom!
    Você sabe cozinhar?
    Sei fazer algumas coisas simples.
    Cozinhar é uma habilidade útil.
    Você já viajou para outro país?
    Ainda não, mas quero muito.
    Viajar é uma experiência incrível.
    Qual lugar você gostaria de visitar?
    Quero conhecer o Japão.
    Eu gostaria de visitar a Europa.
    Existem muitos lugares bonitos no mundo.
    Você acredita em sorte?
    Às vezes parece que sim.
    Eu acho que esforço é mais importante.
    Faz sentido.
    Você costuma planejar o futuro?
    Sim, gosto de ter objetivos.
    Ter metas ajuda bastante.
    Você prefere trabalhar sozinho ou em equipe?
    Prefiro trabalhar em equipe.
    Eu gosto de trabalhar sozinho às vezes.
    Depende da situação.
    Você gosta de aprender idiomas?
    Sim, acho muito interessante.
    Qual idioma você gostaria de aprender?
    Gostaria de aprender inglês melhor.
    Eu quero aprender espanhol.
    Aprender idiomas abre portas.
    Você usa redes sociais?
    Sim, uso todos os dias.
    Eu tento usar menos.
    Às vezes é bom desconectar.
    Você joga videogame?
    Sim, gosto bastante.
    Qual seu jogo favorito?
    Gosto de jogos de aventura.
    Eu prefiro jogos de estratégia.
    Jogos ajudam a relaxar.
    Você gosta de filmes ou séries?
    Gosto dos dois.
    Séries são boas para maratonar.
    Filmes são mais rápidos.
    Você gosta de tecnologia?
    Sim, estou sempre aprendendo mais.
    A tecnologia evolui rapidamente.
    Precisamos acompanhar.
    Você acredita em inteligência artificial?
    Sim, é o futuro.
    Já estamos vendo muitos avanços.
    Isso é só o começo.
    Você acha que robôs vão dominar o mundo?
    Espero que não!
    Provavelmente vão ajudar mais do que atrapalhar.
    Você gosta de conversar?
    Sim, conversar é sempre bom.
    Ajuda a passar o tempo.
    E também a aprender coisas novas.
    Você está feliz hoje?
    Sim, estou me sentindo bem.
    Que bom ouvir isso!
    Espero que continue assim.
    Você costuma ajudar as pessoas?
    Sempre que posso.
    Ajudar faz bem.
    Você tem sonhos?
    Sim, muitos sonhos.
    Nunca desista deles.
    Persistência é importante.
    Você gosta de café?
    Sim, adoro café.
    Eu prefiro chá.
    Ambos são ótimos.
    Você gosta de acordar cedo?
    Nem sempre.
    Eu tenho dificuldade também.
    Mas é bom quando conseguimos.
    Você acredita em mudanças?
    Sim, tudo pode mudar.
    Mudanças fazem parte da vida.
    Às vezes são difíceis.
    Mas também trazem crescimento.
    """
    bot = NGramChatbot(n=3)
    bot.train(corpus)

    print("Chatbot iniciado! (digite 'sair')")

    while True:
        try:
            user = input("\nVocê: ").strip()

            if not user:
                continue

            if user.lower() in ["sair", "exit", "quit"]:
                print("Chatbot: Até mais!")
                break

            if user.lower().startswith("treinar "):
                path = user.split(" ", 1)[1]
                bot.train_from_file(path)
                continue

            response = bot.generate_response(user)
            print("Chatbot:", response)

        except KeyboardInterrupt:
            print("\nEncerrando...")
            break


if __name__ == "__main__":
    main()
