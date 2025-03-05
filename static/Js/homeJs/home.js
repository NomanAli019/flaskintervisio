function moveto_employesignup(){
    const joinsection1 = document.getElementById("joinus-sect1");
    const joinsection2 = document.getElementById("joinussect2");

    joinsection2.classList.remove("joinus-sect2contdisp");
    joinsection1.style.display = "none";
}

function moveto_joinus(){
    const joinsection1 = document.getElementById("joinus-sect1");
    const joinsection2 = document.getElementById("joinussect2");

    joinsection2.classList.add("joinus-sect2contdisp");
    joinsection1.style.display = "block";
}

var globalFullNameemp;
var globalEmailemp;
var globalPasswordemp;
var phonenumberemp;
var youraddressemp;
var countryemp;

function validateForm() {
    globalFullNameemp = document.getElementById("fullName").value.trim();
    globalEmailemp = document.getElementById("email").value.trim();
    globalPasswordemp = document.getElementById("password").value.trim();
    
    console.log("Full Name:", globalFullNameemp);
    console.log("Email:", globalEmailemp);
    console.log("Password:", globalPasswordemp);

    moveto_employeecont();
    return false;
}

function validatecompForm(event) {
    event.preventDefault();

    phonenumberemp = document.getElementById("phonenumber").value.trim();
    youraddressemp = document.getElementById("Youraddress").value.trim();
    countryemp = document.getElementById("country").value.trim();

    if (!phonenumberemp || !youraddressemp || !countryemp) {
        alert("Please fill out all fields.");
        return false;
    }

    console.log("Full Name:", globalFullNameemp);
    console.log("Email:", globalEmailemp);
    console.log("Password:", globalPasswordemp);
    console.log("Phone number:", phonenumberemp);
    console.log("Home Address:", youraddressemp);
    console.log("Country:", countryemp);

    registerEmployee();
}

function registerEmployee() {
    const employeeData = {
        full_name: globalFullNameemp,
        email: globalEmailemp,
        password: globalPasswordemp,
        phone_number: phonenumberemp,
        house_address: youraddressemp,
        country: countryemp
    };

    fetch("/callbacks/register-employee/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(employeeData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("✅ Employee registered successfully!");
        } else {
            alert("❌ Error: " + data.message);
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("❌ Failed to register. Please try again later.");
    });
}

function moveto_employeecont() {
    const joinsection2 = document.getElementById("joinussect2");
    const joinsection3 = document.getElementById("joinus-sect3");

    joinsection3.style.display = "block";
    joinsection2.style.display = "none";
}

function moveto_joinsect2(){
    const joinsection2 = document.getElementById("joinussect2");
    const joinsection3 = document.getElementById("joinus-sect3");

    joinsection3.classList.add("joinus-sect2contdisp");
    joinsection2.classList.remove("joinus-sect2contdisp");
}
