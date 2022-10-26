$('document').ready(() => {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    dataType: 'json',
    success: (result) => {
      $('DIV#hello').text(result.hello);
    }
  });
});
