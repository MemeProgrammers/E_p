
const commentContainer = document.getElementById('allComments');
document.getElementById('addComments').addEventListener('click', function (ev) {
   addComment(ev);
});



function addComment(ev) {
    let commentText, wrapDiv;
    const textBox = document.createElement('div');
    const replyButton = document.createElement('button');
    replyButton.className = 'reply';
    replyButton.innerHTML = 'Reply';
    if(hasClass(ev.target.parentElement, 'container')) {
        if(document.getElementById('newComment').value.length > 0) {
        const wrapDiv = document.createElement('div');
        wrapDiv.className = 'wrapper';
        wrapDiv.style.marginLeft = 0;
        commentText = document.getElementById('newComment').value;
        document.getElementById('newComment').value = '';
        textBox.innerHTML = commentText;
        wrapDiv.append(textBox, replyButton);
        commentContainer.appendChild(wrapDiv);
    }
    } else {
        wrapDiv = ev.target.parentElement;
        commentText = ev.target.parentElement.firstElementChild.value;
        textBox.innerHTML = commentText;
        wrapDiv.innerHTML = '';
        wrapDiv.append(textBox, replyButton);
    }
  }


function hasClass(elem, className) {
    return elem.className.split(' ').indexOf(className) > -1;
}
document.getElementById('allComments').addEventListener('click', function (e) {
    if (hasClass(e.target, 'reply')) {
     
        $('.reply').hide()
        const parentDiv = e.target.parentElement;
        const wrapDiv = document.createElement('div');
        wrapDiv.style.marginLeft = (Number.parseInt(parentDiv.style.marginLeft) + 15).toString() + 'px';
        wrapDiv.className = 'wrap';
        const w = document.createElement('div');
        w.className = 'w';

        wrapDiv.style.display='flex';
        wrapDiv.style.flexDirection = 'row';
        wrapDiv.style.widthLeft+='20px;';
        const textArea = document.createElement('textarea');
        textArea.className='text_reply';
        textArea.style.marginLeft += '20px;';
        const addButton = document.createElement('button');
        addButton.className = 'addReply';
        addButton.innerHTML = 'Reply';
        const cancelButton = document.createElement('button');
        cancelButton.innerHTML = 'Cancel';
        cancelButton.className='cancelReply';
        w.append(textArea, addButton, cancelButton);
        w.style.widthLeft+='20px;'
        wrapDiv.appendChild(w);
        parentDiv.appendChild(wrapDiv);
    } else if(hasClass(e.target, 'addReply'))  {
        addComment(e);
        $('.reply').show();
        
    } else if(hasClass(e.target, 'cancelReply')) {
        e.target.parentElement.innerHTML = '';
        $('.reply').show();
        
    }
});
