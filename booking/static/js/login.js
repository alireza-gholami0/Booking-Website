// const error = document.getElementsByClassName("error")[0];
// const loginForm = document.getElementById("login-form");
//
// function handleSubmit(e) {
//   e.preventDefault();
//
//   let email = document.getElementById("email").value;
//   let password = document.getElementById("pwd").value;
//
//   if (email === "test@email.com" && password === "password123") {
//     console.log('fix');
//     window.location.href = "../home.html";
//   } else {
//     error.innerHTML = `
//         <div class="toast" data-autohide="false">
//         <div class="toast-header bg-danger">
//           <strong class="mr-auto text-white">خطا</strong>
//           <button type="button" class="close" style="margin-right:auto;" data-dismiss="toast">&times;</button>
//         </div>
//         <div class="toast-body">
//          ایمیل یا رمز عبور اشتباه است
//         </div>
//       </div>`;
//     $(".toast").toast({ autohide: false }).toast("show");
//   }
// };
//
// loginForm.addEventListener("submit", handleSubmit);

const error = document.getElementsByClassName("error")[0];
const loginForm = document.getElementById("login-form");

function handleSubmit(e) {
  e.preventDefault();

  let email = document.getElementById("email").value;
  let password = document.getElementById("pwd").value;

  var data = {
    email: email,
    password: password
  };

  $.ajax({
    type: 'POST',
    url: '/api/login/',
    data: data,
    dataType: 'json',
    success: function (response) {
      localStorage.setItem('access_token', response.access);
      localStorage.setItem('refresh_token', response.refresh);
      $('#message').html('<p class="text-dark">' + data.password + '</p>');
      window.location.href = 'signup/';
    },
    error: function (xhr, status, error) {
      error.innerHTML = `
        <div class="toast" data-autohide="false">
        <div class="toast-header bg-danger">
          <strong class="mr-auto text-white">خطا</strong>
          <button type="button" class="close" style="margin-right:auto;" data-dismiss="toast">&times;</button>
        </div>
        <div class="toast-body">
         ایمیل یا رمز عبور اشتباه است 
        </div>
      </div>`;
      $(".toast").toast({ autohide: false }).toast("show");
    }
  });
};

loginForm.addEventListener("submit", handleSubmit);