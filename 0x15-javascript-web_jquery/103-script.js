$('document').ready(() => {
  const translate = () => {
    const code = $('INPUT#language_code').val();
    $.ajax({
      url: `https://stefanbohacek.com/hellosalut/?lang=${code}`,
      dataType: 'json',
      success: (result) => {
        $('DIV#hello').text(result.hello);
      }
    });
  };

  $('INPUT#btn_translate').on('click', () => {
    translate();
  });

  $(document).keypress((e) => {
    if (e.key === 'Enter') translate();
  });
});
