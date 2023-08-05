 //membuat count uniq untuk membuat nama file menjadi unik agar halaman mendapatkan audio terbaru
 var count = 0;

 function extractSelectedText(event) {
   event.preventDefault();

   var externalHtml = document.getElementById("external-html");
   var externalDoc = externalHtml.contentDocument || externalHtml.contentWindow.document;
   var selectedText = externalDoc.getSelection().toString();

   var select = document.getElementById("lang");
   var selectedValue = select.value;

   //cek apakah ada tag audio, jika tidak maka hapus
   var div = document.getElementById("audio");
   var audio = document.querySelector("audio");

   if (div.contains(audio))
   {
     div.removeChild(audio);
   }

   //membuat count uniq untuk membuat nama file menjadi unik agar halaman mendapatkan audio terbaru
   if (count > 2) {
     count = 0;
   }
   else {
     count +=1;
   }

   console.log(count)

   var xhr = new XMLHttpRequest();
   var url = "/upload";
   xhr.open("POST", url, true);
   xhr.setRequestHeader("Content-Type", "application/json");
   xhr.onreadystatechange = function() {
     if (xhr.readyState === 4 && xhr.status === 200) {
       var response = JSON.parse(xhr.responseText);
       document.getElementById("translated-text").innerText = "" + response.translated;

       // Menambahkan elemen audio
       var div = document.getElementById("audio");
       var audio = document.createElement("audio");
       audio.src = `${response.location_audio}/${count}${response.name_audio}`;
       audio.setAttribute("controls", "");
       div.appendChild(audio);

     } else if (xhr.readyState === 4) {
       console.log(xhr.responseText);
     }
   };
   var data = JSON.stringify({ text_input: selectedText, lang: selectedValue, count: count});
   xhr.send(data);
 }