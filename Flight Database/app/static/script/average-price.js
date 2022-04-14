// Enable All Tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

// Search on click
submitForm = (event, form) => {
    e.preventDefault();
    
    fetch('/search-avg-price', {
      method: 'post',
      body: JSON.stringify({
            leavingFrom: form.leavingFrom.value,
            minPrice: form.minPrice.value,
            maxPrice: form.maxPrice.value,
            maxSeat: form.maxSeat.value
        })
    }).then((response) => {
      return response.json();
    }).then((data) => {
      //Success code goes here
    }).catch((err) => {
      //Failure
    });
}