document.getElementById('consultar').addEventListener('click', async () => {
  const email = document.getElementById('email').value;
  const mensagemDiv = document.getElementById('mensagem');
  const respostaContainer = document.getElementById('resposta-container');
  respostaContainer.style.display = 'none';

  mensagemDiv.textContent = '🔄 Buscando informações...';

  try {
    const response = await fetch(`/api/baterias?email=${encodeURIComponent(email)}`);
    const data = await response.json();

    if (data.erro) {
      mensagemDiv.textContent = `❌ Erro: ${data.erro}`;
    } else {
      mensagemDiv.textContent = data.mensagem;

      const emailNaoEncontrado = data.mensagem.includes("❗ O email não foi encontrado na base de dados.");
      if (
        !emailNaoEncontrado &&
        data.passadas &&
        data.passadas.length > 0
      ) {
        respostaContainer.style.display = 'block';
        window.passadas = data.passadas;
      } else {
        respostaContainer.style.display = 'none';
      }
    }
  } catch (err) {
    mensagemDiv.textContent = '❌ Erro ao conectar com o servidor.';
  }
});

function mostrarPassadas(resposta) {
  const mensagemDiv = document.getElementById('mensagem');
  if (resposta === 'sim' && window.passadas) {
    let texto = '\n📜 Baterias passadas:\n';
    for (const b of window.passadas) {
      texto += `- ${b.data_agendamento} às ${b.horario_agendamento} para ${b.qtde_pessoas} pessoas\n`;
    }
    mensagemDiv.textContent += texto;
    document.getElementById('resposta-container').style.display = 'none';
  }
}
