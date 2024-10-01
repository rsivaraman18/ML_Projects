function signup()
    {
        document.querySelector(".login-form-container").style.cssText = "display: none;";
        document.querySelector(".signup-form-container").style.cssText = "display: block;";
        document.querySelector(".container").style.cssText = "background: linear-gradient(to bottom, rgb(56, 189, 149),  rgb(28, 139, 106));";
        document.querySelector(".button-1").style.cssText = "display: none";
        document.querySelector(".button-2").style.cssText = "display: block";

    };



function login()
    {
        document.querySelector(".signup-form-container").style.cssText = "display: none;";
        document.querySelector(".login-form-container").style.cssText = "display: block;";
        document.querySelector(".container").style.cssText = "background: linear-gradient(to bottom, rgb(6, 108, 224),  rgb(14, 48, 122));";
        document.querySelector(".button-2").style.cssText = "display: none";
        document.querySelector(".button-1").style.cssText = "display: block";

    }



function validateForm() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("cpassword").value;
    var phone = document.getElementsByName("phone")[0].value;
    var username = document.getElementsByName("username")[0].value;
    var location = document.getElementsByName("location")[0].value;
    // Username validation for letters only
    if (!/^[A-Za-z]+$/.test(username)) {
        alert("Username must contain only letters.");
        return false;
    }

    if (!/^[A-Za-z\s]+$/.test(location)) { // Allow spaces for location names consisting of more than one word
            alert("Location must contain only letters.");
            return false;
        }



    // Check if passwords match
    if (password !== confirmPassword) {
        alert("Passwords and Confirm Password do not ");
        return false;
    }

    // Check for phone number validity
    if (!/^[6789]\d{9}$/.test(phone)) {
        alert("Invalid Phone Number, with phone number start must be 6,7, 8, or 9");
        return false;
    }

    // Validate password
    var passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).+$/;
    if (!passwordPattern.test(password)) {
        alert("Password must contain at least 1 symbol, 1 lowercase letter, 1 uppercase letter, and 1 number.");
        return false;
    }

    return true;
   }