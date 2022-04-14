// Enable All Tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})
// document.onload = ()=>{
//   fetch('/search', {
//     method: 'post',
//     body: JSON.stringify({
//           leavingFrom: form.leavingFrom.value,
//           goingTo: form.goingTo.value,
//           departureDate: form.departureDate.value,
//           arrivalDate: form.arrivalDate.value
//       })
//   }).then((response) => {
//     return response.json();
//   }).then((data) => {
//     //Success code goes here
//   }).catch((err) => {
//     //Failure
//   });

// }
