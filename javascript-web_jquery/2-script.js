$(document).ready(function () {
  const header = $("header");
  const divHeader = $("#red_header");

  header.css("color", "#FF0000");

  divHeader.click(function () {
    $(this).css("color", "#FF0000");
  });
});
