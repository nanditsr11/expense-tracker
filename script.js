document.addEventListener("DOMContentLoaded", () => {
    fetch('/api/get_expenses')
        .then(response => response.json())
        .then(data => {
            const expenseList = document.getElementById("expenseList");
            expenseList.innerHTML = "<ul>" + data.map(expense => `<li>${expense[1]} - ${expense[2]}: $${expense[3]} - ${expense[4]}</li>`).join('') + "</ul>";
        });
});
