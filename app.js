const API_URL = "https://jsonplaceholder.typicode.com/users";


async function fetchUsers() {
  const response = await fetch(API_URL);

  if (!response.ok) {
    throw new Error("Napaka pri pridobivanju podatkov");
  }

  return response.json();
}

function renderUsers(users) {
  const list = document.getElementById("user-list");
  list.innerHTML = "";

  users.forEach(user => {
    const li = document.createElement("li");
    li.textContent = `${user.name} (${user.email})`;
    list.appendChild(li);
  });
}


async function main() {
  try {
    const users = await fetchUsers();
    renderUsers(users);
  } catch (error) {
    document.getElementById("test-result").textContent =
      "✖️ Napaka: " + error.message;
  }
}

