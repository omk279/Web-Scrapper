let page = 1;

function loadProducts(p = 1) {
    page = p;
    fetch(`api/products.php?page=${page}`)
        .then(res => res.json())
        .then(data => {
            let html = "";
            data.products.forEach(tv => {
                html += `
                    <div class="card">
                        <img src="${tv.image_url}">
                        <h4>${tv.product_name}</h4>
                        <p>₹${tv.price}</p>
                        <a href="${tv.product_url}" target="_blank">View</a>
                    </div>
                `;
            });
            document.getElementById("products").innerHTML = html;

            let pg = "";
            for (let i = 1; i <= data.pages; i++) {
                pg += `<button onclick="loadProducts(${i})">${i}</button>`;
            }
            document.getElementById("pagination").innerHTML = pg;
        });
}

loadProducts();
