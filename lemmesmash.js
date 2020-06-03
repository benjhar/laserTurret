function getValue() {
  let value = document.getElementById("textarea").value;

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "", true);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.setRequestHeader("Value", value)
  xhr.send(JSON.stringify({
      "value": value
  }));
}
