const API_URL = "http://localhost:8000/api/kindergartens";
let modalInstance;

document.addEventListener("DOMContentLoaded", () => {
    modalInstance = new bootstrap.Modal(document.getElementById('kinderModal'));
    fetchData();
});

// 1. Ma'lumotlarni olish (READ)
async function fetchData() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();
        renderTable(data);
    } catch (error) {
        console.error("Xatolik:", error);
        alert("Ma'lumotlarni yuklashda xatolik!");
    }
}

function renderTable(data) {
    const tbody = document.getElementById("tableBody");
    tbody.innerHTML = "";

    data.forEach(item => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>#${item.id}</td>
            <td class="fw-bold">${item.name}</td>
            <td>${item.region}, ${item.district}</td>
            <td>${item.price.toLocaleString()} so'm</td>
            <td><span class="badge bg-warning text-dark"><i class="fas fa-star me-1"></i>${item.rating}</span></td>
            <td>
                <button class="btn btn-sm btn-primary me-2" onclick="editItem(${item.id})">
                    <i class="fas fa-edit"></i>
                </button>
                <button class="btn btn-sm btn-danger" onclick="deleteItem(${item.id})">
                    <i class="fas fa-trash"></i>
                </button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

// 2. Modalni ochish (Yangi qo'shish uchun)
function openModal() {
    document.getElementById("kinderForm").reset();
    document.getElementById("kinderId").value = ""; // ID bo'sh bo'lsa - yangi qo'shish
    document.getElementById("modalTitle").innerText = "Yangi bog'cha qo'shish";
    modalInstance.show();
}

// 3. Tahrirlash uchun ma'lumotni yuklash
async function editItem(id) {
    try {
        const response = await fetch(`${API_URL}/${id}`);
        const item = await response.json();

        // Formani to'ldiramiz
        document.getElementById("kinderId").value = item.id;
        document.getElementById("name").value = item.name;
        document.getElementById("region").value = item.region;
        document.getElementById("district").value = item.district;
        document.getElementById("type").value = item.type;
        document.getElementById("price").value = item.price;
        document.getElementById("rating").value = item.rating;
        document.getElementById("short_description").value = item.short_description || "";
        document.getElementById("image").value = item.image || "";
        document.getElementById("programs").value = (item.programs || []).join(", ");
        document.getElementById("languages").value = (item.languages || []).join(", ");

        // Batafsil qism (agar backenddan kelsa)
        document.getElementById("location_address").value = item.location_address || "";
        document.getElementById("phone").value = item.phone || "";
        document.getElementById("ages").value = item.ages || "";
        document.getElementById("full_description").value = item.full_description || "";

        document.getElementById("modalTitle").innerText = "Tahrirlash";
        modalInstance.show();
    } catch (error) {
        alert("Ma'lumotni o'qishda xatolik");
    }
}

// 4. Saqlash (Create yoki Update)
async function saveData() {
    const id = document.getElementById("kinderId").value;
    const isUpdate = id !== "";

    // Formadagi ma'lumotlarni yig'amiz
    const data = {
        name: document.getElementById("name").value,
        region: document.getElementById("region").value,
        district: document.getElementById("district").value,
        type: document.getElementById("type").value,
        price: parseInt(document.getElementById("price").value),
        rating: parseFloat(document.getElementById("rating").value),
        short_description: document.getElementById("short_description").value,
        image: document.getElementById("image").value,

        // Massivlarni yasash
        programs: document.getElementById("programs").value.split(",").map(s => s.trim()).filter(s => s),
        languages: document.getElementById("languages").value.split(",").map(s => s.trim()).filter(s => s),

        // Batafsil
        location_address: document.getElementById("location_address").value,
        phone: document.getElementById("phone").value,
        ages: document.getElementById("ages").value,
        full_description: document.getElementById("full_description").value
    };

    const url = isUpdate ? `${API_URL}/${id}` : API_URL;
    const method = isUpdate ? "PUT" : "POST";

    try {
        const response = await fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            modalInstance.hide();
            fetchData(); // Jadvalni yangilash
            alert(isUpdate ? "Yangilandi!" : "Qo'shildi!");
        } else {
            alert("Xatolik yuz berdi");
        }
    } catch (error) {
        console.error(error);
        alert("Server bilan aloqa yo'q");
    }
}

// 5. O'chirish (DELETE)
async function deleteItem(id) {
    if (confirm("Rostdan ham o'chirmoqchimisiz?")) {
        try {
            await fetch(`${API_URL}/${id}`, { method: "DELETE" });
            fetchData();
        } catch (error) {
            alert("O'chirishda xatolik");
        }
    }
}