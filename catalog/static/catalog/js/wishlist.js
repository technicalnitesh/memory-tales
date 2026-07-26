function initWishlist(){

    

    document.querySelectorAll(".wishlist-toggle").forEach(button=>{

        button.onclick=function(){

            let productId=this.dataset.product;

            fetch("/wishlist/toggle/",{

                method:"POST",

                headers:{

                    "X-CSRFToken":csrfToken,

                    "X-Requested-With":"XMLHttpRequest",

                    "Content-Type":"application/x-www-form-urlencoded"

                },

                body:new URLSearchParams({

                    product_id:productId

                })

            })

            .then(response=>response.json())

         .then(data => {

    if (!data.success) {

        return;

    }

    const icon = this.querySelector("i");

    if (data.added) {

        // Add Wishlist

        icon.classList.remove("bi-heart");
        icon.classList.add("bi-heart-fill");

        this.classList.add("active");

        showAlert(
            "success",
            "Added",
            "Product added to wishlist."
        );

    } else {

        // Remove Wishlist

        icon.classList.remove("bi-heart-fill");
        icon.classList.add("bi-heart");

        this.classList.remove("active");

        showAlert(
            "info",
            "Removed",
            "Product removed from wishlist."
        );

        // Wishlist page se card remove

        const card = this.closest(".wishlist-item");

        if (card) {

            card.style.transition = "all .35s ease";

            card.style.opacity = "0";

            card.style.transform = "scale(.95)";

            setTimeout(function () {

                card.remove();

                updateWishlistPage();

            }, 350);

        }

    }

    // Navbar Count Update

    const count = document.getElementById("wishlistCount");

    if (count) {

        count.innerText = data.count;

    }

})
.catch(error => {

    console.log(error);

});

        };

    });

}
function updateWishlistPage() {

    const container = document.getElementById("wishlistContainer");

    if (!container) {

        return;

    }

    const cards = container.querySelectorAll(".wishlist-item");

    if (cards.length === 0) {

        container.innerHTML = `

        <div class="col-12">

            <div class="text-center py-5">

                <i class="bi bi-heart display-1 text-muted"></i>

                <h3 class="mt-4">

                    Your Wishlist is Empty

                </h3>

                <p class="text-muted">

                    Save your favourite products here.

                </p>

                <a href="/products/" class="btn btn-primary mt-3">

                    Browse Products

                </a>

            </div>

        </div>

        `;

    }

}

initWishlist();
