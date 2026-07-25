// ===============================
// Sweet Alert Helper
// ===============================

function showAlert(icon, title, message) {

    Swal.fire({

        icon: icon,

        title: title,

        text: message,

        confirmButtonColor: "#6f42c1",

        confirmButtonText: "OK",

        allowOutsideClick: false,

        allowEscapeKey: true,

        customClass: {
            popup: "memory-alert"
        }

    });

}

// ===============================
// Confirm Dialog
// ===============================

function showConfirm(title, message, callback) {

    Swal.fire({

        icon: "question",

        title: title,

        text: message,

        showCancelButton: true,

        confirmButtonText: "Yes",

        cancelButtonText: "No",

        confirmButtonColor: "#6f42c1",

        cancelButtonColor: "#6c757d",

        allowOutsideClick: false

    }).then((result) => {

        if (result.isConfirmed) {

            callback();

        }

    });

}