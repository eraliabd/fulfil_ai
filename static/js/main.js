let mybutton = document.getElementById("btn-modal"),
    confirm = document.getElementById("confirm");
let up_btn = document.getElementById("up_btn");

window.onscroll = function () {
    scrollFunction();

    if (window.scrollY > 800) {
        up_btn.style.display = "block";
    } else {
        up_btn.style.display = "none";
    }
};

function scrollFunction() {
    if (
        document.body.scrollTop > 300 ||
        document.documentElement.scrollTop > 300
    ) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
    window.scrollTo({
        behavior: "smooth",
    });
}

function modalOpen(event) {
    event.preventDefault();
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
    document.getElementById("overlay").classList.add("is-visible");
    document.getElementById("modal").classList.add("is-visible");
    document.getElementById("scrollBlock").classList.add("scrollNone");
}

document.getElementById("close-btn").addEventListener("click", function () {
    document.getElementById("overlay").classList.remove("is-visible");
    document.getElementById("modal").classList.remove("is-visible");
    document.getElementById("scrollBlock").classList.remove("scrollNone");
});
document.getElementById("overlay").addEventListener("click", function () {
    document.getElementById("overlay").classList.remove("is-visible");
    document.getElementById("modal").classList.remove("is-visible");
    document.getElementById("all-confirm").classList.remove("is-visible");
    document.getElementById("scrollBlock").classList.remove("scrollNone");
});

// document.getElementsByTagName("button").addEventListener("click", function (event) {
//     event.preventDefault();
//     const confirmID = document.getElementsByTagName("button");
//     confirmID.setAttribute("id", "confirm")
//     modal.classList.remove("is-visible");
//     document.getElementById("all-confirm").classList.add("is-visible");
// });

// confirm function
confirm.addEventListener("click", function (event) {
    event.preventDefault();
    modal.classList.remove("is-visible");
    document.getElementById("all-confirm").classList.add("is-visible");
});
document
    .getElementById("confermed")
    .addEventListener("click", function (event) {
        event.preventDefault();
        document.getElementById("all-confirm").classList.remove("is-visible");
        document.getElementById("overlay").classList.remove("is-visible");
        document.getElementById("scrollBlock").classList.remove("scrollNone");
    });

$.ajax({
    type: 'GET',
    url: 'fulfil:home',
    success: function (response) {
        console.log(response)
        const data = JSON.parse(response.data)
        console.log(data)
        data.forEach(e => {
            console.log(e.field_name)
        })
    },
    error: function (error) {
        console.log(error)
    }
})
