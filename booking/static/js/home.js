jalaliDatepicker.startWatch();

const allTabs = document.querySelectorAll(".nav-pills .nav-item .nav-link");
let currentTabs = document.querySelector(".nav-pills .nav-item .nav-link.active").getAttribute("href");

allTabs.forEach(function (tab) {
    handleClick(tab);
});

function handleClick (tab, event) {
    tab.addEventListener("click", function (e) {
        e.preventDefault();
        currentTabs = this.getAttribute("href");

        const aboutFlight = document.getElementsByClassName("about-flight")[0];
        const aboutTrain = document.getElementsByClassName("about-train")[0];
        const aboutHotel = document.getElementsByClassName("about-hotel")[0];

        switch(currentTabs) {
            case "#pills-flight":
                aboutFlight.style.display = 'block';
                aboutTrain.style.display = 'none';
                aboutHotel.style.display = 'none';
                break;
            
            case "#pills-train":
                aboutFlight.style.display = 'none';
                aboutTrain.style.display = 'block';
                aboutHotel.style.display = 'none';
                break;
            
            case '#pills-hotel':
                aboutFlight.style.display = 'none';
                aboutTrain.style.display = 'none';
                aboutHotel.style.display = 'block';
                break; 
        }
    });
}