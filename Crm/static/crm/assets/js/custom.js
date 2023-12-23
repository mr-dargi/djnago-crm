// When the user clicks on the status part in the page, 
// toggle between hiding and showing the dropdown content
const dropbtn = document.getElementsByClassName("dropbtn");

for(let i = 0; i < dropbtn.length; i++) {
  dropbtn[i].addEventListener("click", () => {
    const myDropdown = document.getElementsByClassName("myDropdown");
    myDropdown[i].classList.toggle("show");
  });
}

// Close the dropdown if the user clicks outside of 
// the status part in the page
window.onclick = event => {
  if (!event.target.matches('.dropbtn')) {
    let dropdowns = document.getElementsByClassName("dropdown-content");
    for (let i = 0; i < dropdowns.length; i++) {
      let openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}