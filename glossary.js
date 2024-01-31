let data = [
    ["Процессор", "центральное устройство компьютера, производящее обработку информации в двоичном коде."],
    ["Оперативная память", "устройство, в котором хранятся программы и данные."],
    ["Биссектриса", "крыса, которая бегает по углам и делит угол пополам"]
];

let ol = document.getElementsByTagName("ol")[0];
data.forEach((v) => {ol.innerHTML += `<li><b>${v[0]}</b> - ${v[1]}</li>`});
document.getElementsByTagName("img")[0].setAttribute("src", `img${Math.floor(Math.random() * 4)}.png`)