

const buttonPress = document.querySelectorAll("#btn");
const opt = document.getElementById("options");
const custom_style={
    userSelect: "all",
    color: "white"
}
let value = "";

console.log(value);
buttonPress.forEach((button)=>{
    button.addEventListener("click", code);

    function code() {
        console.log(button.value);

        value = value.concat(button.value);
        console.log(value);
        
        if(value === "395248"){
              opt.href = "./options.zip";
              console.log("IT'S ME");
            }
        }
});

