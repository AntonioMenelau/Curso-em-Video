function carrega() {
    var foto = window.document.getElementById('foto')
    var msg = window.document.getElementById('msg')
    var agora = new Date()
    var hora = agora.getHours()
    console.log(hora)
    msg.innerHTML = `Agora são ${hora} horas`
    if (hora >= 0 && hora < 12) {
        /*bom dia*/
        foto.innerHTML = '<img src="imagens/fotodia.jpg" alt="foto dia">'
        document.body.style.background = "#fff564"
    } else if (hora >= 12 && hora <= 18) {
        /*boa tarde*/
        foto.innerHTML = '<img src="imagens/fototarde.jpg" alt="foto tarde">'
        document.body.style.background = "#f8b34b"
    } else {
        /*boa noite*/
        foto.innerHTML = '<img src="imagens/fotonoite.jpg" alt="foto noite">'
        document.body.style.background = "#1e1d8f"
    }
}