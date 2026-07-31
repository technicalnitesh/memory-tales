$(document).ready(function () {

    $(document).on(

        "click",

        ".plusQty, .minusQty",

        function () {

            let button = $(this);

            let cartItemId = button.data("id");

            let action = button.hasClass("plusQty")
                ? "plus"
                : "minus";

            $.ajax({

                url: "/cart/update/",

                type: "POST",

                data: {

                    cart_item_id: cartItemId,

                    action: action

                },
                success: function (response) {

                    if (response.success) {

                        $("#qty" + cartItemId).text(

                            response.quantity

                        );

                        $("#itemTotal" + cartItemId).text(

                            response.item_total.toFixed(2)

                        );

                        $("#grandTotal").text(

                            response.grand_total.toFixed(2)

                        );
                        $("#grandTotalFinal").text(

                            response.grand_total.toFixed(2)

                        );

                    }

                },

                error: function () {

                    alert(

                        "Unable to update cart."

                    );

                }

            });

        }

    );

    $(document).on(

    "click",

    ".removeCartItem",

    function(){

        let itemId = $(this).data("id");

        showConfirm(

            "Remove Item",

            "Are you sure you want to remove this item from cart?",

            function(){

                $.ajax({

                    url:"/cart/remove/",

                    type:"POST",

                    data:{

                        item_id:itemId

                    },

                    success:function(response){

                        if(response.success){

                            $("#cartItem"+itemId).fadeOut(300,function(){

                                $(this).remove();

                            });

                            $("#grandTotal").text(

                                response.grand_total.toFixed(2)

                            );
                            $("#grandTotalFinal").text(

                                response.grand_total.toFixed(2)

                            );

                            $("#cartCount").text(

                                response.cart_count

                            );

                            showAlert(

                                "success",

                                "Removed",

                                "Item removed successfully."

                            );

                        }

                    }

                });

            }

        );

    }

    );

});