from auth import getToken
from query_service import buscarBaterias
from output import criarMensagem

def main():
    try:
        email = input("Digite o e-mail do cliente: ").strip()
        token = getToken()
        baterias = buscarBaterias(token, email)
        message, passadas = criarMensagem(baterias)

        print("\n" + message)
        resposta = input("> ").strip().lower()

        if resposta == "sim":
            print("\n📜 Baterias passadas:")
            for b in passadas:
                print(f"- {b['data_agendamento']} às {b['horario_agendamento']} para {b['qtde_pessoas']} pessoas")
        else:
            print("✅ Obrigado!")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
