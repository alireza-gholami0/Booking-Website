const signUp = document.getElementById("signUp-form");
const error = document.getElementsByClassName("error")[0];



function handleSubmit(e) {
  e.preventDefault();

  let password = document.getElementById("pwd").value;
  let acceptPass = document.getElementById("acceptPass").value;

  if (password !== acceptPass) {
    error.innerHTML = `
        <div class="toast" data-autohide="false">
        <div class="toast-header bg-danger">
            <strong class="mr-auto text-white">خطا</strong>
            <button type="button" class="close" style="margin-right:auto;" data-dismiss="toast">&times;</button>
        </div>
        <div class="toast-body">
            عدم تطابق رمز های عبور !
        </div>
        </div>`;
    $(".toast").toast({ autohide: false }).toast("show");
  } else {
    alert("success");
  }
}

signUp.addEventListener("submit", handleSubmit);


