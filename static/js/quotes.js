var quotes = [
  ["The Net interprets censorship as damage and routes around it", "John Gilmore", "http://www.toad.com/gnu/"],
  ["It’s incredible what people can make when they’re able to fail publicly without fear, since not only will those failures not be attributed to them, but they’ll be washed away by a waterfall of new content", "Christopher ‘moot’ Poole", "http://chrishateswriting.com/post/76431353368/the-anonymity-i-know"],
  ["L'invenzione di Dio è stata resa necessaria per dare un indirizzo più preciso alle bestemmie, che prima erano troppo generiche e poco incisive", "Corrado Guzzanti", ""],
  ["Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. Code for readability.", "John F. Woods", "https://groups.google.com/forum/#!msg/comp.lang.c++/rYCO5yn4lXw/oITtSkZOtoUJ"]
]

function getrandomquote(){
  var quote = quotes[Math.floor(Math.random()*quotes.length)];
  var quote_text = quote[0];
  var quote_author = '<strong>' + quote[1] + '</strong>';
  var quote_url = '';

  if (quote[2].length > 0) {
    quote_url = ' - <a href="' + quote[2] + '">Link</a>';
  }

  return quote_text + ' - ' + quote_author + quote_url;
}
