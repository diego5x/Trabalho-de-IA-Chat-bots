#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <time.h>

#define MAX 256

void minusculo(char *str) {
    for (int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
}

void limpar(char *str) {
    str[strcspn(str, "\n")] = 0;
}

int main() {
    char entrada[MAX];
    srand(time(NULL));

    printf("Oi, eu sou um chatbot estilo ELIZA.\n");
    printf("Como posso lhe ajudar? (digite 'sair' para encerrar)\n");

    char *respostas[] = {
        "Interessante... me conte mais.",
        "Por que você pensa isso?",
        "Como isso faz você se sentir?",
        "Você pode explicar melhor?",
        "Entendo. Continue.",
        "Isso acontece com frequência?",
        "Você já se sentiu assim antes?",
        "O que você acha que causou isso?",
        "Isso é importante para você?",
        "Por que isso te incomoda?",
        "Fale mais sobre isso.",
        "Você gostaria que fosse diferente?",
        "O que você faria se pudesse mudar isso?",
        "Isso te deixa feliz ou triste?",
        "Você já conversou com alguém sobre isso?",
        "Como você reagiu a isso?",
        "Isso ainda te afeta?",
        "O que você espera que aconteça?",
        "Você acha que isso vai melhorar?",
        "Isso depende de você?",
        "Você costuma pensar muito sobre isso?",
        "Isso te preocupa?",
        "O que passa pela sua cabeça quando isso acontece?",
        "Você sente isso com frequência?",
        "Isso muda o seu dia?",
        "Você acha isso normal?",
        "Outras pessoas pensam assim também?",
        "Isso já aconteceu antes?",
        "Você consegue lidar bem com isso?",
        "Isso é algo recente?",
        "Você gosta de falar sobre isso?",
        "Isso te lembra alguma coisa?",
        "Você evita pensar nisso?",
        "Você considera isso importante?",
        "Isso faz parte da sua rotina?",
        "Você gostaria de mudar isso?",
        "Isso te motiva de alguma forma?",
        "Você sente controle sobre isso?",
        "Isso te deixa confuso?",
        "Você entende por que isso acontece?",
        "Isso é algo que você quer resolver?",
        "Você já tentou mudar isso?",
        "Isso te afeta muito?",
        "Você consegue ignorar isso?",
        "Isso te deixa inseguro?",
        "Você acha que isso tem solução?",
        "Isso depende de outras pessoas?",
        "Você já pediu ajuda sobre isso?",
        "Isso te incomoda muito?",
        "Você consegue explicar isso melhor?"
    };

    int total_respostas = 50;

    while (1) {
        printf("\n> ");
        fgets(entrada, MAX, stdin);

        limpar(entrada);
        minusculo(entrada);

        
        if (strcmp(entrada, "sair") == 0) {
            printf("Tchau!\n");
            break;
        }

        
        else if (strstr(entrada, "oi")) {
            printf("Olá!\n");
        }
        else if (strstr(entrada, "tudo bem")) {
            printf("Sim! E com você?\n");
        }

        
        else if (strstr(entrada, "triste") || strstr(entrada, "depress")) {
            printf("Por que você está se sentindo assim?\n");
        }
        else if (strstr(entrada, "feliz")) {
            printf("Que bom! O que te deixa feliz?\n");
        }
        else if (strstr(entrada, "raiva")) {
            printf("O que te deixa com raiva?\n");
        }
        else if (strstr(entrada, "ansioso") || strstr(entrada, "ansiedade")) {
            printf("O que está te deixando ansioso?\n");
        }
        else if (strstr(entrada, "nervoso")) {
            printf("O que está te deixando nervoso?\n");
        }
        else if (strstr(entrada, "cansado")) {
            printf("Você tem descansado o suficiente?\n");
        }
        else if (strstr(entrada, "namorada") || strstr(entrada, "namorado")) {
            printf("Como está seu relacionamento?\n");
        }
        else if (strstr(entrada, "termino") || strstr(entrada, "término")) {
            printf("Términos podem ser difíceis. Quer falar sobre isso?\n");
        }
        else if (strstr(entrada, "amor")) {
            printf("O que o amor significa para você?\n");
        }
        else if (strstr(entrada, "ciume") || strstr(entrada, "ciúme")) {
            printf("Você acha que o ciúme é saudável?\n");
        }
        else if (strstr(entrada, "amigo")) {
            printf("Você confia nos seus amigos?\n");
        }
        else if (strstr(entrada, "pai")) {
            printf("Como é sua relação com seu pai?\n");
        }
        else if (strstr(entrada, "mae") || strstr(entrada, "mãe")) {
            printf("Você conversa bastante com sua mãe?\n");
        }
        else if (strstr(entrada, "familia") || strstr(entrada, "família")) {
            printf("Sua família é importante para você?\n");
        }
        else if (strstr(entrada, "prova")) {
            printf("Prova sempre dá nervosismo. Você estudou bastante?\n");
        }
        else if (strstr(entrada, "faculdade")) {
            printf("Como está sendo sua experiência na faculdade?\n");
        }
        else if (strstr(entrada, "professor")) {
            printf("O que você acha dos seus professores?\n");
        }
        else if (strstr(entrada, "estudo")) {
            printf("Você gosta de estudar?\n");
        }
        else if (strstr(entrada, "trabalho")) {
            printf("Você gosta do seu trabalho?\n");
        }
        else if (strstr(entrada, "dinheiro")) {
            printf("Você se preocupa com dinheiro?\n");
        }
        else if (strstr(entrada, "futuro")) {
            printf("Você pensa muito sobre o seu futuro?\n");
        }
        else if (strstr(entrada, "sonho")) {
            printf("Qual é o seu maior sonho?\n");
        }
        else if (strstr(entrada, "eu sinto")) {
            printf("Por que você sente isso?\n");
        }
        else if (strstr(entrada, "eu quero")) {
            printf("O que te impede de conseguir isso?\n");
        }
        else if (strstr(entrada, "não consigo")) {
            printf("Por que você acha que não consegue?\n");
        }
        else if (strstr(entrada, "eu acho")) {
            printf("Por que você acha isso?\n");
        }
        else if (strstr(entrada, "por que")) {
            printf("O que você acha?\n");
        }
        else if (strstr(entrada, "como")) {
            printf("Como você acha que isso poderia acontecer?\n");
        }
        else if (strstr(entrada, "chato")) {
            printf("O que está te entediando?\n");
        }
        else if (strstr(entrada, "tedio") || strstr(entrada, "tédio")) {
            printf("O que você gosta de fazer quando está entediado?\n");
        }
        else if (strstr(entrada, "problema")) {
            printf("Quer me contar mais sobre esse problema?\n");
        }

        else {
            int r = rand() % total_respostas;
            printf("%s\n", respostas[r]);
        }
    }

    return 0;
}