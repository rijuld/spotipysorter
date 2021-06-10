

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById("page1next").addEventListener("click", next);
  document.getElementById("page1remove").addEventListener("click", remove);
  document.getElementById("page1add").addEventListener("click", add);
  document.getElementById("page1edit").addEventListener("click", edit);
  document.getElementById("page1save").addEventListener("click", save);


  function next() { location.reload(); }

  function add() {
    fetch(`/page1add`, { method: 'POST', body: JSON.stringify({ id: id }) })
      .then(response => response.json()).then(result => { alert("hurray! added") });
  }
  function remove() {
    fetch(`/page1remove`, { method: 'POST', body: JSON.stringify({ id: id }) })
      .then(response => response.json()).then(result => { alert("hurray! removed") });
  }
  function edit() {
    document.getElementById("page1edit").style.display = "none";
    document.getElementById("page1cardbody").style.display = "none";
    document.getElementById("page1save").style.display = "block";
    document.getElementById("page1textarea").style.display = "block";
  }
  function save() {
    text = document.getElementById("texta").value;
    fetch(`/page1textarea`, { method: 'POST', body: JSON.stringify({ id: id ,text: text}) })
      .then(response => response.json()).then(result => {var url = $("#Url").attr("data-url"); window.location.replace(url);});
    document.getElementById("page1edit").style.display= "block";
    document.getElementById("page1cardbody").style.display = "block";
    document.getElementById("page1cardbody").value = text;
    document.getElementById("page1save").style.display = "none";
    document.getElementById("page1textarea").style.display = "none";
  }


})



