const btn = document.querySelector('#pronto')


btn.addEventListener('click', () => {
    var time = 41
    const tittle = document.createElement('h1')
    tittle.innerHTML = 'Estamos medindo o seu peso'
    const subtittle = document.createElement('h3')
    subtittle.innerHTML = 'Aguarde'
    const body_m = document.querySelector('.input')
    body_m.innerHTML = ''
    body_m.append(tittle)
    console.log(body_m)
    body_m.append(subtittle)
    const timer = document.createElement('p')
    body_m.append(timer)
    let inter = setInterval(() => {
        if (time === 16) {
            subtittle.innerHTML = 'Parece que estamos tendo problemas...'
        }else if (time === 1) {
            window.location.assign('/dados/error')
            clearInterval(inter)
        }
        timer.innerHTML = --time
        }, 1000)
})