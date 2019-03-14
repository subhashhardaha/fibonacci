function copyFunction() {
  /* Get the text field */
  var copyText = document.getElementById("fibonacci_value").innerHTML;;
  console.log(copyText);
  /* Select the text field */
  const el = document.createElement('textarea');
  el.value = copyText;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);

  /* Alert the copied text */
  alert("Copied Successfull");
}