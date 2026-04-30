<h1>Projet 3</h1>


<html><head></head><body><div align="center">
  <h1 style="color: white; border-bottom: 2px solid rgb(46, 134, 222); padding-bottom: 10px; background:green; border-radius:3px">
    Weather For All
  </h1>
  <p style="font-style: italic; color: rgb(87, 101, 116);">
    Application Python orientée objet pour l'analyse météorologique en temps réel.
  </p>
</div>

<hr style="border: 0.5px solid whitesmoke; margin: 20px 0;">

<h2 style="color:orange; border-left: 5px solid orange; padding-left: 15px;">
  Auteurs du Projet
</h2>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
  <tbody><tr style="background-color: rgb(2, 19, 36);">
    <th style="padding: 12px; border: 1px solid whitesmoke; text-align: left;">Nom et Prénoms</th>
    <th style="padding: 12px; border: 1px solid whitesmoke; text-align: left;">Profil</th>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid whitesmoke;">
      <strong>André Sèhomi Basile KOVOHOUANDE</strong>
    </td>
    <td style="padding: 12px; border: 1px solid whitesmoke;">Etudiant en 2è année en <b><i>informatique de gestion</i></b> - IUT,UP</td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid white;">
      <strong>Daniella GAMBIALA</strong>
    </td>
    <td style="padding: 12px; border: 1px solid whitesmoke;">Etudiante en 2è année en <b><i>informatique de gestion</i></b> - IUT,UP</td>
  </tr>
</tbody></table>

<h2 style="color: rgb(16, 172, 132); border-left: 5px solid rgb(16, 172, 132); padding-left: 15px; margin-top: 30px;">
   Composant clés du système
</h2>

<div style="color: rgb(236, 240, 241); padding: 15px; border-radius: 8px; font-family: monospace;">
 <li>module de gestion de fichier</li>
 <li>module de gestion du fichier de sauvegarde de données(fichier JSON)</li>
 <li>module de fonctions utilisées dans l'application</li>
 <li>classes</li>
</div>

<h2 style="color: rgb(243, 156, 18); border-left: 5px solid rgb(243, 156, 18); padding-left: 15px; margin-top: 30px;">
    Configuration et Installation
</h2>

<p>Pour faire fonctionner ce projet sur votre machine :</p>

<ol>
   <li>
      <h3>Clonage du projet</h3>
      Ouvrez votre terminal dans le dossier de destination et exécutez la commande suivante :  

```Bash
git clone https://github.com/Andre-Basile/Explorateur-meteo-API.git
cd Explorateur-meteo-API
```
   </li>
   <li>
      <h3>Configuration de l'environnement (Recommandé)</h3>
      Créer un environnement virtuel pour isoler les dépendances du projet :

```Bash
python -m venv venv
```
  </li>
   <li>
      <h3>Installation des dépendances</h3>
      Installez tous les modules nécessaires listés dans le fichier requirements.txt avec la commande(installer pip si non installé):

```Bash
pip install -r requirements.txt
```
   </li>
   <li>
      <h3>Configuration de la clé API OpenWeatherMap</h3>
      L'application nécessite une clé de service pour fonctionner :

<div style="border:2px solid orange; border-radius:8px; margin:10px; padding:10px">
        <ul>
          <li>Rendez-vous sur le site : [https://openweathermap.org/](https://openweathermap.org/)</li>
          <li>Créez un compte ou connectez-vous.</li>
          <li>Accédez à la section API keys de votre profil et copiez votre clé.</li>
          <li>À la racine du projet, renommez le fichier <b>.env.exemple</b> en <b>.env</b></li>
          <li>Ouvrez ce nouveau fichier <b>.env</b> et remplacez la valeur par votre clé récupérée depuis le site</li>
        </ul>
</div>
   </li>

   <li>
      <h3>Lancement de l'application</h3>
      Une fois la configuration terminée, lancez le programme avec :

```Bash
py main.py
```
   </li>
</ol>

<hr style="border: 0.5px solid whitesmoke; margin: 30px 0;">

<div align="center" style="color: rgb(127, 140, 141); font-size: 0.9em;">
  <p>Projet réalisé à l'Université de Parakou - Avril 2026</p>
  <p>Licence MIT</p>
</div></body></html>