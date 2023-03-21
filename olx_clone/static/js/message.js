let loc=window.location
let wsStart='ws://'

let input_message = $('#message')
let message_body = $('.msg-display')
let message_form = $('#message-form')
const currentDate = new Date()
const time = currentDate.toLocaleTimeString('en-US', { hour12: true });


if(loc.protocol === 'htpps'){
    wsStart='wss://'
}

let endpoint = wsStart + loc.host + loc.pathname

var socket = new WebSocket(endpoint)


// called when connection successfully established
socket.onopen = async function(e){
    console.log('open',e);
    message_form.submit(function(e){
        e.preventDefault()
        let message = input_message.val()
        let data = {
            'message':message
        }
        data = JSON.stringify(data)
        //sending msg to server
        socket.send(data)
        $(this)[0].reset()
    })
}

socket.onmessage = async function(e){
    console.log('onmessage',e);
    let data = JSON.parse(e.data)
    let message = data['message']
    console.log(message);
    newMessge(message)
    

}
socket.onerror = async function(e){
    console.log('Error',e);
}
socket.onclose = async function(e){
    console.log('OnClose',e);
}


newMessge = (message) =>{
    let messageElement = `

    <div class="sent-msg">
    <span>${message} &nbsp; ${time}  </span>
    </div>

    `
     message_body.append($(messageElement))
}