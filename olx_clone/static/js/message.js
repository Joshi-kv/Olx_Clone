let loc=window.location
let wsStart='ws://'

let input_message = $('#message')
let message_body = $('.msg_card_body')
let message_form = $('#message-form')

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

}
socket.onerror = async function(e){
    console.log('Error',e);
}
socket.onclose = async function(e){
    console.log('OnClose',e);
}
