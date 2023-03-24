
    const chatButton = document.querySelector('#chat-button');
    const chatBoxContainer = document.querySelector('#chat-box');

    chatButton.addEventListener('click', () => {
        // Add your chat box HTML code here
        chatBoxContainer.innerHTML = `
        <div class="productDetails">
        <span >{{product.name}}</span>
        <span >₹{{product.price}}</span>
    </div>
    <div class="msg-display">
        <div class="date">
            <h4><span>{{day_name}}</span>,&nbsp;{{day}}&nbsp;{{month}}</h4>
        </div>
        <div class="received-msg">
            <span> Hello &nbsp; {{time}}</span>
        </div>
        <div class="sent-msg">
            <span>Hi &nbsp; {{time}}</span>
        </div>
    </div>
    <div class="type-box">
        <form id="message-form" >
            <i class="fa-sharp fa-solid fa-paperclip paperclip" ></i>
            <input type="text"  id="message" placeholder="Type your message .....">
            <div class="sent-btn">
                <button type="submit"><i class="fa-regular fa-paper-plane"></i></button>
                <i class="fa-solid fa-microphone"></i>
            </div>
        </form>
    </div>
        `;
    });

