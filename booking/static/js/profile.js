jalaliDatepicker.startWatch();

function saveProfile(event) {
    event.preventDefault();
  
    let fullName = document.getElementById('fullName').value;
    let email = document.getElementById('email').value;
    let address = document.getElementById('address').value;
    let phoneNumber = document.getElementById('phone-number').value;
    let birthDate = document.getElementById('birth-date').value;
  
    document.getElementById('fullName').disabled = true;
    document.getElementById('email').disabled = true;
    document.getElementById('phone-number').disabled = true;
    document.getElementById('birth-date').disabled = true;
    document.getElementById('address').disabled = true;
  
    alert('Profile saved successfully!');
  }
  
  function editProfile() {
    document.getElementById('fullName').disabled = false;
    document.getElementById('email').disabled = false;
    document.getElementById('phone-number').disabled = false;
    document.getElementById('birth-date').disabled = false;
    document.getElementById('address').disabled = false;
  }
  
  window.onload = function () {
    document.getElementById('fullName').disabled = true;
    document.getElementById('email').disabled = true;
    document.getElementById('phone-number').disabled = true;
    document.getElementById('birth-date').disabled = true;
    document.getElementById('address').disabled = true;
  };
  
  document.getElementById('profileForm').addEventListener('submit', saveProfile);