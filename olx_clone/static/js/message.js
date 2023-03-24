let loc=window.location
let wsStart='ws://'

let input_message = $('#message')
let message_body = $('.msg-display')
let message_form = $('#message-form')
const currentDate = new Date()
const time = currentDate.toLocaleTimeString('en-US', { hour12: true });

//fetching current logged user id
const userId = $('#logged-user-id').val()

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
        let send_by = userId 
        let send_to
        
        if(userId == 3){
            send_to = 4
        }else{
            send_to = 3
        }

        let data = {
            'message':message,
            'send_by':send_by,
            'send_to':send_to
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
    let send_by_id = data['send_by']
    console.log(message);
    newMessge(message,send_by_id)
    

}
socket.onerror = async function(e){
    console.log('Error',e);
}
socket.onclose = async function(e){
    console.log('OnClose',e);
}


newMessge = (message,send_by_id) =>{

    let messageElement;
    if(send_by_id == userId){
        messageElement = `

        <div class="sent-msg">
        <span>${message} &nbsp; ${time}  </span>
        </div>
    
        `
         message_body.append($(messageElement))
    }else{
        messageElement = `

        <div class="received-msg">
        <span>${message} &nbsp; ${time}  </span>
        </div>
    
        `
         message_body.append($(messageElement))
    }


}