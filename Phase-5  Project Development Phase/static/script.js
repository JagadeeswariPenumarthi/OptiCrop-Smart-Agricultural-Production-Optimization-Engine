// OptiCrop - basic client-side niceties

document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form.crop-form");
  if (!form) return;

  form.addEventListener("submit", function (event) {
    const inputs = form.querySelectorAll("input[required]");
    let valid = true;

    inputs.forEach(function (input) {
      if (input.value.trim() === "" || isNaN(parseFloat(input.value))) {
        valid = false;
        input.style.borderColor = "#e53935";
      } else {
        input.style.borderColor = "#c8c8c8";
      }
    });

    if (!valid) {
      event.preventDefault();
      alert("Please enter valid numeric values in every field before predicting.");
    }
  });
});
