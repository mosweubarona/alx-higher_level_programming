$('document').ready(() => {
  const translate = (code) => {
    $.ajax({
      url: `https://stefanbohacek.com/hellosalut/?lang=${code}`,
      dataType: 'json',
      success: (result) => {
        $('DIV#hello').text(result.hello);
      }
    });
  };

  $('INPUT#btn_translate').on('click', () => {
    const text = $('INPUT#language_code').val();
    translate(text);
  });
})
