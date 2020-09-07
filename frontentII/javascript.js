const tabs = document.querySelectorAll('[data-tab-target]') 
//selects all the different tabs in html
const tabContents = document.querySelectorAll('[data-tab-content]')
//Tab Contents contain all the different tab contents in the html

//loop through each tab, add an event listener for each tab when clicked
tabs.forEach(tab => {
  tab.addEventListener("click", () => {
    const target = document.querySelector(tab.dataset.tabTarget)
    //grab the relevant tab target in html based on what tab is clicked on the page.
    //loop through each tab content, remove 'active' class- make them disappear
    tabContents.forEach(tabContent => {
      tabContent.classList.remove("active") //make only the tab clicked active
    })
    tabs.forEach(tab => {
      tab.classList.remove("active")
    })//create class for css styling
    tab.classList.add("active")
    target.classList.add("active")  
  })
})     
