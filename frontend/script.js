const API = "http://127.0.0.1:8000"

async function loadRevenue(){

const res = await fetch(API + "/api/revenue")
const json = await res.json()

const data = json.data

let list = document.getElementById("revenue")

data.forEach(r=>{
let li = document.createElement("li")
li.innerText = r.order_year_month + " : ₹" + r.revenue
list.appendChild(li)
})

}

async function loadCustomers(){

const res = await fetch(API + "/api/top-customers")
const json = await res.json()

const data = json.data

let list = document.getElementById("customers")

data.forEach(c=>{
let li = document.createElement("li")
li.innerText = c.name + " ("+c.region+") : ₹" + c.total_spend
list.appendChild(li)
})

}

async function loadCategories(){

const res = await fetch(API + "/api/categories")
const json = await res.json()

const data = json.data

let list = document.getElementById("categories")

data.forEach(c=>{
let li = document.createElement("li")
li.innerText = c.category + " : ₹" + c.total_revenue
list.appendChild(li)
})

}

async function loadRegions(){

const res = await fetch(API + "/api/regions")
const json = await res.json()

const data = json.data

let list = document.getElementById("regions")

data.forEach(r=>{
let li = document.createElement("li")
li.innerText = r.region + " | Revenue ₹" + r.total_revenue
list.appendChild(li)
})

}

loadRevenue()
loadCustomers()
loadCategories()
loadRegions()