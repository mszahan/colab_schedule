const text = "Two shadows merge, weaving a tale yet to be told"; // Your text here
let i = 0;

function typeWriter() {
  if (i <text.length) {
    document.getElementById("typewriter").innerHTML += text.charAt(i);
    i++;
    setTimeout(typeWriter, 100); // Adjust the typing speed here
  } else {
    i=0;
    setTimeout(() => {
      document.getElementById("typewriter").innerHTML = '';
     typeWriter();
    }, 3000); // Adjust the time before the text restarts typing
    
  } 
}
typeWriter();