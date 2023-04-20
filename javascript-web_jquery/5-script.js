$(document).ready(function () {
  const divHeader = $("#add_item");

  divHeader.click(function () {
    $("UL.my_list").append("<li>Item</li>");
  });
});
