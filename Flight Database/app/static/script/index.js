// Enable All Tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

// Search on click
submitForm = (event, form) => {
    e.preventDefault();
    
    fetch('/search', {
      method: 'post',
      body: JSON.stringify({
            leavingFrom: form.leavingFrom.value,
            goingTo: form.goingTo.value,
            departureDate: form.departureDate.value,
            arrivalDate: form.arrivalDate.value
        })
    }).then((response) => {
      return response.json();
    }).then((data) => {
      //Success code goes here
    }).catch((err) => {
      //Failure
    });
}

// Click listener for add to cart button on homepage
// Listener on entire document instead of each button
document.addEventListener('click', (event) => {

	// If the clicked element doesn't have the right selector, bail
	if (!event.target.closest('.add-to-cart')) return;

	// Don't follow the link
	event.preventDefault();

	// Log the clicked element in the console
  var row = event.target.closest('tr');
  var FlightNumber = row.firstElementChild.innerText;

  fetch('/create', {
    method: 'post',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      FlightNumber,
  })
  }).then((response) => {
    return response.json();
  }).then((data) => {
    //Success code goes here
  }).catch((err) => {
    //Failure
  });

}, false);