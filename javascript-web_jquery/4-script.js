const header = $('header');
const divHeader = $('#toggle_header');

divHeader.click(function() {
  if (header.hasClass('red')){
    header.removeClass('red').addClass('green');
  } else {
    header.removeClass('green').addClass('red');
  }
});
