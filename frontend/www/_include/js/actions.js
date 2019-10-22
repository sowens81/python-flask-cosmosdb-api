// Validate the DJ Registration Password Matches.

function djMatchPassword(){
    let match_password = document.getElementById("password")
    , validate_password = document.getElementById("validate_password")
    , validate_password_response = document.getElementById("validate_password_response");
    
    if(match_password .value != validate_password.value) {
        validate_password.setCustomValidity("Password does not Match!");
        validate_password_response.style.color = 'red';
        validate_password_response.innerHTML = 'Password does not Match!';
    } else {
        validate_password.setCustomValidity("Password Matches");
        validate_password_response.style.color = 'green';
        validate_password_response.innerHTML = 'Password Matches';
    }
}

validate_password.onkeyup = djMatchPassword;

// Check the DJ Registration Password against Regex .

function  djValidatePassword(){
    var password = document.getElementById("password").value
    , password_response = document.getElementById("password_response")
    , pass_length =  password.length;

    if (pass_length < 8) {
        password_response.style.color = 'red';
        password_response.innerHTML =  'The password is not valid!<br>At least 8 charachters';
        return;
    }

    re = /[0-9]/;
    if(!re.test(password)) {
        password_response.style.color = 'red';
        password_response.innerHTML =  'The password is not valid!<br>At least one number.';
        return;
    }
    re = /[a-z]/;
    
    if(!re.test(password)) {
        password_response.style.color = 'red';
        password_response.innerHTML =  'The password is not valid!<br>At least One lowercase character';
        return;
    }

    re = /[A-Z]/;
    if(!re.test(password)) {
        password_response.style.color = 'red';
        password_response.innerHTML = 'The password is not valid!<br>At least One Uppercase  character';
        return;
    }

    password_response.style.color = 'green';
    password_response.innerHTML = 'Password Valid';
    return;

}

password.onchange = djValidatePassword;

// Validate the Label Registration Password Matches.

function labelMatchPassword(){
    let label_match_password = document.getElementById("label_password")
    , label_validate_password = document.getElementById("label_validate_password")
    , label_validate_password_response = document.getElementById("label_validate_password_response");
    if(label_match_password.value != label_validate_password.value) {
        label_validate_password.setCustomValidity("Password does not Match!");
        label_validate_password_response.style.color = 'red';
        label_validate_password_response.innerHTML = 'Password does not Match!';
    } else {
        label_validate_password.setCustomValidity("Password Matches");
        label_validate_password_response.style.color = 'green';
        label_validate_password_response.innerHTML = 'Password Matches';
    }
}

label_validate_password.onkeyup = labelMatchPassword;

// Check the Label Registration Password against Regex.

function  labelValidatePassword(){
    var label_password = document.getElementById("label_password").value
    , label_password_response = document.getElementById("label_password_response")
    , pass_length =  label_password.length;

    if (pass_length < 8) {
        label_password_response.style.color = 'red';
        label_password_response.innerHTML =  'The password is not valid!<br>At least 8 charachters';
        return;
    }

    re = /[0-9]/;
    if(!re.test(label_password)) {
        label_password_response.style.color = 'red';
        label_password_response.innerHTML =  'The password is not valid!<br>At least one number.';
        return;
    }
    re = /[a-z]/;
    
    if(!re.test(label_password)) {
        label_password_response.style.color = 'red';
        label_password_response.innerHTML =  'The password is not valid!<br>At least One lowercase character';
        return;
    }

    re = /[A-Z]/;
    if(!re.test(label_password)) {
        label_password_response.style.color = 'red';
        label_password_response.innerHTML = 'The password is not valid!<br>At least One Uppercase  character';
        return;
    }

    label_password_response.style.color = 'green';
    label_password_response.innerHTML = 'Password Valid';
    return;

}

label_password.onchange = labelValidatePassword;

// Send registration data to api.

function djRegistration() {
    
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://0.0.0.0:8000/register');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var userInfo = JSON.parse(xhr.responseText);
            document.getElementById('registration_response').innerHTML = "Thankyou for Registering!"
            document.getElementById('form_response').style.display = "none";
        }
    };
    xhr.send(JSON.stringify({
        firstname: document.getElementById('dj_firstname').value ,
        lastname: document.getElementById('dj_lastname').value,
        email: document.getElementById('dj_email').value,
        password: document.getElementById('password').value})
    );
}


