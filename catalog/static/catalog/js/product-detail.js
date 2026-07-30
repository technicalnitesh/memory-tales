document.addEventListener("DOMContentLoaded", function () {

    console.log("Product Detail JS Loaded");

    const priceElement = document.getElementById("productPrice");
    const qtyInput = document.getElementById("qty");
    const plusBtn = document.getElementById("plusBtn");
    const minusBtn = document.getElementById("minusBtn");
    const selects = document.querySelectorAll(".product-option");

    const cartForm = document.getElementById("cartForm");
    const addToCartBtn = document.getElementById("addToCartBtn");


    if(addToCartBtn){

       addToCartBtn.addEventListener("click", function (e) {

    console.log("Button Clicked");

    e.preventDefault();

    addToCart();

});

        }

    if (!priceElement) return;

    let basePrice = parseFloat(priceElement.textContent.trim());

   function updatePrice(){

    let optionTotal = 0;

    document.querySelectorAll(".product-option").forEach(function(select){

        let selected =
            select.options[
                select.selectedIndex
            ];

        optionTotal += parseFloat(
            selected.dataset.price || 0
        );

    });

    let qty =
        parseInt(
            document.getElementById("qty").value
        );

    let singlePrice =
        basePrice + optionTotal;

    let finalPrice =
        singlePrice * qty;

    document.getElementById("optionPrice").innerText =
        optionTotal.toFixed(2);

    document.getElementById("qtyText").innerText =
        qty;

    document.getElementById("productPrice").innerText =
        finalPrice.toFixed(2);

}

  selects.forEach(function(select){

    select.addEventListener(
        "change",
        updatePrice
    );

});

    if (plusBtn) {
plusBtn.addEventListener("click",function(){

    qtyInput.value =
        parseInt(qtyInput.value)+1;

    updatePrice();

});

    }

    if (minusBtn) {

       minusBtn.addEventListener("click",function(){

    let qty =
        parseInt(qtyInput.value);

    if(qty>1){

        qty--;

        qtyInput.value=qty;

        updatePrice();

    }

});

    }

});


function changeImage(img){

    document.getElementById("mainProductImage").src = img.src;

}
const uploadBox =
document.getElementById("uploadBox");

const photoInput =
document.getElementById("photoInput");

const previewImage =
document.getElementById("previewImage");

const previewSection =
document.getElementById("previewSection");

uploadBox.addEventListener("click",function(){

    photoInput.click();

});

photoInput.addEventListener("change",function(e){

    const file=e.target.files[0];

    if(!file) return;

    const reader=new FileReader();

    reader.onload=function(event){

        previewImage.src=
        event.target.result;

        previewSection.style.display=
        "block";

    }

    reader.readAsDataURL(file);

});


$(document).on("click", "#addToCartBtn", function (e) {

    // alert("caa");

    e.preventDefault();

    let form = $("#cartForm")[0];

    let formData = new FormData(form);

    $.ajax({

        url: "/cart/add/",

        type: "POST",

        data: formData,

        processData: false,

        contentType: false,

        headers: {

            "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()

        },

        beforeSend: function () {

            $("#addToCartBtn")
                .prop("disabled", true)
                .html('<i class="fa fa-spinner fa-spin"></i> Adding...');

        },

        success: function (response) {

            console.log(response);

            $("#addToCartBtn")
                .prop("disabled", false)
                .html("🛒 Add To Cart");

            if (response.success) {

                $("#cartCount").text(response.count);

                showAlert(
                    "success",
                    "Added",
                    response.message
                );

            } else {

                showAlert(
                    "error",
                    "Error",
                    response.message
                );

            }

        },

        error: function (xhr) {

            $("#addToCartBtn")
                .prop("disabled", false)
                .html("🛒 Add To Cart");

            console.log(xhr.responseText);

            showAlert(
                "error",
                "Error",
                "Something went wrong."
            );

        }

    });

});