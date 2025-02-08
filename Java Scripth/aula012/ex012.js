var data = new Date()
var hora = Number(data.getHours())

console.log(`Agr é ${hora} horas`)
if (hora <= 12) {
    console.log('bom dia')
} else {
    if (hora < 20) {
        console.log('boa tarde')
    } else {
        console.log('boa noite')
    }
}