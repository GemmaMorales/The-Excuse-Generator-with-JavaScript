/* eslint-disable */

import "../assets/img/rigo-baby.jpg";
import "../assets/img/4geeks.ico";
//import 'breathecode-dom'; //DOM override to make JS easier to use
import "../style/index.scss";

window.onload = async function() {
  console.log("Hello Rigo from the console!");
  const r = await fetch(
    "https://3000-d686684e-b46a-40bc-82c3-f8f6328ae63c.ws-us02.gitpod.io/api/excuse"
  );
  document.querySelector(".alert").innerHTML = await r.json();
};
