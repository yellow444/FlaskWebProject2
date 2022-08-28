//upload.js
$(document).ready(function () {
    $('#Upload').click(function (e) {
        e.stopPropagation();
        e.preventDefault();
        var form_data = new FormData($('#formdata')[0]);
        if (form_data.getAll('file')[0].name == '') {
            alert('Please Upload File');
            return;
        }
        $.ajax({
            type: 'POST',
            url: '/',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function (data) {
                //var msg = document.getElementById('msg');
                //msg.textContent = data.msg
                var usrInput = document.getElementById('usrInput');
                usrInput.textContent = data.usrInput
                var usrOutput = document.getElementById('usrOutput');
                usrOutput.textContent = data.usrOutput
                var textarea = document.getElementById("usrInput");
                textarea.style.backgroundColor = data.color;
            },
        });
    });
});