let scrollPos = 0;
const nav = document.querySelector('.site-nav');

function checkPosition() {
  let windowY = window.scrollY;
  if (windowY < scrollPos) {
    // Scrolling UP
    nav.classList.add('is-visible');
    nav.classList.remove('is-hidden');
  } else {
    // Scrolling DOWN
    nav.classList.add('is-hidden');
    nav.classList.remove('is-visible');
  }
  scrollPos = windowY;
}

window.addEventListener('scroll', checkPosition);

function tinkoffPayFunction(event) {
    if (event && event.preventDefault) {
        event.preventDefault();
    }
    var receipt = document.getElementById('receipt');
    var amount = document.getElementById('amount');
    var email = document.getElementById('email');
    var phone = document.getElementById('phone');
    var name = document.getElementById('name')

    if (amount && (email || phone || name)) {
        receipt.value = JSON.stringify({
            "Email": email,
            "Phone": phone,
            "Name": name,
            "EmailCompany": "question@shtandart.ru",
            "Taxation": "patent",
            "Items": [
                {
                    "Name": 'Пожертвование',
                    "Price": amount,
                    "Quantity": 1.00,
                    "Amount": amount,
                    "PaymentMethod": "full_prepayment",
                    "PaymentObject": "service",
                    "Tax": "none"
                }
            ]
        });
    }
    pay(event);
    return false;
}

var news = document.querySelector(".background-news");
news.style.height = getComputedStyle(news).width;