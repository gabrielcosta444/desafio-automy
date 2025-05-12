from dateutil.parser import parse
from datetime import datetime

def criarMensagem(baterias):
    futuras = []
    passadas = []

    if baterias is None:
        return f"❗ O email não foi encontrado na base de dados.", []
    
    for b in baterias:
        data_agendamento = parse(b['data_agendamento'], dayfirst=True)
        if data_agendamento >= datetime.today():
            futuras.append(b)
        else:
            passadas.append(b)        

    message = ""

    if futuras:
        message += "📅 Próximas baterias agendadas:\n"
        for b in futuras:
            message += f"- {b['data_agendamento']} às {b['horario_agendamento']} para {b['qtde_pessoas']} pessoas\n"
    else:
        message += "❌ Nenhuma bateria futura encontrada.\n"

    message += "\nDeseja visualizar suas baterias passadas?\n"

    return message, passadas
