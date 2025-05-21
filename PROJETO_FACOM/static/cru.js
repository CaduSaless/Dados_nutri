const inp = document.querySelector('#cpf')
inp.addEventListener('input', (el) => {
    let valor = inp.value
    let tam = inp.value.length
    console.log(el)
    console.log(el.data)
    if (el.data != null) {
        if (tam == 3 || tam == 7) {
            inp.value =  `${valor}.`
            console.log(valor)
        } else if (tam == 11) {
            inp.value =  `${valor}-`
            console.log(valor)
        }
    }
})

const variaveis = document.querySelector('.variaveis-py')
const progresso = document.querySelector('.completado')
const texto = document.querySelector('h3')
texto.innerHTML = `${100 - Number(variaveis.innerHTML)}% Completado`
progresso.style.transition = "width 0.7s ease-out";
progresso.style.width = `${variaveis.innerHTML}%`
