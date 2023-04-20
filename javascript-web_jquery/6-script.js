$(document).ready(function () {
  const divHeader = $("#update_header");

  divHeader.click(function () {
    $("header").text("New Header!!!");
  });
});
