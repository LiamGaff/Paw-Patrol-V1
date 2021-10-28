var stripe = Stripe("pk_test_51JSey2IdhFlB16DTWznPmmrt7w62ooXMT0k9IJgc42ZklkYeq9D2TQX9haat8Z2qYvhY49DSzcpMC2VKC9mvzmOt00NAd8fdeU");

var donationData = {
  currency: "eur",
};
// Disable the button until we have Stripe set up on the page
document.querySelector("button").disabled = true;
fetch("create_payment_intent/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(donationData)
}).then(function(result) {
    return result.json();
  })
  .then(function(data) {
    var elements = stripe.elements();
    var style = {
      base: {
        color: "#32325d",
        fontFamily: 'Arial, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
          color: "#32325d"
        }
      },
      invalid: {
        fontFamily: 'Arial, sans-serif',
        color: "#fa755a",
        iconColor: "#fa755a"
      }
    };
    var card = elements.create("card", { style: style });
    // Stripe injects an iframe into the DOM
    card.mount("#card-element");
    card.on("change", function (event) {
      // Disable the Pay button if there are no card details in the Element
      document.querySelector("button").disabled = event.empty;
      document.querySelector("#card-error").textContent = event.error ? event.error.message : "";
    });
    var form = document.getElementById("payment-form");
    form.addEventListener("submit", function(event) {
      event.preventDefault();
      // Complete payment when the submit button is clicked
      payWithCard(stripe, card, data.clientSecret, data.amount);
    });
  });
// Calls stripe.confirmCardPayment
// If the card requires authentication Stripe shows a pop-up modal to
// prompt the user to enter authentication details without leaving your page.
var payWithCard = function(stripe, card, clientSecret, amount) {
  // loading(true);
  stripe
    .confirmCardPayment(clientSecret, {
      payment_method: {
        card: card
      }
    })
    .then(function(result) {
      if (result.error) {
        // Show error to your customer
        showError(result.error.message);
      } else {
        // The payment succeeded!
        orderComplete(result.paymentIntent.id);
        alert("Thanks for your donation");
        // location.href="success/"
      }
    });
};
/* ------- UI helpers ------- */
// Shows a success message when the payment is complete
var orderComplete = function(paymentIntentId) {
  // loading(false);

  console.log("TESTING: "+paymentIntentId);
  // document.querySelector(".result-message a").setAttribute(
  //     "href",
  //     "https://dashboard.stripe.com/test/payments/"
  //   );
  // document.querySelector(".result-message").classList.remove("hidden");
  document.querySelector("button").disabled = true;
};
