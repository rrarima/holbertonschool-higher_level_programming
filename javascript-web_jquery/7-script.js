$(document).ready(function () {
  const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  const characterDiv = $("#character");

  $.get(url, function (data) {
    characterDiv.text(data.name);
  });
});