//Special Feature: All <h2> text fades in from a blur. Original pin @ https://codepen.io/dudleystorey/pen/pRLMrE//
function splitWords() {
  let quote = document.querySelector("h2"); //This tells the script what tag to look for in index.html; in this case, it's only <h2> tags.//
  quote.innerText.replace(/(<([^>]+)>)/ig, "");
  quotewords = quote.innerText.split(" "),
    wordCount = quotewords.length;
  quote.innerHTML = "";
  for (let i = 0; i < wordCount; i++) {
    quote.innerHTML += "<span>" + quotewords[i] + "</span>"; 
    if (i < quotewords.length - 1) {
      quote.innerHTML += " ";
    }
  }
  quotewords = document.querySelectorAll("h2");
  fadeWords(quotewords);
}

function getRandom(min, max) {
  return Math.random() * (max - min) + min;
}

function fadeWords(quotewords) {
  Array.prototype.forEach.call(quotewords, function(word) {
    let animate = word.animate([{
      opacity: 0,
      filter: "blur(" + getRandom(2, 5) + "px)"
    }, {
      opacity: 1,
      filter: "blur(0px)"
    }], {
      duration: 1000,
      delay: getRandom(500, 3300),
      fill: 'backwards'
    })
  })
}

splitWords();

//Please ask before copying my code if you're interested in using it.//
//Remember kids, stealing code is bad unless you take it from codepen! :D //

