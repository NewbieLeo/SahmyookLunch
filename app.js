const menu = JSON.parse(JSON.stringify(data)).data;
const currentDay = new Date().getDate();
const todayMenu = menu[currentDay];
const [breakfast, lunch, dinner] = todayMenu;
console.log(todayMenu)

allergyEmojis = {
     1: "🥚",
     2: "🥛",
     3: "🫒",
     4: "🥜",
     5: "🟢",
     6: "🌾",
     7: "🐟",
     8: "🦀",
     9: "🦐",
    10: "🐷",
    11: "🍑",
    12: "🍅",
    13: "🧪",
    14: "🌰",
    15: "🐔",
    16: "🐮",
    17: "🦑",
    18: "🦪"
};

const fillBox = (name) => {
    allergyInfo = new Set();
    eval(name).forEach((v) => {
        let $meal = document.createElement("p");
        let sep = separateMenuName(v);
        $meal.innerHTML = sep[0];
        if (sep[1] != null) {
            sep[1].forEach((v, i) => {
                allergyInfo.add(v.replace(".", ""));
            });
        }
        $meal.classList.add("meal");
        console.log(allergyInfo);
        document.querySelector(`#${name}`).appendChild($meal);
    })
    let $allergy = document.createElement("p");
    $allergy.innerHTML = getAllergy(allergyInfo);
    $allergy.classList.add("allergy");
    document.querySelector(`#${name}`).appendChild($allergy);
};

const separateMenuName = (name) => {
    const allergy = name.match(/[\d]+\./g);
    const matched = (allergy == null) ? "" : allergy.join("");
    return [name.replace(" (" + matched + ")", ""), allergy];
};

const getAllergy = (set) => {
    set = Array.from(set).sort();
    let result = new String();
    set.forEach((v) => {
        result += allergyEmojis[v];
    })
    return result;
};

["breakfast", "lunch", "dinner"].forEach(fillBox);
