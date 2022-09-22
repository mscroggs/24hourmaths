let cookie_settings = "expires=Mon, 01 Jan 2024 12:00:00 UTC; path=/; SameSite=Lax";

let zone = "BST"

let difference_to_gmt = {
    "BST": [1, 0],
    "GMT": [0, 0],
    "GMT+1": [1, 0],
    "GMT+2": [2, 0],
    "GMT+3": [3, 0],
    "GMT+4": [4, 0],
    "GMT+5": [5, 0],
    "GMT+6": [6, 0],
    "GMT+7": [7, 0],
    "GMT+8": [8, 0],
    "GMT+9": [9, 0],
    "GMT+10": [10, 0],
    "GMT+11": [11, 0],
    "GMT+12": [12, 0],
    "GMT-1": [-1, 0],
    "GMT-2": [-2, 0],
    "GMT-3": [-3, 0],
    "GMT-4": [-4, 0],
    "GMT-5": [-5, 0],
    "GMT-6": [-6, 0],
    "GMT-7": [-7, 0],
    "GMT-8": [-8, 0],
    "GMT-9": [-9, 0],
    "GMT-10": [-10, 0],
    "GMT-11": [-11, 0],
    "GMT-12": [-12, 0],
}

decoded_cookie = decodeURIComponent(document.cookie)
ca = decoded_cookie.split(";")
for (let i = 0; i < ca.length; i++) {
    let c = ca[i]
    while (c.charAt(0) == " "){c = c.substring(1);}
    if (c.indexOf("tz=") == 0){
        zone = c.substring(3);
    }
}

function change_timezone_dropdown(tz){
    zone = tz
    document.cookie = "tz=" + tz + "; " + cookie_settings
    update_timezones()
}

ee = document.getElementsByClassName("bst-time")[0]

function update_timezones(){
    es = document.getElementsByClassName("bst-time")
    for (let i = 0; i < es.length; i++){
        let h = parseInt(es[i].dataset["hour"])
        let m = parseInt(es[i].dataset["minute"])
        // Convert BST -> GMT
        h -= 1
        // Convert GMT -> timezone
        h += difference_to_gmt[zone][0]
        m += difference_to_gmt[zone][1]
        while (m < 0){
            m += 60
            h -= 1
        }
        while (m >= 60){
            m -= 60
            h += 1
        }
        while (h < 0){
            h += 24
            // TODO: day?
        }
        while (h >= 24){
            h -= 24
            // TODO: day?
        }
        let time = ""
        if (h < 10){time += "0";}
        time += h + ":"
        if (m < 10){time += "0";}
        time += m + " " + zone
        es[i].innerHTML = time
    }
}

function page_load_update_timezone(){
    e = document.getElementById("tzselect")
    keys = Object.keys(difference_to_gmt)
    for (let i = 0; i < keys.length; i++){
        let opt = document.createElement('option');
        opt.value = keys[i];
        opt.innerHTML = keys[i];
        e.appendChild(opt);

        if (keys[i] == zone){
            e.selectedIndex = i;
        }
    }
    update_timezones()
}
