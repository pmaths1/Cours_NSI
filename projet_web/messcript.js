var listenb = document.getElementById('nbde');
var rep = parseInt(document.getElementById('rep').value);
var listedes = document.getElementById('mesdes').getElementsByTagName('li');
var tbody = document.getElementById('donnees');
var couleur = ["#70CCC3","#26998D", "#A6FFC4","#FF66A5","#CC70C4"];
var sommes= {};
var freq = {};
var ancien = 1;
var demax = 1;
var res= [];


function de(){ // résultat d’un lancer de dé
    return  Math.floor(Math.random() * 6 ) + 1 ;
  };

// Calcul les fréquences
function stat(){
    T = 0 ;
    for(i in sommes){
      T += sommes[i];
    } // T est l'effectif total
    for(i in sommes){
      freq[i] = sommes[i]/T;
    }
  };

// Affiche un graphique
function graphe(){
  var canvas = document.getElementById('graphe');
  var parent = document.getElementById('main');
  canvas.width = parent.clientWidth - 20;
  var ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.restore();
  M = 0;
  for (i in freq){
    v=freq[i]
    if (v>M){
      M=v
    };
  }; // M est le maximum des fréquences
  index = 0;
  for (i in freq){
    index += 1;
    ctx.fillStyle = couleur[index %5];
    x = index*20;
    y = Math.floor((canvas.height-25)*freq[i]/M);
    ctx.fillRect(x,canvas.height-25-y,15,y);
    ctx.fillText(i,x+1,canvas.height-10);
    ctx.stroke();
  };
};

// Affiche les résultats avec les fréquences
function aff(){
  tbody.innerHTML = "\n";
  for( d in sommes ){
      tr = '<tr><td>'+d+'</td><td>'+sommes[d]+'</td><td>'+parseFloat(freq[d]*100).toFixed(2)+'</td></tr>';
      tbody.innerHTML += tr;
  };
};

// lance les dés et mise
function lance_des(){
  // Affiche le résultat des dés - méthode des sprites
    var S = 0;
    res = []; // garde la liste des résultats des dés pour l'affichage du dernier lancer
    for (i = 0 ; i< demax; i++ ){
      n=de();
      res.push(n);
      S = S+n;
    };
    // enregistrement des résultats
    if (S in sommes){
      sommes[S] += 1
    }else{
      sommes[S] =1;
    };
};

// fonction appelée après avoir cliqué sur lancer
function jet_des(){
    ancien = demax;
    rep = parseInt(document.getElementById('rep').value);
    demax = parseInt(listenb.options[listenb.selectedIndex].value);

    if (ancien != demax){
      sommes = {};
      freq = {};
    }
    for(k = 0; k <rep; k++){
      lance_des();
    };
    for (i = 0 ; i< demax; i++ ){
      listedes[i].setAttribute("class", "de"+res[i]); // Affiche le résultat du dernier dé
    };
    for (i = demax ; i < listedes.length; i++ ){
      listedes[i].setAttribute("class", "cache"); // Efface les dés inutiles
    };

  stat();
  aff();
  graphe();
};

// Association du bouton à la fonction
var jouer = document.getElementById('lancer');
jouer.addEventListener("click",jet_des);
