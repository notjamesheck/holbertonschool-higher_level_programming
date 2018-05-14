$(() => {
  $('DIV#red_header').css({ 'color': '#FF0000' }).click(() => {
    $('header').css({ 'color': '#FF0000' });
  });
});
