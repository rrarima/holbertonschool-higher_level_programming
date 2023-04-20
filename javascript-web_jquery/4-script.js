$(document).ready(function () {
  const header = $("header");
  const divHeader = $("#toggle_header");

  divHeader.click(function () {
    header.toggleClass("red green");
  });
});
