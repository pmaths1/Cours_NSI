// Récupération des éléments utiles du document html
// ...

// Variables partagées par les différentes fonctions du script
var couleur = ["#70CCC3","#26998D", "#A6FFC4","#FF66A5","#CC70C4"]; // couleurs du diagramme
var sommes= {};
var freq = {};
/// ...

function de(){ // Donne le résultat d’un lancer de dé,
               // soit un nombre aléatoire entre 1 et 6
    return  Math.floor(Math.random() * 6) + 1 ;
  };

function stat(){ // Calcul les fréquences
    T = 0 ;
    for(i in sommes){
      T += sommes[i] ;
    } // T est l'effectif total
    for(i in sommes){
      freq[i] = sommes[i]/T ;
    }
  } ;

// Affiche un graphique
function graphe(){
  var canvas = document.getElementById('graphe');
  var parent = document.getElementById('main');
  canvas.width = parent.clientWidth - 20;
  var ctx = canvas.getContext('2d');
  // (Ré)initialisation du graphique
  // ...
  // Calcul de M, maximum des fréquences
  // ...
  index = 0;
  for (i in freq){
    // Affichage des rectangles du diagramme en bâtons
    // Affichage de la somme associée
    // ...
  };
};

// Affiche les résultats dans le tableau selon les fréquences
function aff(){
  // ...
};

// lance les dés et met à jour les données
function lance_des(){
    var S = 0; // somme des dés du lancer
    res = []; // garde la liste des résultats des dés pour l'affichage du dernier lancer
    for (i = 0 ; i< demax; i++ ){
      // lancer un dé, mise à jour des variables
      // ...
    };
    // mise à jour de la variable sommes
    // ...
};

// fonction appelée après avoir cliqué sur lancer
function jet_des(){
    ancien = demax;
    rep = parseInt(document.getElementById('rep').value);
    demax = parseInt(listenb.options[listenb.selectedIndex].value);

    // Vérifier si le nombre de dés a changé, et remettre à zéro les donnés si c’est le cas
    // ...
    // lancer les dés puis afficher le dernier résultat
    // ...
    // Calcule les statistiques, affiche le tableau puis le graphique
    // ...
};

// Association du bouton à la fonction
// ...
