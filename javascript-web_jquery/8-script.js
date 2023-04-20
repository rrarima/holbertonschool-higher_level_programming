$(document).ready(function () {
  const url = "https://swapi-api.hbtn.io/api/films/?format=json";
  const characterList = $("#list_movies");

  $.get(url, function (data) {
    data.results.forEach(function (movie) {
      const title = movie.title;
      const listItem = $("<li>").text(title);
      characterList.append(listItem);
    });
  });
});