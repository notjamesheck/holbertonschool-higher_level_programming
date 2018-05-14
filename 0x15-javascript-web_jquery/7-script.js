let character = '';
$(() => {
  $.get('https://swapi.co/api/people/5/?format=json', function (data) {
    character = data.name;
    $('DIV#character').replaceWith(character);
  });
});
