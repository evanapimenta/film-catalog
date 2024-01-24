document.addEventListener('DOMContentLoaded', function() {
   var dropdownItems = document.querySelectorAll(".dropdown-menu .dropdown-item.text-light");
  
   dropdownItems.forEach(function(dropdownItem) {
      dropdownItem.addEventListener("click", function() {
         dropdownItems.forEach(function(item) {
            item.classList.remove("fw-bold");
            item.classList.remove("text-dark");
            item.style.backgroundImage = "";
            item.style.transition = "ease-in 0.2s";

         });
         this.classList.add("fw-bold");
         this.classList.add("text-dark");
         this.style.backgroundImage = "linear-gradient(45deg, #e5bbce, #646897)";
         this.style.transition = "ease-in 0.2s"
      });
   });



});
