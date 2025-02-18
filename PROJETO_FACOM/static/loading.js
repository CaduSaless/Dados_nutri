const btn = document.querySelector('#Pronto')


btn.addEventListener('click', btn => {
    var time = 0
    const tittle = document.createElement('h1')
    tittle.innerHTML = 'Estamos medindo o seu peso'
    const subtittle = document.createElement('p')
    subtittle.innerHTML = 'Aguarde'
    const body_m = document.querySelector('.container')
    body_m.innerHTML = ''
    body_m.append(tittle)
    console.log(body_m)
    body_m.append(subtittle)
    const timer = document.createElement('p')
    body_m.append(timer)
    setInterval(() => {
        console.log('entrou')
        timer.innerHTML = ++time}, 1000)
})