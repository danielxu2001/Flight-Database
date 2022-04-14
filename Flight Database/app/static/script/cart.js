// Enable All Tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

var editDescriptionModal = document.getElementById('edit-description-modal');
editDescriptionModal.addEventListener('show.bs.modal',  (event) => {
  // Button that triggered the modal
  var button = event.relatedTarget;
  var row = button.closest('tr');
  var FlightNumber = row.firstElementChild.innerText;
  var Description = row.querySelector(".flight-description").innerText; // idx of description

  var modalBodyTextArea = document.getElementById('description');
  modalBodyTextArea.textContent = Description;
  
  var saveChangesButton = document.getElementById('editDescriptionFinal');

  editDescription = (event) => {
    // Don't follow the link
    event.preventDefault();

    fetch('/update', {
        method: 'post',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            FlightNumber,
            Description: modalBodyTextArea.value
        })
      }).then((response) => {
        return response.json();
      }).then((data) => {
        //Success code goes here
      }).catch((err) => {
        //Failure
      });
      event.target.removeEventListener('click', editDescription, false);
    }
    
    // If the function or object, is already in the list of event listeners for this target, they are not added a second time.
    saveChangesButton.addEventListener('click', editDescription);
})

var removeFromCartModal = document.getElementById('remove-from-cart-modal');
removeFromCartModal.addEventListener('show.bs.modal',  (event) => {
  // Button that triggered the modal
  var button = event.relatedTarget;
  var row = button.closest('tr');
  var FlightNumber = row.firstElementChild.innerText;
  
  var button2 = document.getElementById('removeFromCartFinal');

  removeFromCart = (event) => {
    // Don't follow the link
    event.preventDefault();
    
    fetch(`/delete/${FlightNumber}`, {
        method: 'post',
      }).then((response) => {
        return response.json();
      }).then((data) => {
        //Success code goes here
      }).catch((err) => {
        //Failure
      });
      

      event.target.removeEventListener('click', removeFromCart, false);
    }

    // If the function or object, is already in the list of event listeners for this target, they are not added a second time.
    button2.addEventListener('click', removeFromCart);
})
