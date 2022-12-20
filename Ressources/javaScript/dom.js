getElementById('yourId') /* retourne l'element qui a identifiant yourId    */;
getElementsByClassName('className') /* retourne une collection d'element ayant la classe className */
getElementByTagName('tagHTML') /* retourne la balise HTML */
querySelector('selector css') /* retoure le premier element correspondant au selecteur specifiés */
querySelectorAll('selector css') /* retoure tous les elements correspondant au(x) selecteur specifiés */
lastElementChild() /* recupère le dernier enfant de l'element */
lastChild() /* recupère le dernier noeud enfant de l'element */
nextSibling() /* obtient le noeud suivant situé au même niveau */
nextElementSibling() /* obtient l'element suivant situé au même niveau de noeud */
nodeName() /* recupère le nom du noeud courant */
parentNode() /* recupère le noeud parent de l'element */
parentElement() /* recupère l'élément parent de l'élément */
previousSibling() /* obtient le noeud précédent situé au même niveau */
previousElementSibling() /* obtient l'élément précédent situé au même niveau de noeud */
childElementCount() /* récupère le nombre d'élément enfants dans le noeud spécifié */
childNodes() /* récupère une liste des noeuds enfants de l'élément */
classList() /* récupère une liste ou les noms de classe de l'élément */
className() /* récupère ou definit la valeur de l'attribut de classe de l'élément */
firstChild() /* le noeud premier enfant */
firstElementChild() /* premier enfant */
removeChild() /* supprimer l'élément */
/* événements */

addEventListener('eventName',callBackFunction,false) /* ajouter un écouteur d'événement */
/* quelques eventName*/
click // sur le clic
focus // réception de focus
blur // perte de focus 
submit // soumission de formulaire 
load // chargement de la page 

// callBackFunction est la fonction à appeler quand l'événement est lieu 

