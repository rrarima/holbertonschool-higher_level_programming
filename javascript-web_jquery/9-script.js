$(document).ready(function () {
  const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  const helloDiv = $("#hello");

  $.get(url, function (data) {
    const helloText = data.hello;
    helloDiv.text(helloText);
  });
});