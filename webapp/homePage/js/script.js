function getBookCached() {
    let baseUrlServer = "http://bara111.pythonanywhere.com"; //main server for catalog
    let baseUrlFirstRplica = "http://bara1111.pythonanywhere.com"; // second server for catalog
    let x = "" + document.getElementById("searchItem").value;
    let obj = ""
    let url = ""
    let query = ""
    let serverID = "serverID"
    let e = document.getElementById("type");
    let strUser = e.options[e.selectedIndex].text;
    console.log(localStorage.length);
    if (localStorage.hasOwnProperty(serverID)) { // localStorage serverID check the id of the main server or the other two replicas 1 for main server, 2 for the second server, 3 for the third server
        let ID = localStorage.getItem(serverID);
        if (ID == "1" && strUser == "DOS") {
            query = "/search/dos?dos=" + x;
            url = baseUrlServer + query;
            getDataFromNetwork(url, query);
            localStorage.setItem(serverID, "2");

        } else if (ID == "2" && strUser == "DOS") {
            query = "/search/dos?dos=" + x;
            url = baseUrlFirstRplica + query;
            getDataFromNetwork(url, query);
            localStorage.setItem(serverID, "1");

        } else if (ID == "1" && strUser == "graduate school") {
            query = "/search/graduateSchool?id=" + x;
            url = baseUrlServer + query;
            getDataFromNetwork(url, query);
            localStorage.setItem(serverID, "2");

        } else if (ID == "2" && strUser == "graduate school") {
            query = "/search/graduateSchool?id=" + x;
            url = baseUrlFirstRplica + query;
            getDataFromNetwork(url, query);
            localStorage.setItem(serverID, "1");

        } else if (ID == "1" && strUser == "ID") {
            query = "/search/id?id=" + x;
            url = baseUrlServer + query;
            getDataFromNetwork(url, query);
            localStorage.setItem(serverID, "2");

        } else if (ID == "2" && strUser == "ID") {
            query = "/search/id?id=" + x;
            url = baseUrlFirstRplica + query;
            getDataFromNetwork(url, query);
            localStorage.setItem(serverID, "1");

        }
    } else { //first time send
        localStorage.setItem(serverID, "1");
        if (strUser == "DOS") {
            query = "/search/dos";
            url = baseUrlServer + query; //search by DOS catagory
            getDataFromNetwork(url, query);
        } else if (strUser == "graduate school") {
            query = "/search/graduateSchool";
            url = baseUrlServer + query; //search by graduate school catagory
            getDataFromNetwork(url, query);
        } else if (strUser == "ID") {
            query = "/search/id?id=" + x;
            url = baseUrlServer + query; //search by ID
            console.log(url);
            getDataFromNetwork(url, query);
        }
    }
}

function getDataFromNetwork(url, query) {
    if (localStorage.hasOwnProperty(query)) { //check of request is has been made before
        let dataJson = JSON.parse(getWithExpiry(query));
        updateUiBookResult(dataJson);
    } else {
        fetch(url)
            .then(function(response) {
                return response.json();
            }).then(function(obj) {
                console.log(obj)
                setWithExpiry(query, JSON.stringify(obj), 600000);
                updateUiBookResult(obj)
            })
    }
}


function setWithExpiry(key, value, ttl) { // set cache result into local storage browser with custom TTL value
    const now = new Date()
    const item = {
        value: value,
        expiry: now.getTime() + ttl
    }
    localStorage.setItem(key, JSON.stringify(item))
}

function getWithExpiry(key) { // get cache result from local storage browser
    const itemStr = localStorage.getItem(key)
    if (!itemStr) {
        return null
    }
    const item = JSON.parse(itemStr)
    const now = new Date()
    if (now.getTime() > item.expiry) {
        localStorage.removeItem(key)
        return null
    }
    return item.value
}

function updateUiBookResult(myObj) {
    var x = "";
    for (var i = 0; i < myObj.book.length; i++) {
        var user = myObj.book[i];

        x += '<div class="doctor-card">' +
            '<div class="info">' +
            '<div class="avatar">' +
            '<img src="https://image.freepik.com/free-vector/book-cartoon_22350-95.jpg" alt="doc name">' +
            '</div>' +
            '<div class="details">' +
            '<div class="name">' + user.name + '</div>' +
            '</div>' +
            '</div>' +
            '<div class="actions">' +
            '<div class="comments">' +
            '<span class="comment-count">' + '<strong>' + user.quantity + '</strong> Qunatity</span>' +
            '</div>' +
            '<div class="consultation">' +
            '<span class="fee"><strong>34$</strong>Price</span>' +
            '</div>' +
            '<div class="appo">' +
            '<a onclick=' + console.log(user.id) + 'href="#" class="btn">BUY</a>' +
            '</div>' +
            '</div>' +
            '</div>'
    }
    document.getElementById("demo").innerHTML = x;
}

function buyBook() { // buy item from bazar by id
    let x = "" + document.getElementById("searchItemBuy").value;
    let obj = ""
    let url = ""
    let serverID = "serverIdBuy"
    let baseUrlServer = "http://ambara059.pythonanywhere.com"; // main server for buying books
    let baseUrlFirstRplica = "http://ambara056.pythonanywhere.com"; // second server for buying books
    let e = document.getElementById("typeBuy");
    let strUser = e.options[e.selectedIndex].text;
    if (localStorage.hasOwnProperty(serverID)) {
        let ID = localStorage.getItem(serverID);
        if (ID == "1" && strUser == "DOS") {
            query = "/buy/dos/id?id=" + x;
            url = baseUrlServer + query;
            handleBuyRequest(url, query);
            localStorage.setItem(serverID, "2");
        } else if (ID == "2" && strUser == "DOS") {
            query = "/buy/dos/id?id=" + x;
            url = baseUrlFirstRplica + query;
            handleBuyRequest(url, query);
            localStorage.setItem(serverID, "1");
        } else if (ID == "1" && strUser == "graduate school") {
            query = "/buy/graduateSchool/id?id=" + x;
            url = baseUrlServer + query;
            handleBuyRequest(url, query);
            localStorage.setItem(serverID, "2");
        } else if (ID == "2" && strUser == "graduate school") {
            query = "/buy/graduateSchool/id?id=" + x;
            url = baseUrlFirstRplica + query;
            handleBuyRequest(url, query);
            localStorage.setItem(serverID, "1");
        }

    } else {
        localStorage.setItem(serverID, "1");
        if (strUser == "DOS") {
            url = baseUrlServer + "/buy/dos/id?id=" + x;
        } else if (strUser == "graduate school") {
            url = baseUrlServer + "/buy/graduateSchool/id?id=" + x;
        }
    }
}

function handleBuyRequest(url, query) {
    fetch(url)
        .then(function(response) {
            console.log(response.status); // server push an invalidate an update for database to clear the cache of the old response in order to get the right data
            if (response.status == "200") {
                localStorage.clear();
            }
            return response
        }).then(function(obj) {
            console.log(obj);
            window.alert(obj);

        })
}
