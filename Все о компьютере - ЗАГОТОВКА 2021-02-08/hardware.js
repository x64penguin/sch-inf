let harware_list = [
    ["Intel Core i3", 70],
    ["HDD 500GB", 120],
    ["Monitor 17 inches", 180],
    ["RAM 16GB", 60],
    ["Компьютерная крыса", 30],
    ["Башня на проц", 50],
    ["Видяшка", 300]
];

let table = document.getElementsByClassName("hardware_table")[0];
harware_list.forEach((v, idx) => {
    table.innerHTML += `<tr>
        <td class="row_index">${idx + 1}</td>
        <td>${v[0]}</td>
        <td>${v[1]}</td>
    </tr>`; // i love xss
});