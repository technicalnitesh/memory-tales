let currentSearch = "";

let currentSort = "";

let currentCategory = "";

let currentPage = 1;

let currentMinPrice = "";

let currentMaxPrice = "";

// ===============================
// Load Products
// ===============================

function loadProducts() {

    let url = "/products/?";
    url += "page=" + currentPage + "&";

    if (currentSearch) {
        url += "search=" + encodeURIComponent(currentSearch) + "&";
    }

    if (currentSort) {
        url += "sort=" + currentSort + "&";
    }

    if (currentCategory) {
        url += "category=" + currentCategory + "&";
    }
    if(currentMinPrice){

    url += "min_price=" + currentMinPrice + "&";

}

if(currentMaxPrice){

    url += "max_price=" + currentMaxPrice + "&";

}

    fetch(url, {

        headers: {
            "X-Requested-With": "XMLHttpRequest"
        }

    })

    .then(response => response.json())

    .then(data => {

        document.getElementById("productContent").outerHTML = data.html;

        initEvents();
        // Remove previous active class

document.querySelectorAll(".category-filter")
.forEach(item => {

    item.classList.remove("active-category");

});

// Add active class

if(currentCategory){

    const activeCategory = document.querySelector(
        '.category-filter[data-category="' + currentCategory + '"]'
    );

    if(activeCategory){

        activeCategory.classList.add("active-category");

    }

}

    });

}

// ===============================
// Events
// ===============================

function initEvents(){

    // Search

    const searchForm =
        document.getElementById("searchForm");

    if(searchForm){

        searchForm.addEventListener("submit",function(e){

            e.preventDefault();

            currentSearch = this.search.value;
            currentPage = 1;

            loadProducts();

        });

    }

    // Sort

    const sortForm =
        document.getElementById("sortForm");

    if(sortForm){

        sortForm.addEventListener("change",function(){

            currentSort = this.sort.value;
            currentPage = 1;

            loadProducts();

        });

    }

    // Category

    document.querySelectorAll(".category-filter")

    .forEach(item=>{

        item.addEventListener("click",function(e){

            e.preventDefault();

            currentCategory = this.dataset.category;

            currentPage = 1;

            loadProducts();

        });

    });

    document.querySelectorAll(".pagination-link")

.forEach(item => {

    item.addEventListener("click", function(e){

        e.preventDefault();

        currentPage = this.dataset.page;

        loadProducts();

    });

});

const priceBtn = document.getElementById("priceFilterBtn");

if (priceBtn) {

    priceBtn.addEventListener("click", function () {

        let min = parseFloat(document.getElementById("minPrice").value) || 0;
        let max = parseFloat(document.getElementById("maxPrice").value) || 0;

        if (min && max && max < min) {

            showAlert(
                "warning",
                "Invalid Price Range",
                "Maximum price cannot be less than Minimum price."
            );

            document.getElementById("maxPrice").focus();

            return; // loadProducts() nahi chalega
        }

        currentMinPrice = min;
        currentMaxPrice = max;
        currentPage = 1;

        loadProducts();

    });

}

}

// ===============================

initEvents();

const clearBtn = document.getElementById("clearFilterBtn");

if (clearBtn) {

    clearBtn.addEventListener("click", function () {

        // Reset Variables
        currentSearch = "";
        currentCategory = "";
        currentSort = "";
        currentMinPrice = "";
        currentMaxPrice = "";
        currentPage = 1;

        // Reset Search Box
        const searchInput = document.getElementById("searchInput");
        if (searchInput) {
            searchInput.value = "";
        }

        // Reset Price
        document.getElementById("minPrice").value = "";
        document.getElementById("maxPrice").value = "";

        // Reset Sort Dropdown
        const sortSelect = document.querySelector('select[name="sort"]');
        if (sortSelect) {
            sortSelect.selectedIndex = 0;
        }

        // Remove Active Category
        document.querySelectorAll(".category-filter").forEach(item => {
            item.classList.remove("active-category");
        });

        // Load All Products
        loadProducts();

    });

}

const minInput = document.getElementById("minPrice");

const maxInput = document.getElementById("maxPrice");

if (minInput && maxInput) {

    minInput.addEventListener("input", function () {

        if (this.value !== "") {

            maxInput.min = this.value;

        }

    });

}

